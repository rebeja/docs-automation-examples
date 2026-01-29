# Step 1: Setup Environment

In this step, you'll set up your development environment with all necessary tools and dependencies.

**Time Estimate:** 15-20 minutes

## What You'll Accomplish

By the end of this step:

- Python 3.8+ installed and verified
- Virtual environment created
- All dependencies installed
- Configuration file created
- First test run successful

## Prerequisites

Before starting, ensure you have:

- Command line/terminal access
- Text editor installed
- Internet connection for downloads

## Step-by-Step Instructions

### 1. Verify Python Installation

Check if Python is installed:

```bash
python --version
# or
python3 --version
```

**Expected output:** `Python 3.8.0` or higher

**If you see Python 2.x or no Python installed:** Download Python 3.8+ from [python.org](https://www.python.org/downloads/)

### 2. Clone the Repository

```bash
git clone https://github.com/rebeja/docs-automation-examples.git
cd docs-automation-examples
```

**Verify:** You should see the project files:

```bash
ls
# Expected: 01-release-notes-automation/ README.md requirements.txt ...
```

### 3. Create Virtual Environment

Virtual environments keep project dependencies isolated.

**On macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows (PowerShell):**

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**On Windows (Command Prompt):**

```bash
python -m venv venv
venv\Scripts\activate.bat
```

**Verify:** Your prompt should now show `(venv)`:

```
(venv) your-computer:docs-automation-examples$
```

**Activation Issues on Windows:** You may need to enable script execution:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 4. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

This installs:

| Package | Purpose |
|---------|---------|
| `anthropic` | Claude AI API client |
| `openai` | OpenAI/ChatGPT API client |
| `PyGithub` | GitHub API wrapper |
| `pyyaml` | Configuration file parsing |
| `python-dotenv` | Environment variable management |
| `requests` | HTTP requests |

**Verify installation:**

```bash
pip list | grep -E "anthropic|openai|PyGithub"
```

Should show installed versions.

### 5. Create Configuration File

Copy the example configuration:

```bash
cp config.example.yaml config.yaml
```

**Open config.yaml in your editor:**

```yaml
# AI Provider - Choose ONE
ai_provider: "anthropic"  # or "openai"
ai_api_key: "YOUR_KEY_HERE"
model: "claude-3-sonnet-20240229"

# GitHub
github_token: "YOUR_TOKEN_HERE"

# Optional settings
default_repo: ""
output_file: "release_notes.md"
```

**Security Note:** The `config.yaml` file is in `.gitignore` to prevent accidental commits of API keys. Never commit files with real API keys.

### 6. Get API Keys (Placeholder for Now)

You'll get real API keys in [Step 3](step-3-configure.md). For now, leave placeholders:

```yaml
ai_api_key: "PLACEHOLDER"
github_token: "PLACEHOLDER"
```

### 7. Verify Setup

Test that imports work:

```bash
python -c "import anthropic; import github; import yaml; print('All dependencies imported successfully')"
```

**Expected output:** `All dependencies imported successfully`

### 8. Navigate to Project Directory

```bash
cd 01-release-notes-automation
ls
```

You should see:

```
generate_release_notes.py
prompts/
examples/
README.md
```

### 9. Test Help Command

```bash
python generate_release_notes.py --help
```

**Expected output:**

```
usage: generate_release_notes.py [-h] --repo REPO --since SINCE
                                  [--config CONFIG] [--output OUTPUT]

Generate release notes from commits

optional arguments:
  -h, --help       show this help message and exit
  --repo REPO      Repository (owner/repo)
  --since SINCE    Start date (YYYY-MM-DD)
  --config CONFIG  Config file path
  --output OUTPUT  Output file
```

If you see this, setup is complete.

## Troubleshooting

### Python Command Not Found

**Problem:** `python: command not found`

**Solution:** Try `python3` instead, or install Python from [python.org](https://www.python.org/downloads/)

### Permission Denied (Windows)

**Problem:** Cannot activate virtual environment

**Solution:** Run PowerShell as Administrator and enable scripts:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Import Errors

**Problem:** `ModuleNotFoundError: No module named 'anthropic'`

**Solution:**

1. Verify virtual environment is activated (look for `(venv)` in prompt)
2. Reinstall dependencies: `pip install -r requirements.txt`
3. Check Python version: `python --version` (must be 3.8+)

### Git Clone Fails

**Problem:** Cannot clone repository

**Solution:**

1. Verify Git is installed: `git --version`
2. Check internet connection
3. Try HTTPS URL instead of SSH

## What You've Learned

In this step, you:

- Set up a Python virtual environment
- Installed required dependencies
- Created configuration files
- Verified the setup works

## Next Step

Now that your environment is ready, move on to the most important step: documenting your manual process.

[Next: Step 2 - Document Your Process](step-2-document-process.md)

---

**Having issues?** Check the [Troubleshooting Guide](../troubleshooting.md) or [FAQ](../faq.md).
