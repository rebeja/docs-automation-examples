#!/usr/bin/env python3
"""
README generator using AI to produce documentation from a code repository.
Accepts a local directory path or a GitHub repository (owner/repo).

From the Doc360Talk webinar: "From Writer to Tool Builder"
Educational example demonstrating AI-assisted documentation automation.
"""

import os
import sys
import argparse
import json
import re
import yaml
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional

# ─── Optional dependency detection ───────────────────────────────────────────

try:
    from github import Github, GithubException
    HAS_GITHUB = True
except ImportError:
    HAS_GITHUB = False

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
    print("   or:  pip install openai      (for GPT)")
    sys.exit(1)

# ─── Language detection ───────────────────────────────────────────────────────

EXTENSION_TO_LANGUAGE = {
    '.py': 'Python', '.js': 'JavaScript', '.ts': 'TypeScript',
    '.jsx': 'JavaScript', '.tsx': 'TypeScript', '.rb': 'Ruby',
    '.go': 'Go', '.rs': 'Rust', '.java': 'Java', '.kt': 'Kotlin',
    '.swift': 'Swift', '.cs': 'C#', '.cpp': 'C++', '.c': 'C',
    '.php': 'PHP', '.sh': 'Shell', '.bash': 'Shell',
    '.r': 'R', '.scala': 'Scala', '.ex': 'Elixir', '.exs': 'Elixir',
}

ENTRY_POINT_NAMES = {
    'main.py', 'app.py', 'cli.py', 'run.py', 'server.py',
    'index.js', 'index.ts', 'app.js', 'server.js',
    'main.go', 'main.rs', 'main.rb', 'main.java',
    'index.html', '__main__.py',
}

DEPENDENCY_FILES = {
    'requirements.txt', 'requirements.in', 'Pipfile', 'pyproject.toml',
    'setup.py', 'setup.cfg', 'package.json', 'yarn.lock', 'Cargo.toml',
    'go.mod', 'Gemfile', 'pom.xml', 'build.gradle', 'composer.json',
    'mix.exs',
}

DEFAULT_README_TEMPLATE = """\
{{ description_section }}

{{ installation_section }}

{{ usage_section }}

{{ contributing_section }}

---

_This README was generated with AI assistance. Review for accuracy before publishing._
"""

# ─── AI Provider classes ──────────────────────────────────────────────────────

class AnthropicProvider:
    def __init__(self, config: Dict):
        if not HAS_ANTHROPIC:
            print("❌ Error: Anthropic library not installed. Run: pip install anthropic")
            sys.exit(1)
        self.config = config

    def generate(self, prompt: str) -> str:
        client = _anthropic.Anthropic(api_key=self.config['ai_api_key'])
        message = client.messages.create(
            model=self.config['model'],
            max_tokens=2000,
            temperature=0.4,
            messages=[{"role": "user", "content": prompt}]
        )
        return message.content[0].text


class OpenAIProvider:
    def __init__(self, config: Dict):
        if not HAS_OPENAI:
            print("❌ Error: OpenAI library not installed. Run: pip install openai")
            sys.exit(1)
        self.config = config

    def generate(self, prompt: str) -> str:
        client = _openai.OpenAI(api_key=self.config['ai_api_key'])
        response = client.chat.completions.create(
            model=self.config['model'],
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000,
            temperature=0.4,
        )
        return response.choices[0].message.content


class AzureOpenAIProvider:
    def __init__(self, config: Dict):
        if not HAS_OPENAI:
            print("❌ Error: OpenAI library not installed. Run: pip install openai")
            sys.exit(1)
        self.config = config

    def generate(self, prompt: str) -> str:
        client = _openai.AzureOpenAI(
            api_key=self.config['ai_api_key'],
            azure_endpoint=self.config['azure_endpoint'],
            api_version=self.config.get('azure_api_version', '2024-02-01'),
        )
        response = client.chat.completions.create(
            model=self.config['model'],
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000,
            temperature=0.4,
        )
        return response.choices[0].message.content


def get_ai_provider(config: Dict):
    provider = config['ai_provider'].lower()
    if provider == 'anthropic':
        return AnthropicProvider(config)
    elif provider == 'openai':
        return OpenAIProvider(config)
    elif provider == 'azure_openai':
        return AzureOpenAIProvider(config)
    else:
        print(f"❌ Error: Unknown AI provider: {provider}")
        print("   Supported: anthropic, openai, azure_openai")
        sys.exit(1)


# ─── Repository analysis ──────────────────────────────────────────────────────

def detect_language(file_paths: List[str]) -> str:
    """Detect the primary language from a list of file paths."""
    counts: Dict[str, int] = {}
    for path in file_paths:
        ext = Path(path).suffix.lower()
        lang = EXTENSION_TO_LANGUAGE.get(ext)
        if lang:
            counts[lang] = counts.get(lang, 0) + 1
    if not counts:
        return 'Unknown'
    return max(counts, key=lambda k: counts[k])


def parse_dependencies(file_contents: Dict[str, str]) -> List[str]:
    """
    Extract dependency names from common dependency file formats.
    Returns a list of package names (not version-pinned strings).
    """
    deps = []

    if 'requirements.txt' in file_contents:
        for line in file_contents['requirements.txt'].splitlines():
            line = line.strip()
            if line and not line.startswith('#'):
                # Strip version specifiers: requests>=2.0 → requests
                name = re.split(r'[>=<!;\[]', line)[0].strip()
                if name:
                    deps.append(name)

    if 'package.json' in file_contents:
        try:
            pkg = json.loads(file_contents['package.json'])
            deps.extend(pkg.get('dependencies', {}).keys())
            deps.extend(pkg.get('devDependencies', {}).keys())
        except json.JSONDecodeError:
            pass

    if 'Cargo.toml' in file_contents:
        in_deps = False
        for line in file_contents['Cargo.toml'].splitlines():
            if line.strip() in ('[dependencies]', '[dev-dependencies]'):
                in_deps = True
            elif line.strip().startswith('[') and in_deps:
                in_deps = False
            elif in_deps and '=' in line:
                name = line.split('=')[0].strip()
                if name:
                    deps.append(name)

    if 'go.mod' in file_contents:
        in_require = False
        for line in file_contents['go.mod'].splitlines():
            if line.strip() == 'require (': in_require = True
            elif line.strip() == ')': in_require = False
            elif in_require or line.strip().startswith('require '):
                parts = line.strip().lstrip('require').strip().split()
                if parts:
                    deps.append(parts[0].split('/')[-1])

    return list(dict.fromkeys(deps))[:20]  # deduplicate, cap at 20


def detect_project_name(file_contents: Dict[str, str], directory_name: str) -> str:
    """Extract project name from config files, falling back to directory name."""
    if 'package.json' in file_contents:
        try:
            pkg = json.loads(file_contents['package.json'])
            if pkg.get('name'):
                return pkg['name']
        except json.JSONDecodeError:
            pass

    if 'pyproject.toml' in file_contents:
        for line in file_contents['pyproject.toml'].splitlines():
            if line.strip().startswith('name'):
                match = re.search(r'name\s*=\s*["\'](.+?)["\']', line)
                if match:
                    return match.group(1)

    if 'setup.py' in file_contents:
        match = re.search(r'name\s*=\s*["\'](.+?)["\']', file_contents['setup.py'])
        if match:
            return match.group(1)

    if 'Cargo.toml' in file_contents:
        for line in file_contents['Cargo.toml'].splitlines():
            match = re.search(r'^name\s*=\s*"(.+?)"', line)
            if match:
                return match.group(1)

    return directory_name


def detect_license(file_contents: Dict[str, str]) -> str:
    """Detect license type from LICENSE file content."""
    license_text = file_contents.get('LICENSE', file_contents.get('LICENSE.md', ''))
    if not license_text:
        return 'Not specified'

    license_text_lower = license_text.lower()
    if 'mit license' in license_text_lower or 'mit\n' in license_text_lower:
        return 'MIT'
    if 'apache license' in license_text_lower and '2.0' in license_text_lower:
        return 'Apache 2.0'
    if 'gnu general public license' in license_text_lower:
        return 'GPL'
    if 'bsd' in license_text_lower:
        return 'BSD'
    if 'mozilla public license' in license_text_lower:
        return 'MPL 2.0'
    return 'Custom'


def read_local_repo(path: str, max_file_lines: int = 200) -> Dict:
    """
    Scan a local directory and return a repo context dict.
    Reads up to 5 key files (entry points and dependency files).
    """
    repo_path = Path(path).resolve()
    if not repo_path.is_dir():
        print(f"❌ Error: Directory not found: {path}")
        sys.exit(1)

    all_files = [
        str(f.relative_to(repo_path))
        for f in repo_path.rglob('*')
        if f.is_file()
        and not any(part.startswith('.') for part in f.parts[len(repo_path.parts):])
        and '__pycache__' not in str(f)
        and 'node_modules' not in str(f)
    ]
    top_level = [str(f.name) for f in repo_path.iterdir()]

    # Read dependency and key files
    files_to_read = set()
    for fname in all_files:
        if Path(fname).name in DEPENDENCY_FILES:
            files_to_read.add(fname)
        if Path(fname).name.lower() in {'license', 'license.md', 'license.txt'}:
            files_to_read.add(fname)
        if Path(fname).name.lower() in {'readme.md', 'readme.rst', 'readme.txt', 'readme'}:
            files_to_read.add(fname)

    # Add up to 3 entry points
    entry_points_found = []
    for fname in all_files:
        if Path(fname).name.lower() in ENTRY_POINT_NAMES and len(entry_points_found) < 3:
            files_to_read.add(fname)
            entry_points_found.append(fname)

    file_contents: Dict[str, str] = {}
    for rel_path in files_to_read:
        abs_path = repo_path / rel_path
        try:
            lines = abs_path.read_text(encoding='utf-8', errors='ignore').splitlines()
            file_contents[Path(rel_path).name] = '\n'.join(lines[:max_file_lines])
        except Exception:
            pass

    return {
        'name': detect_project_name(file_contents, repo_path.name),
        'language': detect_language(all_files),
        'dependencies': parse_dependencies(file_contents),
        'entry_points': entry_points_found,
        'license': detect_license(file_contents),
        'existing_readme': file_contents.get('README.md', file_contents.get('README.rst', '')),
        'file_tree': sorted(top_level)[:30],
        'key_files': {k: v for k, v in file_contents.items()
                      if k not in {'README.md', 'README.rst', 'LICENSE'}},
    }


def read_github_repo(repo_slug: str, config: Dict, max_file_lines: int = 200) -> Dict:
    """Fetch repo metadata and key file contents from GitHub."""
    if not HAS_GITHUB:
        print("❌ Error: PyGithub not installed. Run: pip install PyGithub")
        sys.exit(1)

    token = config.get('github_token', '')
    if not token or token == 'YOUR_GITHUB_TOKEN_HERE':
        print("❌ Error: Missing github_token in config")
        sys.exit(1)

    try:
        g = Github(token)
        repo = g.get_repo(repo_slug)
        contents = repo.get_contents("")
        all_files = [c.path for c in contents if c.type == 'file']

        file_contents: Dict[str, str] = {}
        files_to_fetch = set()
        entry_points_found = []

        for path in all_files:
            name = Path(path).name
            if name in DEPENDENCY_FILES:
                files_to_fetch.add(path)
            if name.lower() in {'license', 'license.md', 'readme.md', 'readme.rst'}:
                files_to_fetch.add(path)
            if name.lower() in ENTRY_POINT_NAMES and len(entry_points_found) < 3:
                files_to_fetch.add(path)
                entry_points_found.append(path)

        for path in files_to_fetch:
            try:
                content = repo.get_contents(path)
                text = content.decoded_content.decode('utf-8', errors='ignore')
                lines = text.splitlines()
                file_contents[Path(path).name] = '\n'.join(lines[:max_file_lines])
            except Exception:
                pass

        return {
            'name': repo.name,
            'language': repo.language or detect_language(all_files),
            'dependencies': parse_dependencies(file_contents),
            'entry_points': entry_points_found,
            'license': repo.get_license().license.name if repo.get_license() else detect_license(file_contents),
            'existing_readme': file_contents.get('README.md', ''),
            'file_tree': sorted([c.path for c in contents])[:30],
            'key_files': {k: v for k, v in file_contents.items()
                          if k not in {'README.md', 'LICENSE'}},
        }
    except GithubException as e:
        print(f"❌ GitHub API Error: {e.data.get('message', str(e))}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error reading GitHub repo: {e}")
        sys.exit(1)


def get_sample_repo_context() -> Dict:
    """Return a built-in sample repo context for testing without API calls."""
    sample_dir = Path(__file__).parent / 'examples' / 'sample_project'
    if sample_dir.exists():
        return read_local_repo(str(sample_dir))
    # Fallback inline context if sample_project directory is missing
    return {
        'name': 'taskflow',
        'language': 'Python',
        'dependencies': ['click', 'rich', 'pyyaml', 'requests'],
        'entry_points': ['main.py'],
        'license': 'MIT',
        'existing_readme': '',
        'file_tree': ['main.py', 'requirements.txt', 'LICENSE', 'tests/', 'taskflow/'],
        'key_files': {
            'main.py': (
                '#!/usr/bin/env python3\n'
                '"""TaskFlow CLI — manage tasks from the command line."""\n\n'
                'import click\n'
                'from taskflow import TaskManager\n\n'
                '@click.group()\n'
                'def cli():\n'
                '    """TaskFlow: a lightweight task manager."""\n'
                '    pass\n\n'
                '@cli.command()\n'
                '@click.argument("title")\n'
                'def add(title):\n'
                '    """Add a new task."""\n'
                '    tm = TaskManager()\n'
                '    tm.add(title)\n'
                '    click.echo(f"✓ Added: {title}")\n'
            ),
            'requirements.txt': 'click>=8.0\nrich>=13.0\npyyaml>=6.0\nrequests>=2.28\n',
        },
    }


def analyze_repo(input_arg: str, config: Dict, use_sample: bool = False) -> Dict:
    """
    Analyze a repository and return a context dict for README generation.
    Auto-detects local path vs. GitHub repo from the input argument.
    """
    if use_sample:
        print("Using sample project (no API calls)")
        return get_sample_repo_context()

    is_github = re.match(r'^[\w.-]+/[\w.-]+$', input_arg) or input_arg.startswith('http')
    if is_github:
        slug = input_arg.replace('https://github.com/', '').rstrip('/')
        return read_github_repo(slug, config, config.get('readme_max_file_lines', 200))
    else:
        return read_local_repo(input_arg, config.get('readme_max_file_lines', 200))


# ─── Section generation ───────────────────────────────────────────────────────

def build_context_summary(repo_context: Dict) -> str:
    """Format repo context into a readable summary for inclusion in prompts."""
    lines = [
        f"Project name: {repo_context['name']}",
        f"Primary language: {repo_context['language']}",
        f"License: {repo_context['license']}",
    ]
    if repo_context['dependencies']:
        lines.append(f"Dependencies: {', '.join(repo_context['dependencies'][:10])}")
    if repo_context['entry_points']:
        lines.append(f"Entry points: {', '.join(repo_context['entry_points'])}")
    lines.append(f"\nTop-level files/directories:\n{chr(10).join(repo_context['file_tree'][:15])}")

    for filename, content in list(repo_context['key_files'].items())[:3]:
        lines.append(f"\n--- {filename} ---\n{content[:1500]}")

    if repo_context.get('existing_readme'):
        lines.append(f"\n--- Existing README (for context) ---\n{repo_context['existing_readme'][:1000]}")

    return '\n'.join(lines)


def load_prompt(prompt_path: str) -> str:
    """Load a prompt template from file."""
    if not os.path.exists(prompt_path):
        print(f"❌ Error: Prompt file not found: {prompt_path}")
        print("   Make sure you're running from the 03-readme-generator/ directory")
        sys.exit(1)
    with open(prompt_path) as f:
        return f.read()


def generate_section(
    section_name: str,
    repo_context: Dict,
    config: Dict,
    prompts_dir: str = "prompts",
) -> str:
    """
    Generate one README section using AI.
    Loads the section-specific prompt, injects repo context, calls the AI provider.
    """
    prompt_path = os.path.join(prompts_dir, f"{section_name}_prompt.txt")
    prompt_template = load_prompt(prompt_path)
    context_summary = build_context_summary(repo_context)
    full_prompt = prompt_template.replace("{REPO_CONTEXT}", context_summary)

    try:
        provider = get_ai_provider(config)
        return provider.generate(full_prompt)
    except SystemExit:
        raise
    except Exception as e:
        print(f"⚠️  Failed to generate {section_name} section: {e}")
        return f"## {section_name.title()}\n\n_Section generation failed. Please write this section manually._\n"


# ─── README assembly ──────────────────────────────────────────────────────────

def assemble_readme(sections: Dict[str, str], repo_context: Dict, template_path: Optional[str] = None) -> str:
    """Combine generated sections into a complete README using a Jinja2 template."""
    template_vars = {
        **{f"{name}_section": content for name, content in sections.items()},
        "project_name": repo_context['name'],
        "language": repo_context['language'],
        "license": repo_context['license'],
        "date": datetime.now().strftime('%Y-%m-%d'),
    }

    if HAS_JINJA2:
        if template_path and os.path.exists(template_path):
            env = Environment(
                loader=FileSystemLoader(str(Path(template_path).parent)),
                trim_blocks=True, lstrip_blocks=True
            )
            template = env.get_template(Path(template_path).name)
        else:
            env = Environment(loader=BaseLoader(), trim_blocks=True, lstrip_blocks=True)
            template = env.from_string(DEFAULT_README_TEMPLATE)
        return template.render(**template_vars)

    # Fallback without jinja2
    parts = [sections[name] for name in sections if sections[name]]
    parts.append("\n---\n\n_This README was generated with AI assistance. Review for accuracy before publishing._\n")
    return "\n\n".join(parts)


# ─── Config ───────────────────────────────────────────────────────────────────

def load_config(config_path: str = "../config.yaml") -> Dict:
    """Load configuration with environment variable overrides."""
    config = {}
    if os.path.exists(config_path):
        with open(config_path) as f:
            config = yaml.safe_load(f) or {}

    env_map = {
        'AI_PROVIDER': 'ai_provider',
        'AI_API_KEY': 'ai_api_key',
        'AI_MODEL': 'model',
        'GITHUB_TOKEN': 'github_token',
    }
    for env_var, config_key in env_map.items():
        if os.getenv(env_var):
            config[config_key] = os.getenv(env_var)

    placeholder_values = {'YOUR_API_KEY_HERE', 'YOUR_GITHUB_TOKEN_HERE'}
    required = ['ai_provider', 'ai_api_key', 'model']
    missing = [f for f in required if not config.get(f) or config[f] in placeholder_values]
    if missing:
        print(f"❌ Error: Missing configuration: {', '.join(missing)}")
        print(f"   Update {config_path} or set environment variables")
        sys.exit(1)

    return config


# ─── Entry point ──────────────────────────────────────────────────────────────

ALL_SECTIONS = ['description', 'installation', 'usage', 'contributing']


def main():
    parser = argparse.ArgumentParser(
        description='Generate a README from a code repository using AI',
        epilog='Examples:\n'
               '  python readme_generator.py --sample\n'
               '  python readme_generator.py --input ./my-project\n'
               '  python readme_generator.py --input owner/repo\n',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('--input', help='Local directory path or GitHub owner/repo')
    parser.add_argument('--output', default='README.md', help='Output file (default: README.md)')
    parser.add_argument('--config', default='../config.yaml', help='Config file path')
    parser.add_argument('--prompts', default='prompts', help='Prompts directory')
    parser.add_argument('--template', default=None, help='Custom Jinja2 template (.j2)')
    parser.add_argument('--sections', default=','.join(ALL_SECTIONS),
                        help=f'Comma-separated sections to generate (default: all). '
                             f'Options: {", ".join(ALL_SECTIONS)}')
    parser.add_argument('--analyze', action='store_true',
                        help='Print repo analysis only, do not generate README')
    parser.add_argument('--sample', action='store_true',
                        help='Use built-in sample project (no API calls needed)')

    args = parser.parse_args()

    if not args.sample and not args.input:
        print("❌ Error: Provide --input or use --sample")
        parser.print_help()
        sys.exit(1)

    print("📄 README Generator")
    print("=" * 50)

    config = load_config(args.config)

    # Step 1: Analyze repo
    source = "sample project" if args.sample else args.input
    print(f"\n🔍 Analyzing {source}...")
    repo_context = analyze_repo(args.input or '', config, use_sample=args.sample)

    print(f"✓ Project: {repo_context['name']}")
    print(f"✓ Language: {repo_context['language']}")
    print(f"✓ License: {repo_context['license']}")
    if repo_context['dependencies']:
        print(f"✓ Dependencies: {', '.join(repo_context['dependencies'][:5])}"
              + (f" (+{len(repo_context['dependencies'])-5} more)" if len(repo_context['dependencies']) > 5 else ""))
    if repo_context['entry_points']:
        print(f"✓ Entry points: {', '.join(repo_context['entry_points'])}")

    if args.analyze:
        print("\n📋 Full repo context:")
        print("-" * 50)
        print(build_context_summary(repo_context))
        return

    # Step 2: Generate sections
    sections_to_generate = [s.strip() for s in args.sections.split(',') if s.strip() in ALL_SECTIONS]
    unknown = [s.strip() for s in args.sections.split(',') if s.strip() not in ALL_SECTIONS]
    if unknown:
        print(f"⚠️  Unknown sections ignored: {', '.join(unknown)}")

    sections: Dict[str, str] = {}
    for section in ALL_SECTIONS:
        if section in sections_to_generate:
            print(f"\n✍️  Generating {section} section...")
            sections[section] = generate_section(section, repo_context, config, args.prompts)
            print(f"✓ {section.title()} section complete")
        else:
            sections[section] = ''

    # Step 3: Assemble and write
    print("\n📝 Assembling README...")
    readme = assemble_readme(sections, repo_context, args.template)

    with open(args.output, 'w') as f:
        f.write(readme)

    print(f"✓ README written to {args.output}")
    print("\n" + "=" * 50)
    print("✅ Done! Review the output before publishing.")
    print("\n💡 Next steps:")
    print(f"   1. Review {args.output} for accuracy")
    print("   2. Add real code examples and screenshots")
    print("   3. Verify all installation steps work")
    print("   4. Add badges (CI status, version, license)")

    print(f"\n📄 Preview (first 400 characters):")
    print("-" * 50)
    print(readme[:400] + "..." if len(readme) > 400 else readme)
    print("-" * 50)


if __name__ == "__main__":
    main()
