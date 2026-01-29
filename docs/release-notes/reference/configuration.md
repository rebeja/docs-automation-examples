# Configuration reference

Complete reference for `config.yaml` configuration file.

## File location

Place the `config.yaml` file in the repository root:

```
docs-automation-examples/
├── config.yaml              # Your configuration
├── config.example.yaml      # Template to copy from
├── 01-release-notes-automation/
└── ...
```

## Complete configuration example

```yaml
# AI Provider Configuration
ai_provider: "anthropic"
ai_api_key: "sk-ant-your-key-here"
model: "claude-3-sonnet-20240229"

# GitHub Configuration
github_token: "ghp_your-token-here"

# Optional: Default Settings
default_repo: "owner/repo-name"
output_file: "release_notes.md"
date_format: "%Y-%m-%d"

# Optional: Behavior Settings
max_commits: 100
include_merge_commits: false
verbose: false
```

## Required fields

### `ai_provider`

Type: String  
Required: Yes  
Options: `"anthropic"` or `"openai"`

Specifies which AI provider to use.

```yaml
# Use Anthropic Claude
ai_provider: "anthropic"

# Use OpenAI GPT
ai_provider: "openai"
```

Choose a provider:

| Provider | Best For | Model Options |
|----------|---------|---------------|
| Anthropic | Following detailed instructions, explanations | claude-3-sonnet, claude-3-opus |
| OpenAI | Speed, availability | gpt-4, gpt-3.5-turbo |

### `ai_api_key`

Type: String  
Required: Yes  
Format: Depends on provider

Your AI provider API key.

```yaml
# Anthropic key format
ai_api_key: "sk-ant-api03-xxxxx..."

# OpenAI key format
ai_api_key: "sk-xxxxx..."
```

Security:

- Never commit this file with real keys
- Already in `.gitignore`
- Use environment variables for production

Get keys:

- Anthropic: [console.anthropic.com](https://console.anthropic.com/)
- OpenAI: [platform.openai.com](https://platform.openai.com/)

### `model`

Type: String  
Required: Yes  
Format: Provider-specific model identifier

The specific AI model to use.

Anthropic models:

```yaml
# Recommended: Good balance of quality and cost
model: "claude-3-sonnet-20240229"

# Higher quality, higher cost
model: "claude-3-opus-20240229"

# Faster, lower cost (if available)
model: "claude-3-haiku-20240229"
```

OpenAI models:

```yaml
# Recommended: Most capable
model: "gpt-4"

# Specific versions
model: "gpt-4-turbo-preview"

# Faster, cheaper
model: "gpt-3.5-turbo"
```

Cost comparison (approximate):

| Model | Cost per Run | Quality |
|-------|-------------|---------|
| claude-3-opus | $0.05 | Excellent |
| claude-3-sonnet | $0.02 | Very Good |
| gpt-4 | $0.03 | Excellent |
| gpt-3.5-turbo | $0.01 | Good |

### `github_token`

Type: String  
Required: Yes  
Format: GitHub personal access token

Your GitHub API token for accessing repositories.

```yaml
github_token: "ghp_xxxxxxxxxxxxxxxxxxxx"
```

Required scopes:

For public repositories:
```
public_repo
```

For private repositories:
```
repo (full control)
```

Create a token:

1. Go to [github.com/settings/tokens](https://github.com/settings/tokens)
2. Click "Generate new token (classic)"
3. Select appropriate scopes
4. Copy token immediately

Security:

- Treat like a password
- Set expiration (90 days recommended)
- Rotate regularly
- Do not share in Slack or email

## Optional fields

### `default_repo`

Type: String  
Required: No  
Format: `owner/repo-name`

Default repository if not specified via command line.

```yaml
default_repo: "octocat/Hello-World"
```

Usage:

```bash
# With default_repo set
python generate_release_notes.py --since 2024-01-01

# Overriding default
python generate_release_notes.py --repo other/repo --since 2024-01-01
```

### `output_file`

Type: String  
Required: No  
Default: `"release_notes.md"`

Default filename for generated release notes.

```yaml
output_file: "RELEASE_NOTES.md"
```

Override with:

```bash
python generate_release_notes.py \
  --repo owner/repo \
  --since 2024-01-01 \
  --output custom-notes.md
```

### `date_format`

Type: String  
Required: No  
Default: `"%Y-%m-%d"`
Format: Python strftime format

Formats dates in output.

```yaml
# ISO format (default)
date_format: "%Y-%m-%d"
# Output: 2024-01-28

# US format
date_format: "%m/%d/%Y"
# Output: 01/28/2024

# Full date
date_format: "%B %d, %Y"
# Output: January 28, 2024
```

### `max_commits`

Type: Integer  
Required: No  
Default: No limit

Maximum number of commits to process.

```yaml
max_commits: 100
```

Use cases:

- Testing with smaller datasets
- Rate limit management
- Performance optimization

### `include_merge_commits`

Type: Boolean  
Required: No  
Default: `false`

Include merge commits in categorization.

```yaml
# Exclude merge commits (recommended)
include_merge_commits: false

# Include merge commits
include_merge_commits: true
```

Most merge commits should be filtered by prompt exclusion rules.

### `verbose`

Type: Boolean  
Required: No  
Default: `false`

Enable detailed logging.

```yaml
verbose: true
```

Output with verbose:

```
[DEBUG] Loading configuration from ../config.yaml
[DEBUG] Connecting to GitHub API
[DEBUG] Fetching commits from owner/repo
[DEBUG] Found 23 commits
[DEBUG] Filtering commits...
[DEBUG] Categorizing with AI...
[INFO] Release notes written to release_notes.md
```

## Environment variables

Use as alternative to `config.yaml` for production:

```bash
# AI Provider
export AI_PROVIDER="anthropic"
export AI_API_KEY="sk-ant-..."
export AI_MODEL="claude-3-sonnet-20240229"

# GitHub
export GITHUB_TOKEN="ghp_..."

# Run script
python generate_release_notes.py --repo owner/repo --since 2024-01-01
```

Priority:

1. Command line arguments (highest)
2. Environment variables
3. `config.yaml` file (lowest)

## Configuration validation

### Check configuration

Test configuration validity:

```bash
python -c "
import yaml
config = yaml.safe_load(open('config.yaml'))
required = ['ai_provider', 'ai_api_key', 'model', 'github_token']
missing = [f for f in required if f not in config]
if missing:
    print(f'Missing: {missing}')
else:
    print('All required fields present')
"
```

### Test API connections

Verify API keys work:

```bash
cd 01-release-notes-automation
python -c "
from github import Github
import yaml
config = yaml.safe_load(open('../config.yaml'))
g = Github(config['github_token'])
user = g.get_user()
print(f'GitHub: Connected as {user.login}')

import anthropic
client = anthropic.Anthropic(api_key=config['ai_api_key'])
message = client.messages.create(
    model=config['model'],
    max_tokens=10,
    messages=[{'role': 'user', 'content': 'Hi'}]
)
print('AI Provider: Connected')
"
```

## Multiple configurations

Maintain different configurations:

```bash
# Development
config.dev.yaml

# Production
config.prod.yaml

# Testing
config.test.yaml
```

Use with:

```bash
python generate_release_notes.py \
  --config ../config.prod.yaml \
  --repo owner/repo \
  --since 2024-01-01
```

## Security best practices

Follow these practices:

- Keep `config.yaml` in `.gitignore`
- Use environment variables for CI or CD
- Rotate keys every 90 days
- Use minimal GitHub token scopes
- Set token expiration dates

Avoid these practices:

- Commit `config.yaml` with real keys
- Share keys via Slack or email
- Use production keys for testing
- Grant unnecessary permissions
- Store keys in plaintext elsewhere

## Troubleshooting configuration

### Configuration file not found

```bash
# Check location
ls -la config.yaml

# Create from example
cp config.example.yaml config.yaml
```

### Invalid YAML syntax

Problem: `yaml.scanner.ScannerError`

Solution: Validate YAML:

```bash
python -c "import yaml; yaml.safe_load(open('config.yaml'))"
```

Common issues:

- Missing quotes around values with special characters
- Incorrect indentation (use spaces, not tabs)
- Unescaped characters in strings

### API keys not working

See [Troubleshooting guide](../troubleshooting.md#configuration-issues).

---

Next: [Prompt engineering](prompt-engineering.md)
