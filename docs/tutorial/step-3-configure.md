# Step 3: Configure APIs

Now that your environment is set up and process is documented, you'll configure API access for GitHub and your AI provider.

!!! info "Time Estimate"
    10-15 minutes

## What You'll Accomplish

By the end of this step:

- ✅ GitHub API token created and tested
- ✅ AI provider API key obtained and configured
- ✅ Security best practices understood
- ✅ API connections verified

## API Keys You'll Need

### 1. GitHub Token (Required)

**Purpose:** Fetch commits and pull requests from repositories

**Cost:** Free for public repos, included with GitHub account for private repos

#### Creating a GitHub Token

1. **Go to GitHub Settings**
   
   Navigate to [github.com/settings/tokens](https://github.com/settings/tokens)

2. **Click "Generate new token"**
   
   Choose **"Generate new token (classic)"**

3. **Configure Token**
   
   - **Note:** "Release Notes Automation" (describes purpose)
   - **Expiration:** Choose based on your security policy (90 days recommended)
   - **Scopes:** Select the minimum needed:
     - For public repos only: ✅ `public_repo`
     - For private repos: ✅ `repo` (full control)

4. **Generate and Copy**
   
   Click "Generate token" and **copy it immediately** - you won't see it again!
   
   Format: `ghp_xxxxxxxxxxxxxxxxxxxx`

!!! warning "Save Your Token"
    Store the token in your password manager immediately. If you lose it, you'll need to generate a new one.

### 2. AI Provider API Key (Required)

Choose **one** of these providers:

=== "Anthropic (Claude)"
    **Recommended for this tutorial**

    **Why Claude?** Excellent at following detailed instructions and explaining reasoning

    #### Getting an Anthropic API Key

    1. Go to [console.anthropic.com](https://console.anthropic.com/)
    2. Sign up or log in
    3. Click "Get API Keys" in the navigation
    4. Click "Create Key"
    5. Give it a name: "Release Notes Automation"
    6. Copy the key (starts with `sk-ant-`)

    **Pricing:** Pay-as-you-go, ~$0.01-0.03 per release notes generation
    
    **Free tier:** $5 credit for new accounts

=== "OpenAI (GPT)"
    **Alternative option**

    **Why GPT?** Widely available, fast, good general performance

    #### Getting an OpenAI API Key

    1. Go to [platform.openai.com](https://platform.openai.com/)
    2. Sign up or log in
    3. Click your profile → "View API Keys"
    4. Click "Create new secret key"
    5. Give it a name: "Release Notes Automation"
    6. Copy the key (starts with `sk-`)

    **Pricing:** Pay-as-you-go, ~$0.02-0.05 per release notes generation
    
    **Free tier:** $5 credit for new accounts (first 3 months)

## Configuring Your Keys

### 1. Open Configuration File

Edit `config.yaml` in the repository root:

```bash
# Navigate to repository root if not already there
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

### 2. Add Your Keys

=== "Using Anthropic (Claude)"
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

=== "Using OpenAI (GPT)"
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

### 3. Save the File

Save and close your editor.

!!! danger "Never Commit This File"
    The `config.yaml` file is in `.gitignore` to prevent accidental commits. Double-check:
    
    ```bash
    git status
    # Should NOT show config.yaml as modified
    ```

## Testing Your Configuration

### Test 1: Configuration File Loads

```bash
cd 01-release-notes-automation
python -c "import yaml; config = yaml.safe_load(open('../config.yaml')); print('✓ Configuration loaded')"
```

**Expected:** `✓ Configuration loaded`

### Test 2: GitHub API Access

Test GitHub connection:

```bash
python -c "
from github import Github
import yaml
config = yaml.safe_load(open('../config.yaml'))
g = Github(config['github_token'])
user = g.get_user()
print(f'✓ GitHub API working. Connected as: {user.login}')
"
```

**Expected:** `✓ GitHub API working. Connected as: your-username`

### Test 3: AI API Access

=== "Test Anthropic"
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
    print('✓ Anthropic API working')
    print(f'Response: {message.content[0].text}')
    "
    ```

=== "Test OpenAI"
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
    print('✓ OpenAI API working')
    print(f'Response: {response.choices[0].message.content}')
    "
    ```

**Expected:** Success message with a response

## Security Best Practices

### DO ✅

- **Use environment variables** for production:
  ```bash
  export GITHUB_TOKEN="your-token"
  export AI_API_KEY="your-key"
  ```

- **Add config.yaml to .gitignore** (already done)

- **Rotate keys regularly** (every 90 days)

- **Use minimal scopes** (only `public_repo` if possible)

- **Store in password manager** for backup

### DON'T ❌

- **Never commit** `config.yaml` with real keys
- **Don't share** API keys in Slack/email
- **Don't use** production tokens for testing
- **Don't hardcode** keys in scripts
- **Don't push** to public repositories with keys

## Troubleshooting

### Invalid GitHub Token

**Error:** `401 Unauthorized` or `Bad credentials`

**Solutions:**

1. Verify token is copied correctly (no extra spaces)
2. Check token hasn't expired
3. Verify required scopes are enabled
4. Try regenerating the token

### Invalid AI API Key

**Error:** `Invalid API key` or `Authentication failed`

**Solutions:**

1. Verify key is copied correctly
2. Check you're using the right provider (`anthropic` vs `openai`)
3. Verify billing is set up (after free tier)
4. Check API key is active in provider console

### Configuration File Not Found

**Error:** `FileNotFoundError: config.yaml`

**Solutions:**

1. Verify you're in the right directory
2. Check the file exists: `ls -la config.yaml`
3. Verify you copied from `config.example.yaml`

### Module Import Errors

**Error:** `ModuleNotFoundError: No module named 'anthropic'`

**Solutions:**

1. Activate virtual environment: `source venv/bin/activate`
2. Reinstall dependencies: `pip install -r requirements.txt`
3. Verify Python version: `python --version` (3.8+)

## What You've Learned

In this step, you:

- ✅ Created GitHub API token with appropriate scopes
- ✅ Obtained AI provider API key
- ✅ Configured both keys securely
- ✅ Verified API connections work
- ✅ Learned security best practices

## Next Step

With APIs configured, you're ready to run your first automation!

[Next: Step 4 - First Run →](step-4-run-first-time.md){ .md-button .md-button--primary }

---

!!! tip "API Costs"
    **Estimated cost per run:**
    - GitHub API: Free (rate limited to 5,000 requests/hour)
    - AI API: $0.01-0.05 per release notes generation
    
    For typical biweekly releases: **~$0.50-1.00 per month**
