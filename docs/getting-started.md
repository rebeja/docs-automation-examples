# Getting Started

This guide will help you set up your environment and run the release notes automation for the first time.

## Prerequisites

Before starting, make sure you have:

### Required

- [x] **Python 3.8 or higher** - Check with `python --version` or `python3 --version`
- [x] **Git installed** - Check with `git --version`
- [x] **GitHub account** - For API access (or GitLab/Bitbucket equivalent)
- [x] **AI API access** - Anthropic (Claude) or OpenAI account
- [x] **Command line comfort** - Ability to run terminal commands
- [x] **Text editor** - VS Code, Cursor, Sublime Text, or similar

### Nice to Have

- [ ] **Cursor or AI coding tool** - For asking questions and iterating
- [ ] **Existing docs-as-code workflow** - Makes adaptation easier
- [ ] **Write the Docs community membership** - For sharing and learning

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/rebeja/docs-automation-examples.git
cd docs-automation-examples
```

### 2. Create Virtual Environment

Using a virtual environment keeps dependencies isolated:

=== "macOS/Linux"
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

=== "Windows"
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

You should see `(venv)` in your terminal prompt.

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

This installs:

- `anthropic` or `openai` - AI provider SDKs
- `PyGithub` - GitHub API client
- `pyyaml` - Configuration file parsing
- Other utilities

### 4. Verify Installation

```bash
python -c "import anthropic; import github; print('✓ Dependencies installed')"
```

If you see `✓ Dependencies installed`, you're ready!

## Configuration

### 1. Create Configuration File

Copy the example configuration:

```bash
cp config.example.yaml config.yaml
```

!!! warning "Security Note"
    Never commit `config.yaml` with real API keys. It's already in `.gitignore`.

### 2. Get API Keys

You'll need two types of API keys:

#### AI Provider (Required)

Choose **either** Anthropic or OpenAI:

**Option A: Anthropic (Claude)**

1. Go to [console.anthropic.com](https://console.anthropic.com/)
2. Sign up or log in
3. Navigate to API Keys
4. Create a new key
5. Copy the key (starts with `sk-ant-...`)

**Option B: OpenAI (ChatGPT)**

1. Go to [platform.openai.com](https://platform.openai.com/)
2. Sign up or log in
3. Navigate to API Keys
4. Create a new key
5. Copy the key (starts with `sk-...`)

#### GitHub Token (Required)

1. Go to [github.com/settings/tokens](https://github.com/settings/tokens)
2. Click "Generate new token" → "Generate new token (classic)"
3. Give it a name like "Release Notes Automation"
4. Select scopes:
    - ✅ `repo` (Full control of private repositories)
    - Or just `public_repo` if only accessing public repos
5. Click "Generate token"
6. Copy the token immediately (you won't see it again!)

### 3. Edit Configuration File

Open `config.yaml` in your text editor and add your keys:

```yaml
# AI Provider - Choose ONE
ai_provider: "anthropic"  # or "openai"
ai_api_key: "sk-ant-your-key-here"
model: "claude-3-sonnet-20240229"  # or "gpt-4" for OpenAI

# GitHub
github_token: "ghp_your_token_here"

# Optional: Repository defaults
default_repo: "owner/repo-name"
```

### 4. Test Configuration

```bash
cd 01-release-notes-automation
python generate_release_notes.py --help
```

You should see usage instructions without errors.

## First Run

### Test with Sample Data

The script includes sample data so you can test without API calls:

```bash
cd 01-release-notes-automation
python generate_release_notes.py --repo sample/repo --since 2024-01-01 --sample
```

This generates `release_notes.md` using built-in sample commits.

**Review the output:**

```bash
cat release_notes.md
```

You should see categorized release notes with emoji icons and commit links.

### Run with Real Data

Once comfortable, try with a real repository:

```bash
python generate_release_notes.py --repo YOUR_USERNAME/YOUR_REPO --since 2024-01-01
```

Replace:

- `YOUR_USERNAME` - Your GitHub username or organization
- `YOUR_REPO` - Repository name
- `2024-01-01` - Start date for commits (YYYY-MM-DD format)

**Example:**

```bash
python generate_release_notes.py --repo octocat/Hello-World --since 2024-01-01
```

## What to Expect

### On Success

You'll see output like:

```
Fetching commits from octocat/Hello-World since 2024-01-01...
Found 23 commits
Categorizing commits using AI...
Generating release notes...
Release notes written to release_notes.md
```

Open `release_notes.md` to review the generated draft.

### If Something Goes Wrong

See the [Troubleshooting Guide](troubleshooting.md) for common issues:

- **API key errors** - Check your configuration
- **Rate limit errors** - Wait or upgrade API plan
- **No commits found** - Adjust date range or check repository access
- **Import errors** - Reinstall dependencies

## Understanding the Output

The generated `release_notes.md` looks like:

```markdown
# Release Notes

**Date:** 2024-01-20
**Period:** Since 2024-01-01

## 🎉 New Features

- Add user authentication feature ([abc123](link))

## ✨ Enhancements

- Improve search performance by 50% ([def456](link))

## 🐛 Bug Fixes

- Fix memory leak in parser ([ghi789](link))

## 📝 Documentation

- Update API documentation ([jkl012](link))
```

**This is a draft** - Always review before publishing:

- ✓ Check categorization accuracy
- ✓ Add context for major changes
- ✓ Remove internal-only items that slipped through
- ✓ Adjust wording for your audience
- ✓ Add links to related documentation

## Next Steps

Now that you have the basics working:

1. **[Document your process](tutorial/step-2-document-process.md)** - Write down your manual release notes workflow
2. **[Iterate on prompts](tutorial/step-5-iterate-prompts.md)** - Refine categorization for your needs
3. **[Explore examples](examples/prompt-evolution.md)** - See how others refined their prompts

---

**Ready to customize?** [Start the Tutorial →](tutorial/index.md){ .md-button .md-button--primary }
