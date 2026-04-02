#!/usr/bin/env python3
"""
Release notes generator using AI to categorize VCS commits.
Supports GitHub, GitLab, and Bitbucket as VCS sources.
Supports Anthropic, OpenAI, and Azure OpenAI as AI providers.

From the Doc360Talk webinar: "From Writer to Tool Builder"
Educational example demonstrating AI-assisted automation for technical writers.
"""

import os
import sys
import argparse
import re
import yaml
from datetime import datetime
from typing import List, Dict, Optional
from pathlib import Path

# ─── Optional dependency detection ───────────────────────────────────────────

try:
    from github import Github, GithubException
    HAS_GITHUB = True
except ImportError:
    HAS_GITHUB = False

try:
    import gitlab as _gitlab
    HAS_GITLAB = True
except ImportError:
    HAS_GITLAB = False

try:
    from atlassian import Bitbucket as _Bitbucket
    HAS_BITBUCKET = True
except ImportError:
    HAS_BITBUCKET = False

try:
    import anthropic as _anthropic
    HAS_ANTHROPIC = True
except ImportError:
    HAS_ANTHROPIC = False

try:
    import openai as _openai
    HAS_OPENAI = True
except ImportError:
    HAS_OPENAI = False

try:
    from jinja2 import Environment, FileSystemLoader, BaseLoader
    HAS_JINJA2 = True
except ImportError:
    HAS_JINJA2 = False

if not HAS_ANTHROPIC and not HAS_OPENAI:
    print("❌ Error: No AI provider library installed")
    print("   Run: pip install anthropic   (for Claude)")
    print("   or:  pip install openai      (for GPT / Azure OpenAI)")
    sys.exit(1)

# ─── Default Jinja2 template ──────────────────────────────────────────────────

DEFAULT_TEMPLATE = """\
# Release Notes

**Repository:** {{ repo }}
**Date:** {{ date }}
**Period:** Since {{ since_date }}

---
{% for category in categories %}
{% if category.commits %}
## {{ category.name }}
{% for commit in category.commits %}
- {{ commit.message }} ([{{ commit.sha }}]({{ commit.url }}))
{% endfor %}

{% endif %}
{% endfor %}
---

_Generated using AI-assisted automation. Please review for accuracy before publishing._
"""


# ─── VCS Provider classes ─────────────────────────────────────────────────────

class GitHubProvider:
    """Fetch commits from GitHub using PyGithub."""

    def fetch_commits(self, repo: str, since_date: str, config: Dict, use_sample: bool = False) -> List[Dict]:
        if use_sample:
            print("Using sample commits (no API calls)")
            return get_sample_commits()

        if not HAS_GITHUB:
            print("❌ Error: PyGithub not installed")
            print("   Run: pip install PyGithub")
            sys.exit(1)

        token = config.get('github_token')
        if not token or token == 'YOUR_GITHUB_TOKEN_HERE':
            print("❌ Error: Missing github_token in config")
            print("   Get one at: github.com/settings/tokens")
            sys.exit(1)

        try:
            g = Github(token)
            repository = g.get_repo(repo)
            since = datetime.strptime(since_date, '%Y-%m-%d')
            commits = repository.get_commits(since=since)
            return [
                {
                    'sha': c.sha[:7],
                    'message': c.commit.message.split('\n')[0],
                    'author': c.commit.author.email if c.commit.author else 'unknown',
                    'date': c.commit.author.date.strftime('%Y-%m-%d') if c.commit.author else since_date,
                    'url': c.html_url,
                }
                for c in commits
            ]
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


class GitLabProvider:
    """Fetch commits from GitLab using python-gitlab."""

    def fetch_commits(self, repo: str, since_date: str, config: Dict, use_sample: bool = False) -> List[Dict]:
        if use_sample:
            print("Using sample commits (no API calls)")
            return get_sample_commits()

        if not HAS_GITLAB:
            print("❌ Error: python-gitlab not installed")
            print("   Run: pip install python-gitlab")
            sys.exit(1)

        token = config.get('gitlab_token')
        if not token or token == 'YOUR_GITLAB_TOKEN_HERE':
            print("❌ Error: Missing gitlab_token in config")
            print("   Get one at: gitlab.com/-/profile/personal_access_tokens")
            sys.exit(1)

        try:
            gl = _gitlab.Gitlab(
                config.get('gitlab_url', 'https://gitlab.com'),
                private_token=token
            )
            project = gl.projects.get(repo)
            commits = project.commits.list(since=since_date, all=True)
            return [
                {
                    'sha': c.id[:7],
                    'message': c.title,
                    'author': c.author_name,
                    'date': c.created_at[:10],
                    'url': c.web_url,
                }
                for c in commits
            ]
        except Exception as e:
            print(f"❌ GitLab API Error: {e}")
            sys.exit(1)


class BitbucketProvider:
    """Fetch commits from Bitbucket using atlassian-python-api."""

    def fetch_commits(self, repo: str, since_date: str, config: Dict, use_sample: bool = False) -> List[Dict]:
        if use_sample:
            print("Using sample commits (no API calls)")
            return get_sample_commits()

        if not HAS_BITBUCKET:
            print("❌ Error: atlassian-python-api not installed")
            print("   Run: pip install atlassian-python-api")
            sys.exit(1)

        username = config.get('bitbucket_username')
        app_password = config.get('bitbucket_app_password')
        if not username or not app_password or app_password == 'YOUR_APP_PASSWORD_HERE':
            print("❌ Error: Missing bitbucket_username or bitbucket_app_password in config")
            print("   Create an app password at: bitbucket.org/account/settings/app-passwords")
            sys.exit(1)

        try:
            bb = _Bitbucket(
                url='https://api.bitbucket.org',
                username=username,
                password=app_password
            )
            since_dt = datetime.strptime(since_date, '%Y-%m-%d')
            raw_commits = bb.get_commits(repository=repo)
            commit_list = []
            for c in raw_commits:
                commit_date_str = c.get('date', '')[:10]
                try:
                    commit_dt = datetime.strptime(commit_date_str, '%Y-%m-%d')
                except ValueError:
                    continue
                if commit_dt < since_dt:
                    break  # Bitbucket returns newest-first; stop at the since boundary
                commit_list.append({
                    'sha': c['hash'][:7],
                    'message': c['message'].split('\n')[0],
                    'author': c.get('author', {}).get('raw', 'unknown'),
                    'date': commit_date_str,
                    'url': c.get('links', {}).get('html', {}).get('href', ''),
                })
            return commit_list
        except Exception as e:
            print(f"❌ Bitbucket API Error: {e}")
            sys.exit(1)


def get_vcs_provider(config: Dict):
    """Return the appropriate VCS provider instance based on config."""
    provider = config.get('vcs_provider', 'github').lower()
    if provider == 'github':
        return GitHubProvider()
    elif provider == 'gitlab':
        return GitLabProvider()
    elif provider == 'bitbucket':
        return BitbucketProvider()
    else:
        print(f"❌ Error: Unknown VCS provider: {provider}")
        print("   Supported providers: github, gitlab, bitbucket")
        sys.exit(1)


# ─── AI Provider classes ──────────────────────────────────────────────────────

class AnthropicProvider:
    """Categorize commits using Anthropic Claude."""

    def __init__(self, config: Dict):
        if not HAS_ANTHROPIC:
            print("❌ Error: Anthropic library not installed")
            print("   Run: pip install anthropic")
            sys.exit(1)
        self.config = config

    def categorize(self, prompt_text: str) -> str:
        client = _anthropic.Anthropic(api_key=self.config['ai_api_key'])
        message = client.messages.create(
            model=self.config['model'],
            max_tokens=3000,
            temperature=0.3,
            messages=[{"role": "user", "content": prompt_text}]
        )
        return message.content[0].text


class OpenAIProvider:
    """Categorize commits using OpenAI GPT."""

    def __init__(self, config: Dict):
        if not HAS_OPENAI:
            print("❌ Error: OpenAI library not installed")
            print("   Run: pip install openai")
            sys.exit(1)
        self.config = config

    def categorize(self, prompt_text: str) -> str:
        client = _openai.OpenAI(api_key=self.config['ai_api_key'])
        response = client.chat.completions.create(
            model=self.config['model'],
            messages=[{"role": "user", "content": prompt_text}],
            max_tokens=3000,
            temperature=0.3
        )
        return response.choices[0].message.content


class AzureOpenAIProvider:
    """Categorize commits using Azure OpenAI."""

    def __init__(self, config: Dict):
        if not HAS_OPENAI:
            print("❌ Error: OpenAI library not installed (required for Azure OpenAI)")
            print("   Run: pip install openai")
            sys.exit(1)
        self.config = config

    def categorize(self, prompt_text: str) -> str:
        client = _openai.AzureOpenAI(
            api_key=self.config['ai_api_key'],
            azure_endpoint=self.config['azure_endpoint'],
            api_version=self.config.get('azure_api_version', '2024-02-01')
        )
        response = client.chat.completions.create(
            model=self.config['model'],
            messages=[{"role": "user", "content": prompt_text}],
            max_tokens=3000,
            temperature=0.3
        )
        return response.choices[0].message.content


def get_ai_provider(config: Dict):
    """Return the appropriate AI provider instance based on config."""
    provider = config['ai_provider'].lower()
    if provider == 'anthropic':
        return AnthropicProvider(config)
    elif provider == 'openai':
        return OpenAIProvider(config)
    elif provider == 'azure_openai':
        return AzureOpenAIProvider(config)
    else:
        print(f"❌ Error: Unknown AI provider: {provider}")
        print("   Supported providers: anthropic, openai, azure_openai")
        sys.exit(1)


# ─── Hybrid categorization ────────────────────────────────────────────────────

# Maps conventional commit prefixes to release note categories
CONVENTIONAL_COMMIT_MAP = {
    'feat': 'New Features',
    'feature': 'New Features',
    'fix': 'Bug Fixes',
    'bugfix': 'Bug Fixes',
    'docs': 'Documentation',
    'doc': 'Documentation',
    'perf': 'Enhancements',
    'refactor': 'Enhancements',
    'chore': 'Enhancements',
    'ci': 'Enhancements',
    'test': 'Enhancements',
}

# Consistent output ordering for all category sources
CATEGORY_ORDER = ['New Features', 'Enhancements', 'Bug Fixes', 'Documentation']


def parse_conventional_commit(message: str) -> Optional[str]:
    """
    Parse a conventional commit prefix and return the matching category name.
    Returns None if the message does not follow conventional commit format.

    Examples:
        "feat: add login page"       → "New Features"
        "fix(auth): token expiry"    → "Bug Fixes"
        "docs!: rewrite readme"      → "Documentation"
        "random commit message"      → None
    """
    match = re.match(r'^(\w+)(\([\w/.-]+\))?!?:\s+', message)
    if match:
        prefix = match.group(1).lower()
        return CONVENTIONAL_COMMIT_MAP.get(prefix)
    return None


def match_keyword_rules(message: str, rules: List[Dict]) -> Optional[str]:
    """
    Match a commit message against user-defined keyword rules.
    Returns the category of the first matching rule, or None.

    Rule format: {"keywords": ["auth", "token"], "category": "Security"}
    Matching is case-insensitive. First matching rule wins.
    """
    message_lower = message.lower()
    for rule in rules:
        for keyword in rule.get('keywords', []):
            if keyword.lower() in message_lower:
                return rule['category']
    return None


def load_categorization_rules(rules_path: Optional[str]) -> List[Dict]:
    """Load keyword categorization rules from a YAML file. Returns [] if file not found."""
    if not rules_path or not os.path.exists(rules_path):
        return []
    with open(rules_path, 'r') as f:
        data = yaml.safe_load(f) or {}
    return data.get('rules', [])


def parse_ai_categories(ai_response: str) -> Dict[str, List[str]]:
    """
    Parse an AI markdown response into {category_name: [commit message strings]}.
    Handles ## Category Name sections with - bullet points.
    """
    categories: Dict[str, List[str]] = {}
    current_category = None
    for line in ai_response.splitlines():
        line = line.strip()
        if line.startswith('## '):
            current_category = line[3:].strip()
            categories[current_category] = []
        elif line.startswith('- ') and current_category is not None:
            categories[current_category].append(line[2:].strip())
    return categories


def categorize_commits_hybrid(
    commits: List[Dict],
    config: Dict,
    prompt_path: str = "prompts/categorization_prompt.txt",
    rules_path: Optional[str] = None,
) -> List[Dict]:
    """
    Categorize commits using a three-stage hybrid strategy:

      Stage 1 — Conventional commits: parse feat:, fix:, docs:, etc. prefixes
      Stage 2 — Keyword rules: match against user-defined keyword→category rules
      Stage 3 — AI fallback: send unmatched commits to the configured AI provider

    Only unmatched commits reach Stage 3, reducing API token usage.

    Returns an ordered list of category dicts for template rendering:
      [{"name": "New Features", "commits": [...]}, ...]
    """
    categorized: Dict[str, List[Dict]] = {}
    unmatched: List[Dict] = []
    rules = load_categorization_rules(rules_path)

    for commit in commits:
        category = parse_conventional_commit(commit['message'])
        if not category and rules:
            category = match_keyword_rules(commit['message'], rules)

        if category:
            categorized.setdefault(category, []).append(commit)
        else:
            unmatched.append(commit)

    if unmatched:
        prompt_template = load_prompt_template(prompt_path)
        commits_text = "\n".join([
            f"- {c['message']} ([{c['sha']}]({c['url']}))"
            for c in unmatched
        ])
        full_prompt = prompt_template.replace("{COMMITS}", commits_text)

        try:
            ai_provider = get_ai_provider(config)
            ai_response = ai_provider.categorize(full_prompt)
            ai_categories = parse_ai_categories(ai_response)

            # Map AI-returned message strings back to original commit dicts
            unmatched_by_msg = {c['message']: c for c in unmatched}
            for category, msg_list in ai_categories.items():
                for msg_text in msg_list:
                    # Strip any markdown link the AI appended, e.g. " ([abc123](url))"
                    base_msg = re.sub(r'\s*\(\[.+?\]\(.+?\)\)\s*$', '', msg_text).strip()
                    commit = unmatched_by_msg.get(base_msg)
                    if not commit:
                        for orig_msg, c in unmatched_by_msg.items():
                            if base_msg in orig_msg or orig_msg in base_msg:
                                commit = c
                                break
                    if commit:
                        categorized.setdefault(category, []).append(commit)
        except SystemExit:
            raise
        except Exception as e:
            print(f"⚠️  AI categorization failed: {e}")
            print("   Unmatched commits will be omitted from output.")

    # Build ordered result; known categories first, then any extras from AI/rules
    seen: set = set()
    result = []
    for name in CATEGORY_ORDER:
        result.append({"name": name, "commits": categorized.get(name, [])})
        seen.add(name)
    for name, commits_in_cat in categorized.items():
        if name not in seen:
            result.append({"name": name, "commits": commits_in_cat})

    return result


# ─── Output rendering ─────────────────────────────────────────────────────────

def generate_release_notes(
    categories: List[Dict],
    since_date: str,
    repo: str,
    config: Optional[Dict] = None,
    template_path: Optional[str] = None,
) -> str:
    """
    Render release notes from categorized commits using a Jinja2 template.

    Uses a custom template if --template is specified, otherwise falls back
    to the built-in default template. If jinja2 is not installed, renders
    using plain string assembly so the script stays usable without it.

    Args:
        categories:    Output of categorize_commits_hybrid()
        since_date:    Start date string (YYYY-MM-DD)
        repo:          Repository name string
        config:        Config dict (used for metadata fields in template)
        template_path: Path to a custom .j2 template file (optional)

    Returns:
        Rendered markdown string
    """
    template_vars = {
        "repo": repo,
        "date": datetime.now().strftime('%Y-%m-%d'),
        "since_date": since_date,
        "categories": categories,
        "ai_provider": (config or {}).get('ai_provider', 'ai'),
        "vcs_provider": (config or {}).get('vcs_provider', 'github'),
    }

    if HAS_JINJA2:
        if template_path and os.path.exists(template_path):
            template_dir = str(Path(template_path).parent)
            template_file = Path(template_path).name
            env = Environment(
                loader=FileSystemLoader(template_dir),
                trim_blocks=True,
                lstrip_blocks=True
            )
            template = env.get_template(template_file)
        else:
            env = Environment(
                loader=BaseLoader(),
                trim_blocks=True,
                lstrip_blocks=True
            )
            template = env.from_string(DEFAULT_TEMPLATE)
        return template.render(**template_vars)

    # Fallback: plain string assembly when jinja2 is not installed
    lines = [
        "# Release Notes\n",
        f"**Repository:** {repo}",
        f"**Date:** {template_vars['date']}",
        f"**Period:** Since {since_date}\n",
        "---\n",
    ]
    for cat in categories:
        if cat["commits"]:
            lines.append(f"## {cat['name']}")
            for c in cat["commits"]:
                lines.append(f"- {c['message']} ([{c['sha']}]({c['url']}))")
            lines.append("")
    lines += ["---\n", "_Generated using AI-assisted automation. Please review for accuracy before publishing._\n"]
    return "\n".join(lines)


# ─── Batch processing ─────────────────────────────────────────────────────────

def run_batch(repos: List[str], args, config: Dict) -> None:
    """
    Process multiple repositories sequentially.

    Output modes (--batch-output):
      separate (default) — one file per repo, named release-notes-{owner}-{repo}.md
      combined           — single file with all repos as sections
    """
    batch_output_mode = getattr(args, 'batch_output', 'separate')
    combined_sections = []

    for repo in repos:
        print(f"\n{'='*50}")
        print(f"📦 Processing {repo}")

        vcs = get_vcs_provider(config)
        commits = vcs.fetch_commits(repo, args.since, config, use_sample=args.sample)
        print(f"✓ Found {len(commits)} commits")

        if not commits:
            print(f"⚠️  No commits found for {repo}, skipping.")
            continue

        print("🤖 Categorizing with hybrid strategy...")
        categories = categorize_commits_hybrid(
            commits, config, args.prompt, getattr(args, 'rules', None)
        )

        if batch_output_mode == 'combined':
            combined_sections.append((repo, categories))
        else:
            notes = generate_release_notes(
                categories, args.since, repo, config, getattr(args, 'template', None)
            )
            filename = f"release-notes-{repo.replace('/', '-')}.md"
            with open(filename, 'w') as f:
                f.write(notes)
            print(f"✓ Written to {filename}")

    if batch_output_mode == 'combined' and combined_sections:
        combined = [
            f"# Release Notes — Batch Report\n",
            f"**Date:** {datetime.now().strftime('%Y-%m-%d')}\n",
        ]
        for repo, categories in combined_sections:
            combined.append(f"---\n\n## Repository: {repo}\n")
            for cat in categories:
                if cat["commits"]:
                    combined.append(f"### {cat['name']}")
                    for c in cat["commits"]:
                        combined.append(f"- {c['message']} ([{c['sha']}]({c['url']}))")
                    combined.append("")
        output_file = getattr(args, 'output', 'release_notes_batch.md')
        with open(output_file, 'w') as f:
            f.write("\n".join(combined))
        print(f"\n✓ Combined report written to {output_file}")


# ─── Utility functions ────────────────────────────────────────────────────────

def load_config(config_path: str = "../config.yaml") -> Dict:
    """Load configuration from YAML file with environment variable overrides."""
    config = {}

    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f) or {}

    env_map = {
        'AI_PROVIDER': 'ai_provider',
        'AI_API_KEY': 'ai_api_key',
        'AI_MODEL': 'model',
        'GITHUB_TOKEN': 'github_token',
        'GITLAB_TOKEN': 'gitlab_token',
        'VCS_PROVIDER': 'vcs_provider',
    }
    for env_var, config_key in env_map.items():
        if os.getenv(env_var):
            config[config_key] = os.getenv(env_var)

    placeholder_values = {
        'YOUR_API_KEY_HERE', 'YOUR_GITHUB_TOKEN_HERE',
        'YOUR_GITLAB_TOKEN_HERE', 'YOUR_APP_PASSWORD_HERE',
    }
    required_fields = ['ai_provider', 'ai_api_key', 'model']
    missing = [
        f for f in required_fields
        if not config.get(f) or config[f] in placeholder_values
    ]

    if missing:
        print(f"❌ Error: Missing required configuration: {', '.join(missing)}")
        print(f"\nPlease update {config_path} with your credentials")
        print("Or set environment variables:")
        for field in missing:
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
    Fetch commits using the configured VCS provider.
    Top-level function kept for backwards compatibility.
    """
    provider = get_vcs_provider(config)
    return provider.fetch_commits(repo, since_date, config, use_sample=use_sample)


def load_prompt_template(prompt_path: str) -> str:
    """Load categorization prompt template from file."""
    if not os.path.exists(prompt_path):
        print(f"❌ Error: Prompt file not found: {prompt_path}")
        print("   Make sure you're running from the 01-release-notes-automation/ directory")
        sys.exit(1)
    with open(prompt_path, 'r') as f:
        return f.read()


# ─── Entry point ──────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description='Generate release notes from VCS commits using AI categorization',
        epilog='Example: python generate_release_notes.py --repo octocat/Hello-World --since 2024-01-01'
    )
    parser.add_argument('--repo', help='Single repository (owner/repo)')
    parser.add_argument('--repos', nargs='+', metavar='REPO',
                        help='Multiple repositories for batch processing')
    parser.add_argument('--since', required=True, help='Start date (YYYY-MM-DD)')
    parser.add_argument('--until', help='End date (YYYY-MM-DD), defaults to today')
    parser.add_argument('--config', default='../config.yaml', help='Config file path')
    parser.add_argument('--output', default='release_notes.md', help='Output file')
    parser.add_argument('--prompt', default='prompts/categorization_prompt.txt',
                        help='Prompt template file path')
    parser.add_argument('--rules', default=None,
                        help='Keyword categorization rules YAML file')
    parser.add_argument('--template', default=None,
                        help='Custom Jinja2 output template (.j2 file)')
    parser.add_argument('--batch-output', choices=['separate', 'combined'], default='separate',
                        help='Batch output mode: separate files per repo or one combined report')
    parser.add_argument('--sample', action='store_true',
                        help='Use sample data (no API calls)')

    args = parser.parse_args()

    print("🚀 Release Notes Automation")
    print("=" * 50)

    config = load_config(args.config)

    # ── Batch mode ────────────────────────────────────────────────────────────
    repos_from_config = config.get('batch_repos', [])
    all_repos = args.repos or repos_from_config
    if all_repos and len(all_repos) > 1:
        print(f"\n📦 Batch mode: {len(all_repos)} repositories")
        run_batch(all_repos, args, config)
        print("\n✅ Batch complete.")
        return

    # ── Single repo mode ──────────────────────────────────────────────────────
    repo = (all_repos[0] if all_repos else None) or args.repo or config.get('default_repo')
    if not repo:
        print("❌ Error: No repository specified")
        print("   Use --repo owner/repo or set default_repo in config.yaml")
        sys.exit(1)

    print(f"\n📥 Fetching commits from {repo} since {args.since}...")
    vcs = get_vcs_provider(config)
    commits = vcs.fetch_commits(repo, args.since, config, use_sample=args.sample)
    print(f"✓ Found {len(commits)} commits")

    if not commits:
        print("\n⚠️  No commits found in specified date range")
        print("   Try adjusting --since date or check repository access")
        sys.exit(0)

    print(f"\n🤖 Categorizing commits (hybrid: rules → AI fallback)...")
    categories = categorize_commits_hybrid(commits, config, args.prompt, args.rules)
    print("✓ Categorization complete")

    print("\n📝 Generating release notes...")
    notes = generate_release_notes(categories, args.since, repo, config, args.template)

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

    print(f"\n📄 Preview (first 500 characters):")
    print("-" * 50)
    print(notes[:500] + "..." if len(notes) > 500 else notes)
    print("-" * 50)


if __name__ == "__main__":
    main()
