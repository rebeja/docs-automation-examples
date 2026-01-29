# Step 3: Configure APIs

Configure API access for GitHub and your AI provider.

**Time estimate:** 10-15 minutes

## Complete these tasks

- Create and test GitHub API token
- Obtain and configure AI provider API key
- Review security best practices
- Verify API connections

## Get API keys

### 1. GitHub token (required)

Fetch commits and pull requests from repositories with this token.

Free for public repos, included with GitHub account for private repos.

#### Create a GitHub token

1. Navigate to [github.com/settings/tokens](https://github.com/settings/tokens)

2. Click **Generate new token** and choose **Generate new token (classic)**

3. Configure the token:
   
   - **Note:** "Release Notes Automation" (describes purpose)
   - **Expiration:** Choose based on your security policy (90 days recommended)
   - **Scopes:** Select the minimum needed:
     - For public repos only: `public_repo`
     - For private repos: `repo` (full control)

4. Click **Generate token** and copy it immediately. The token format is `ghp_xxxxxxxxxxxxxxxxxxxx`.

Store the token in your password manager immediately. You cannot view it again after leaving the page.

### 2. AI provider API key (required)

Choose one provider:

#### Option A: Anthropic (Claude) - Recommended

Claude excels at following detailed instructions and explaining reasoning.

Get an Anthropic API key:

1. Go to [console.anthropic.com](https://console.anthropic.com/)
2. Sign up or log in
3. Click **Get API Keys** in the navigation
4. Click **Create Key**
5. Name it "Release Notes Automation"
6. Copy the key (starts with `sk-ant-`)

Pay-as-you-go pricing: approximately $0.01-0.03 per release notes generation

Free tier: $5 credit for new accounts

#### Option B: OpenAI (GPT)

GPT offers wide availability, fast performance, and good general capabilities.

Get an OpenAI API key:

1. Go to [platform.openai.com](https://platform.openai.com/)
2. Sign up or log in
3. Click your profile then **View API Keys**
4. Click **Create new secret key**
5. Name it "Release Notes Automation"
6. Copy the key (starts with `sk-`)

Pay-as-you-go pricing: approximately $0.02-0.05 per release notes generation

Free tier: $5 credit for new accounts (first 3 months)

## Configure your keys

### 1. Open configuration file

Edit `config.yaml` in the repository root:

```bash
# Navigate to repository root
cd /path/to/docs-automation-examples
```

Open in your text editor:

```bash
# VS Code
code config.yaml

# Cursor
cursor config.yaml

# Nano (terminal)
nano config.yaml
```

### 2. Add your keys

For Anthropic (Claude):

```yaml
# AI Provider
ai_provider: "anthropic"
ai_api_key: "sk-ant-your-actual-key-here"
model: "claude-3-sonnet-20240229"

# GitHub
github_token: "ghp_your-actual-token-here"

# Optional: Set a default repository
default_repo: "your-username/your-repo"
output_file: "release_notes.md"
```

For OpenAI (GPT):

```yaml
# AI Provider
ai_provider: "openai"
ai_api_key: "sk-your-actual-key-here"
model: "gpt-4"

# GitHub
github_token: "ghp_your-actual-token-here"

# Optional: Set a default repository
default_repo: "your-username/your-repo"
output_file: "release_notes.md"
```

### 3. Save the file

Save and close your editor.

The `config.yaml` file is in `.gitignore` to prevent accidental commits. Never commit this file. Verify it does not appear in git status:

```bash
git status
# config.yaml should not appear as modified
```

## Test your configuration

### Test 1: Configuration file loads

```bash
cd 01-release-notes-automation
python -c "import yaml; config = yaml.safe_load(open('../config.yaml')); print('Configuration loaded')"
```

The output shows `Configuration loaded`.

### Test 2: GitHub API access

```bash
python -c "
from github import Github
import yaml
config = yaml.safe_load(open('../config.yaml'))
g = Github(config['github_token'])
user = g.get_user()
print(f'GitHub API working. Connected as: {user.login}')
"
```

The output shows `GitHub API working. Connected as: your-username`.

### Test 3: AI API access

Test Anthropic:

```bash
python -c "
import anthropic
import yaml
config = yaml.safe_load(open('../config.yaml'))
client = anthropic.Anthropic(api_key=config['ai_api_key'])
message = client.messages.create(
    model='claude-3-sonnet-20240229',
    max_tokens=10,
    messages=[{'role': 'user', 'content': 'Say hello'}]
)
print('Anthropic API working')
print(f'Response: {message.content[0].text}')
"
```

Test OpenAI:

```bash
python -c "
from openai import OpenAI
import yaml
config = yaml.safe_load(open('../config.yaml'))
client = OpenAI(api_key=config['ai_api_key'])
response = client.chat.completions.create(
    model='gpt-4',
    messages=[{'role': 'user', 'content': 'Say hello'}],
    max_tokens=10
)
print('OpenAI API working')
print(f'Response: {response.choices[0].message.content}')
"
```

The output shows a success message with a response.

## Follow security best practices

### Do these actions

- Use environment variables for production:
  ```bash
  export GITHUB_TOKEN="your-token"
  export AI_API_KEY="your-key"
  ```

- Add config.yaml to .gitignore (already done)

- Rotate keys regularly (every 90 days)

- Use minimal scopes (only `public_repo` when possible)

- Store in password manager for backup

### Avoid these actions

- Never commit `config.yaml` with real keys
- Share API keys in Slack or email
- Use production tokens for testing
- Hardcode keys in scripts
- Push to public repositories with keys

## Troubleshooting

### Invalid GitHub token

Error: `401 Unauthorized` or `Bad credentials`

Solutions:

1. Verify token is copied correctly (no extra spaces)
2. Check token has not expired
3. Verify required scopes are enabled
4. Try regenerating the token

### Invalid AI API key

Error: `Invalid API key` or `Authentication failed`

Solutions:

1. Verify key is copied correctly
2. Check you are using the right provider (`anthropic` versus `openai`)
3. Verify billing is set up (after free tier)
4. Check API key is active in provider console

### Configuration file not found

Error: `FileNotFoundError: config.yaml`

Solutions:

1. Verify you are in the right directory
2. Check the file exists: `ls -la config.yaml`
3. Verify you copied from `config.example.yaml`

### Module import errors

Error: `ModuleNotFoundError: No module named 'anthropic'`

Solutions:

1. Activate virtual environment: `source venv/bin/activate`
2. Reinstall dependencies: `pip install -r requirements.txt`
3. Verify Python version: `python --version` (3.8+)

## Summary

You created a GitHub API token with appropriate scopes, obtained an AI provider API key, configured both keys securely, verified API connections work, and reviewed security best practices.

## Next step

Run your first automation with APIs configured.

[Next: Step 4 - First run](step-4-run-first-time.md)

---

Estimated cost per run: GitHub API is free (rate limited to 5,000 requests per hour), AI API costs $0.01-0.05 per release notes generation. For typical biweekly releases: approximately $0.50-1.00 per month.
