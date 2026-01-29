# Step 1: Setup environment

Set up your development environment with all necessary tools and dependencies.

**Time estimate:** 15-20 minutes

## Complete these tasks

- Install and verify Python 3.8+
- Create virtual environment
- Install all dependencies
- Create configuration file
- Run first test successfully

## Prerequisites

- Command line or terminal access
- Text editor installed
- Internet connection for downloads

## Instructions

### 1. Verify Python installation

Check if Python is installed:

```bash
python --version
# or
python3 --version
```

The output shows `Python 3.8.0` or higher.

Download Python 3.8+ from [python.org](https://www.python.org/downloads/) if you see Python 2.x or no Python installed.

### 2. Clone the repository

```bash
git clone https://github.com/rebeja/docs-automation-examples.git
cd docs-automation-examples
```

Verify the project files exist:

```bash
ls
# Shows: 01-release-notes-automation/ README.md requirements.txt ...
```

### 3. Create virtual environment

Virtual environments keep project dependencies isolated.

**macOS or Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows (PowerShell):**

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**

```bash
python -m venv venv
venv\Scripts\activate.bat
```

Verify your prompt shows `(venv)`:

```
(venv) your-computer:docs-automation-examples$
```

Enable script execution on Windows if needed:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 4. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

Installed packages:

| Package | Purpose |
|---------|---------|
| `anthropic` | Claude AI API client |
| `openai` | OpenAI/ChatGPT API client |
| `PyGithub` | GitHub API wrapper |
| `pyyaml` | Configuration file parsing |
| `python-dotenv` | Environment variable management |
| `requests` | HTTP requests |

Verify installation:

```bash
pip list | grep -E "anthropic|openai|PyGithub"
```

The output shows installed versions.

### 5. Create configuration file

Copy the example configuration:

```bash
cp config.example.yaml config.yaml
```

Open `config.yaml` in your editor:

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

The `config.yaml` file is in `.gitignore` to prevent accidental commits of API keys. Never commit files with real API keys.

### 6. Get API keys (placeholder for now)

Get real API keys in [Step 3](step-3-configure.md). For now, leave placeholders:

```yaml
ai_api_key: "PLACEHOLDER"
github_token: "PLACEHOLDER"
```

### 7. Verify setup

Test that imports work:

```bash
python -c "import anthropic; import github; import yaml; print('All dependencies imported successfully')"
```

The output shows `All dependencies imported successfully`.

### 8. Navigate to project directory

```bash
cd 01-release-notes-automation
ls
```

The directory contains these files:

```
generate_release_notes.py
prompts/
examples/
README.md
```

### 9. Test help command

```bash
python generate_release_notes.py --help
```

The output shows:

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

Setup is complete when you see this output.

## Troubleshooting

### Python command not found

**Problem:** `python: command not found`

**Solution:** Try `python3` instead, or install Python from [python.org](https://www.python.org/downloads/)

### Permission denied (Windows)

**Problem:** Cannot activate virtual environment

**Solution:** Run PowerShell as Administrator and enable scripts:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Import errors

**Problem:** `ModuleNotFoundError: No module named 'anthropic'`

**Solution:**

1. Verify virtual environment is activated (look for `(venv)` in prompt)
2. Reinstall dependencies: `pip install -r requirements.txt`
3. Check Python version: `python --version` (must be 3.8+)

### Git clone fails

**Problem:** Cannot clone repository

**Solution:**

1. Verify Git is installed: `git --version`
2. Check internet connection
3. Try HTTPS URL instead of SSH

## Summary

You set up a Python virtual environment, installed required dependencies, created configuration files, and verified the setup works.

## Next step

Document your manual process—the most important step in this tutorial.

[Next: Step 2 - Document your process](step-2-document-process.md)

---

Check the [Troubleshooting Guide](../troubleshooting.md) or [FAQ](../faq.md) for help with issues.
