#!/usr/bin/env python3
"""
Release notes generator using AI to categorize GitHub commits and pull requests.

From the Doc360Talk webinar: "From Writer to Tool Builder"
Educational example demonstrating AI-assisted automation for technical writers.
"""

import os
import sys
import argparse
import yaml
from datetime import datetime
from typing import List, Dict, Optional
from pathlib import Path

# Try importing required libraries with helpful error messages
try:
    from github import Github, GithubException
except ImportError:
    print("❌ Error: PyGithub not installed")
    print("   Run: pip install PyGithub")
    sys.exit(1)

try:
    import anthropic
    HAS_ANTHROPIC = True
except ImportError:
    HAS_ANTHROPIC = False

try:
    import openai
    HAS_OPENAI = True
except ImportError:
    HAS_OPENAI = False

if not HAS_ANTHROPIC and not HAS_OPENAI:
    print("❌ Error: No AI provider library installed")
    print("   Run: pip install anthropic   (for Claude)")
    print("   or:  pip install openai      (for GPT)")
    sys.exit(1)


def load_config(config_path: str = "../config.yaml") -> Dict:
    """Load configuration from YAML file or environment variables."""
    config = {}
    
    # Try loading from file
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f) or {}
    
    # Override with environment variables if present
    if os.getenv('AI_PROVIDER'):
        config['ai_provider'] = os.getenv('AI_PROVIDER')
    if os.getenv('AI_API_KEY'):
        config['ai_api_key'] = os.getenv('AI_API_KEY')
    if os.getenv('AI_MODEL'):
        config['model'] = os.getenv('AI_MODEL')
    if os.getenv('GITHUB_TOKEN'):
        config['github_token'] = os.getenv('GITHUB_TOKEN')
    
    # Validate required fields
    required_fields = ['ai_provider', 'ai_api_key', 'model', 'github_token']
    missing_fields = [f for f in required_fields if f not in config or not config[f] or config[f] == 'YOUR_API_KEY_HERE' or config[f] == 'YOUR_GITHUB_TOKEN_HERE']
    
    if missing_fields:
        print(f"❌ Error: Missing required configuration: {', '.join(missing_fields)}")
        print(f"\nPlease update {config_path} with your API keys")
        print("Or set environment variables:")
        for field in missing_fields:
            print(f"  export {field.upper()}='your-value'")
        sys.exit(1)
    
    return config


def get_sample_commits() -> List[Dict]:
    """Return sample commits for testing without API calls."""
    return [
        {
            "sha": "abc123",
            "message": "Add user authentication feature with OAuth2 support",
            "author": "developer@example.com",
            "date": "2024-01-15",
            "url": "https://github.com/sample/repo/commit/abc123"
        },
        {
            "sha": "def456",
            "message": "Fix memory leak in parser that caused high RAM usage",
            "author": "developer@example.com",
            "date": "2024-01-16",
            "url": "https://github.com/sample/repo/commit/def456"
        },
        {
            "sha": "ghi789",
            "message": "Update API documentation with new authentication endpoints",
            "author": "writer@example.com",
            "date": "2024-01-17",
            "url": "https://github.com/sample/repo/commit/ghi789"
        },
        {
            "sha": "jkl012",
            "message": "Improve search performance by 50% through better indexing",
            "author": "developer@example.com",
            "date": "2024-01-18",
            "url": "https://github.com/sample/repo/commit/jkl012"
        },
        {
            "sha": "mno345",
            "message": "Update CI/CD pipeline configuration",
            "author": "devops@example.com",
            "date": "2024-01-19",
            "url": "https://github.com/sample/repo/commit/mno345"
        },
        {
            "sha": "pqr678",
            "message": "Resolve login timeout issue affecting mobile users",
            "author": "developer@example.com",
            "date": "2024-01-20",
            "url": "https://github.com/sample/repo/commit/pqr678"
        },
        {
            "sha": "stu901",
            "message": "Create new dashboard analytics view",
            "author": "developer@example.com",
            "date": "2024-01-21",
            "url": "https://github.com/sample/repo/commit/stu901"
        },
        {
            "sha": "vwx234",
            "message": "Introduce webhook support for third-party integrations",
            "author": "developer@example.com",
            "date": "2024-01-22",
            "url": "https://github.com/sample/repo/commit/vwx234"
        }
    ]


def fetch_commits(repo: str, since_date: str, config: Dict, use_sample: bool = False) -> List[Dict]:
    """
    Fetch commits from GitHub API.
    
    Args:
        repo: Repository in format "owner/repo"
        since_date: ISO date string (YYYY-MM-DD)
        config: Configuration dictionary with github_token
        use_sample: If True, return sample data instead of API call
    
    Returns:
        List of commit dictionaries with keys: sha, message, author, date, url
    """
    if use_sample:
        print("Using sample commits (no API calls)")
        return get_sample_commits()
    
    try:
        # Initialize GitHub client
        g = Github(config['github_token'])
        
        # Get repository
        repository = g.get_repo(repo)
        
        # Parse date
        since = datetime.strptime(since_date, '%Y-%m-%d')
        
        # Fetch commits
        commits = repository.get_commits(since=since)
        
        # Convert to our format
        commit_list = []
        for commit in commits:
            commit_list.append({
                'sha': commit.sha[:7],  # Short SHA
                'message': commit.commit.message.split('\n')[0],  # First line only
                'author': commit.commit.author.email if commit.commit.author else 'unknown',
                'date': commit.commit.author.date.strftime('%Y-%m-%d') if commit.commit.author else since_date,
                'url': commit.html_url
            })
        
        return commit_list
        
    except GithubException as e:
        print(f"❌ GitHub API Error: {e.data.get('message', str(e))}")
        if e.status == 401:
            print("   Check your GitHub token is valid and not expired")
        elif e.status == 404:
            print(f"   Repository '{repo}' not found or not accessible")
        elif e.status == 403:
            print("   Rate limit exceeded or insufficient permissions")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error fetching commits: {e}")
        sys.exit(1)

def load_prompt_template(prompt_path: str) -> str:
    """Load categorization prompt template."""
    if not os.path.exists(prompt_path):
        print(f"❌ Error: Prompt file not found: {prompt_path}")
        print(f"   Make sure you're running from the 01-release-notes-automation/ directory")
        sys.exit(1)
    
    with open(prompt_path, 'r') as f:
        return f.read()


def categorize_commits(commits: List[Dict], config: Dict, prompt_path: str = "prompts/categorization_prompt.txt") -> str:
    """
    Use AI to categorize commits into release note categories.
    
    Args:
        commits: List of commit dictionaries
        config: Configuration dictionary with AI settings
        prompt_path: Path to categorization prompt template
    
    Returns:
        Formatted markdown string with categorized commits
    """
    if not commits:
        return "No commits found for categorization."
    
    # Load prompt template
    prompt_template = load_prompt_template(prompt_path)
    
    # Format commits for AI
    commits_text = "\n".join([
        f"- {c['message']} ([{c['sha']}]({c['url']}))"
        for c in commits
    ])
    
    # Construct full prompt
    full_prompt = prompt_template.replace("{COMMITS}", commits_text)
    
    # Call AI API based on provider
    provider = config['ai_provider'].lower()
    
    try:
        if provider == 'anthropic':
            if not HAS_ANTHROPIC:
                print("❌ Error: Anthropic library not installed")
                print("   Run: pip install anthropic")
                sys.exit(1)
            
            client = anthropic.Anthropic(api_key=config['ai_api_key'])
            
            message = client.messages.create(
                model=config['model'],
                max_tokens=3000,
                temperature=0.3,
                messages=[{
                    "role": "user",
                    "content": full_prompt
                }]
            )
            
            response_text = message.content[0].text
            
        elif provider == 'openai':
            if not HAS_OPENAI:
                print("❌ Error: OpenAI library not installed")
                print("   Run: pip install openai")
                sys.exit(1)
            
            client = openai.OpenAI(api_key=config['ai_api_key'])
            
            response = client.chat.completions.create(
                model=config['model'],
                messages=[{
                    "role": "user",
                    "content": full_prompt
                }],
                max_tokens=3000,
                temperature=0.3
            )
            
            response_text = response.choices[0].message.content
            
        else:
            print(f"❌ Error: Unknown AI provider: {provider}")
            print("   Supported providers: anthropic, openai")
            sys.exit(1)
        
        return response_text
        
    except Exception as e:
        print(f"❌ AI API Error: {e}")
        print("\nTroubleshooting:")
        print("1. Check your API key is valid")
        print("2. Verify billing is set up (after free tier)")
        print("3. Check rate limits")
        sys.exit(1)

def generate_release_notes(ai_response: str, since_date: str, repo: str) -> str:
    """
    Generate formatted release notes with header.
    
    Args:
        ai_response: Categorized commits from AI (already formatted)
        since_date: Start date for the period
        repo: Repository name
    
    Returns:
        Complete release notes markdown
    """
    output = "# Release Notes\n\n"
    output += f"**Repository:** {repo}\n"
    output += f"**Date:** {datetime.now().strftime('%Y-%m-%d')}\n"
    output += f"**Period:** Since {since_date}\n\n"
    output += "---\n\n"
    output += ai_response
    output += "\n\n---\n\n"
    output += "_Generated using AI-assisted automation. Please review for accuracy before publishing._\n"
    
    return output


def main():
    parser = argparse.ArgumentParser(
        description='Generate release notes from GitHub commits using AI categorization',
        epilog='Example: python generate_release_notes.py --repo octocat/Hello-World --since 2024-01-01'
    )
    parser.add_argument('--repo', help='Repository (owner/repo)')
    parser.add_argument('--since', required=True, help='Start date (YYYY-MM-DD)')
    parser.add_argument('--until', help='End date (YYYY-MM-DD), defaults to today')
    parser.add_argument('--config', default='../config.yaml', help='Config file path')
    parser.add_argument('--output', default='release_notes.md', help='Output file')
    parser.add_argument('--prompt', default='prompts/categorization_prompt.txt', help='Prompt file path')
    parser.add_argument('--sample', action='store_true', help='Use sample data instead of API calls')
    
    args = parser.parse_args()
    
    print("🚀 Release Notes Automation")
    print("=" * 50)
    
    # Load configuration
    config = load_config(args.config)
    
    # Determine repository
    repo = args.repo or config.get('default_repo')
    if not repo:
        print("❌ Error: No repository specified")
        print("   Use --repo owner/repo or set default_repo in config.yaml")
        sys.exit(1)
    
    # Fetch commits
    print(f"\n📥 Fetching commits from {repo} since {args.since}...")
    commits = fetch_commits(repo, args.since, config, use_sample=args.sample)
    print(f"✓ Found {len(commits)} commits")
    
    if not commits:
        print("\n⚠️  No commits found in specified date range")
        print("   Try adjusting --since date or check repository access")
        sys.exit(0)
    
    # Categorize using AI
    print(f"\n🤖 Categorizing commits using {config['ai_provider'].upper()} ({config['model']})...")
    categorized_text = categorize_commits(commits, config, args.prompt)
    print("✓ Categorization complete")
    
    # Generate release notes
    print("\n📝 Generating release notes...")
    notes = generate_release_notes(categorized_text, args.since, repo)
    
    # Write output
    with open(args.output, 'w') as f:
        f.write(notes)
    
    print(f"✓ Release notes written to {args.output}")
    print("\n" + "=" * 50)
    print("✅ Done! Review the output and make any needed adjustments.")
    print(f"\n💡 Next steps:")
    print(f"   1. Review {args.output}")
    print(f"   2. Add context for major changes")
    print(f"   3. Verify categorization accuracy")
    print(f"   4. Publish when ready")
    
    # Show preview
    print(f"\n📄 Preview (first 500 characters):")
    print("-" * 50)
    print(notes[:500] + "..." if len(notes) > 500 else notes)
    print("-" * 50)


if __name__ == "__main__":
    main()
