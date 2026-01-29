# Getting Started

This guide will help you set up your environment and choose which project to start with.

## Choose Your Project

This repository contains two automation examples:

**Release Notes Automation** - Automate release notes creation from GitHub commits  
[Go to Release Notes Tutorial](release-notes/tutorial/index.md)

**Doc Site Portfolio** - Build a professional portfolio site with AI assistance  
[Go to Portfolio Tutorial](doc-site/tutorial/index.md)

Both projects share similar setup requirements. Follow the steps below to prepare your environment.

## Prerequisites

Before starting, make sure you have:

### Required

- Python 3.8 or higher (check with `python --version` or `python3 --version`)
- Git installed (check with `git --version`)
- AI API access (Anthropic Claude or OpenAI account)
- Text editor (VS Code, Cursor, Sublime Text, or similar)
- Command line comfort (ability to run terminal commands)

### Project-Specific

**For Release Notes Automation:**
- GitHub account for API access (or GitLab/Bitbucket equivalent)
- Existing docs-as-code workflow (makes adaptation easier)

**For Doc Site Portfolio:**
- GitHub account for deployment
- Portfolio content (projects, writing samples, experience)

### Recommended

- Cursor or AI coding tool for asking questions and iterating
- Write the Docs community membership for sharing and learning

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/rebeja/docs-automation-examples.git
cd docs-automation-examples
```

### 2. Choose Your Project Directory

Navigate to the project you want to start with:

**For Release Notes Automation:**
```bash
cd 01-release-notes-automation
```

**For Doc Site Portfolio:**
```bash
cd 02-doc-site-portfolio
```

### 3. Create Virtual Environment

Using a virtual environment keeps dependencies isolated.

**On macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

You should see `(venv)` in your terminal prompt.

### 4. Install Dependencies

**For Release Notes Automation:**

```bash
pip install --upgrade pip
pip install -r ../requirements.txt
```

This installs:

- `anthropic` or `openai` - AI provider SDKs
- `PyGithub` - GitHub API client
- `pyyaml` - Configuration file parsing

**For Doc Site Portfolio:**

```bash
pip install --upgrade pip
pip install -r template/requirements.txt
```

This installs:

- `mkdocs` - Static site generator
- `mkdocs-material` - Material theme
- `pymdown-extensions` - Markdown extensions

### 5. Verify Installation

**For Release Notes Automation:**

```bash
python -c "import anthropic; import github; print('Dependencies installed')"
```

**For Doc Site Portfolio:**

```bash
mkdocs --version
```

If you see output without errors, the setup is complete.

## Configuration

### Get AI API Keys

Both projects use AI for content generation. You'll need API access from one of these providers:

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

### Project-Specific Configuration

Each project has its own configuration requirements. Follow the tutorial for your chosen project for detailed setup:

**Release Notes Automation:**  
[Tutorial Step 1: Setup Environment](release-notes/tutorial/step-1-setup.md)

**Doc Site Portfolio:**  
[Tutorial Step 1: Setup Environment](doc-site/tutorial/step-1-setup.md)

## Next Steps

Once your environment is set up:

**For Release Notes Automation:**

1. [Document your process](release-notes/tutorial/step-2-document-process.md) - Write down your manual release notes workflow
2. [Configure APIs](release-notes/tutorial/step-3-configure.md) - Add your API keys
3. [Run first time](release-notes/tutorial/step-4-run-first-time.md) - Generate your first draft

[Start Release Notes Tutorial](release-notes/tutorial/index.md)

**For Doc Site Portfolio:**

1. [Plan your site](doc-site/tutorial/step-2-plan-site.md) - Define your portfolio goals
2. [Generate structure](doc-site/tutorial/step-3-generate-structure.md) - Create your site navigation
3. [Write content](doc-site/tutorial/step-4-write-content.md) - Draft your portfolio pages

[Start Portfolio Tutorial](doc-site/tutorial/index.md)

## Troubleshooting

If you encounter issues during setup:

- **Python not found** - Install Python from [python.org](https://www.python.org/downloads/)
- **Virtual environment issues** - Try `python3 -m venv venv` instead of `python -m venv venv`
- **Dependency installation fails** - Update pip with `pip install --upgrade pip`
- **Import errors** - Make sure your virtual environment is activated

For project-specific issues, see the troubleshooting guides:

- [Release Notes Troubleshooting](release-notes/troubleshooting.md)
- [Doc Site Troubleshooting](doc-site/troubleshooting.md)

---

**Ready to start?** Choose your project:

- [Release Notes Automation](release-notes/tutorial/index.md)
- [Doc Site Portfolio](doc-site/tutorial/index.md)
