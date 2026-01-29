# Getting started

Set up your environment and choose which project to start with.

## Choose your project

This repository contains two automation examples:

Release notes automation - Automate release notes creation from GitHub commits  
[Go to release notes tutorial](release-notes/tutorial/index.md)

Doc site portfolio - Build a professional portfolio site with AI assistance  
[Go to portfolio tutorial](doc-site/tutorial/index.md)

Both projects share similar setup requirements.

## Prerequisites

Verify you have:

### Required

- Python 3.8 or higher (check with `python --version` or `python3 --version`)
- Git installed (check with `git --version`)
- AI API access (Anthropic Claude or OpenAI account)
- Text editor (VS Code, Cursor, Sublime Text, or similar)
- Command line comfort (ability to run terminal commands)

### Project-specific

For release notes automation:
- GitHub account for API access (or GitLab or Bitbucket equivalent)
- Existing docs-as-code workflow (makes adaptation easier)

For doc site portfolio:
- GitHub account for deployment
- Portfolio content (projects, writing samples, experience)

### Recommended

- Cursor or AI coding tool for asking questions and iterating
- Write the Docs community membership for sharing and learning

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/rebeja/docs-automation-examples.git
cd docs-automation-examples
```

### 2. Choose your project directory

Navigate to the project you want to start with:

For release notes automation:
```bash
cd 01-release-notes-automation
```

For doc site portfolio:
```bash
cd 02-doc-site-portfolio
```

### 3. Create virtual environment

On macOS or Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

The terminal prompt shows `(venv)`.

### 4. Install dependencies

For release notes automation:

```bash
pip install --upgrade pip
pip install -r ../requirements.txt
```

This installs:

- `anthropic` or `openai` - AI provider SDKs
- `PyGithub` - GitHub API client
- `pyyaml` - Configuration file parsing

For doc site portfolio:

```bash
pip install --upgrade pip
pip install -r template/requirements.txt
```

This installs:

- `mkdocs` - Static site generator
- `mkdocs-material` - Material theme
- `pymdown-extensions` - Markdown extensions

### 5. Verify installation

For release notes automation:

```bash
python -c "import anthropic; import github; print('Dependencies installed')"
```

For doc site portfolio:

```bash
mkdocs --version
```

Output without errors indicates successful setup.

## Configuration

### Get AI API keys

Both projects use AI for content generation. You need API access from one of these providers:

Option A: Anthropic (Claude)

1. Go to [console.anthropic.com](https://console.anthropic.com/)
2. Sign up or log in
3. Navigate to API Keys
4. Create a new key
5. Copy the key (starts with `sk-ant-...`)

Option B: OpenAI (ChatGPT)

1. Go to [platform.openai.com](https://platform.openai.com/)
2. Sign up or log in
3. Navigate to API Keys
4. Create a new key
5. Copy the key (starts with `sk-...`)

### Project-specific configuration

Each project has its own configuration requirements. Follow the tutorial for your chosen project for detailed setup:

Release notes automation:  
[Tutorial step 1: Setup environment](release-notes/tutorial/step-1-setup.md)

Doc site portfolio:  
[Tutorial step 1: Setup environment](doc-site/tutorial/step-1-setup.md)

## Next steps

After setting up your environment:

For release notes automation:

1. [Document your process](release-notes/tutorial/step-2-document-process.md) - Write down your manual release notes workflow
2. [Configure APIs](release-notes/tutorial/step-3-configure.md) - Add your API keys
3. [Run first time](release-notes/tutorial/step-4-run-first-time.md) - Generate your first draft

[Start release notes tutorial](release-notes/tutorial/index.md)

For doc site portfolio:

1. [Plan your site](doc-site/tutorial/step-2-plan-site.md) - Define your portfolio goals
2. [Generate structure](doc-site/tutorial/step-3-generate-structure.md) - Create your site navigation
3. [Write content](doc-site/tutorial/step-4-write-content.md) - Draft your portfolio pages

[Start portfolio tutorial](doc-site/tutorial/index.md)

## Troubleshooting

If you encounter issues during setup:

- Python not found - Install Python from [python.org](https://www.python.org/downloads/)
- Virtual environment issues - Try `python3 -m venv venv` instead of `python -m venv venv`
- Dependency installation fails - Update pip with `pip install --upgrade pip`
- Import errors - Make sure your virtual environment is activated

For project-specific issues, see the troubleshooting guides:

- [Release notes troubleshooting](release-notes/troubleshooting.md)
- [Doc site troubleshooting](doc-site/troubleshooting.md)

---

Choose your project:

- [Release notes automation](release-notes/tutorial/index.md)
- [Doc site portfolio](doc-site/tutorial/index.md)
