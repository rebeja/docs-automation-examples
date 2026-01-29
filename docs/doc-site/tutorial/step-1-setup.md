# Step 1: Setup environment

Set up your local development environment and choose your starting point.

## Choose your path

Select the approach that matches your goals:

**Path A: Use the template** (Recommended for first-time users)
- Pre-configured MkDocs site with Material theme
- Basic structure already in place
- Focus on content creation
- Estimated time: 30 minutes

**Path B: Build from scratch**
- Learn complete MkDocs configuration
- Full customization control
- Understand every component
- Estimated time: 1-2 hours

This guide covers both paths. Skip to the section that matches your choice.

## Prerequisites check

Verify you have these installed:

```bash
python3 --version  # Should be 3.8 or higher
git --version      # Any recent version
```

If either command fails, install the missing software:
- Python: [python.org/downloads](https://www.python.org/downloads/)
- Git: [git-scm.com/downloads](https://git-scm.com/downloads)

## Path A: Use the template

### 1. Clone the repository

```bash
git clone https://github.com/rebeja/docs-automation-examples.git
cd docs-automation-examples/02-doc-site-portfolio
```

### 2. Create virtual environment

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

The terminal prompt shows `(venv)` when activated.

### 3. Install dependencies

```bash
pip install --upgrade pip
pip install -r template/requirements.txt
```

This installs:
- `mkdocs` - Static site generator
- `mkdocs-material` - Professional theme
- `pymdown-extensions` - Enhanced Markdown features

### 4. Test the template

```bash
cd template
mkdocs serve
```

Expected output:
```
INFO    - Building documentation...
INFO    - Cleaning site directory
INFO    - Documentation built in 0.52 seconds
INFO    - [12:34:56] Serving on http://127.0.0.1:8000/
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser. You see a basic portfolio site with placeholder content.

Press `Ctrl+C` to stop the server when finished reviewing.

### 5. Create your own copy

Copy the template to start customizing:

```bash
cd ..  # Back to 02-doc-site-portfolio
cp -r template my-portfolio
cd my-portfolio
```

Now you have your own copy to modify without affecting the template.

## Path B: Build from scratch

### 1. Create project directory

```bash
mkdir my-portfolio
cd my-portfolio
```

### 2. Create virtual environment

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

### 3. Install MkDocs

```bash
pip install --upgrade pip
pip install mkdocs mkdocs-material pymdown-extensions
```

### 4. Initialize MkDocs site

```bash
mkdocs new .
```

This creates:
```
.
├── docs/
│   └── index.md
└── mkdocs.yml
```

### 5. Configure Material theme

Open `mkdocs.yml` and replace contents with:

```yaml
site_name: Your Name - Technical Writer
site_description: Software documentation portfolio showcasing API docs, tutorials, and technical guides
site_author: Your Name
site_url: https://yourusername.github.io/my-portfolio/

theme:
  name: material
  palette:
    scheme: default
    primary: indigo
    accent: indigo
  features:
    - navigation.tabs
    - navigation.sections
    - navigation.expand
    - navigation.top
    - search.highlight
    - search.share
    - toc.follow

nav:
  - Home: index.md
  - About: about.md
  - Projects: projects/index.md
  - Samples: samples.md

markdown_extensions:
  - admonition
  - pymdownx.details
  - pymdownx.superfences
  - pymdownx.tabbed:
      alternate_style: true
  - toc:
      permalink: true

plugins:
  - search

extra:
  social:
    - icon: fontawesome/brands/github
      link: https://github.com/yourusername
    - icon: fontawesome/brands/linkedin
      link: https://linkedin.com/in/yourprofile
```

### 6. Create initial pages

Create the basic structure:

```bash
mkdir -p docs/projects
touch docs/about.md docs/samples.md docs/projects/index.md
```

### 7. Test your site

```bash
mkdocs serve
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) to see your site.

## Configure AI access

Both paths require AI provider setup for content generation.

### Option A: Anthropic (Claude)

1. Go to [console.anthropic.com](https://console.anthropic.com/)
2. Sign up or log in
3. Navigate to **API Keys**
4. Click **Create Key**
5. Name it "Portfolio Site Generation"
6. Copy the key (starts with `sk-ant-`)

Store the key securely in your password manager.

### Option B: OpenAI (GPT)

1. Go to [platform.openai.com](https://platform.openai.com/)
2. Sign up or log in
3. Navigate to **API Keys**
4. Click **Create new secret key**
5. Name it "Portfolio Site Generation"
6. Copy the key (starts with `sk-`)

Store the key securely in your password manager.

### Set up environment variable

Create a `.env` file in your project root (never commit this file):

For Anthropic:
```bash
ANTHROPIC_API_KEY=sk-ant-your-key-here
AI_PROVIDER=anthropic
```

For OpenAI:
```bash
OPENAI_API_KEY=sk-your-key-here
AI_PROVIDER=openai
```

Add `.env` to `.gitignore`:
```bash
echo ".env" >> .gitignore
```

## Verify setup

Check everything is working:

```bash
# Virtual environment is activated
which python
# Should show path ending in /venv/bin/python

# MkDocs is installed
mkdocs --version
# Should show version 1.5.0 or higher

# Site builds successfully
mkdocs build
# Should complete without errors
```

## Summary

You completed these tasks:

- ✓ Installed Python and Git
- ✓ Created virtual environment
- ✓ Installed MkDocs and Material theme
- ✓ Created or cloned project structure
- ✓ Configured AI provider access
- ✓ Verified local site preview works

## Troubleshooting

**Command not found errors:**
- Activate your virtual environment: `source venv/bin/activate` (or `venv\Scripts\activate` on Windows)

**Port already in use:**
- Stop other mkdocs servers: `pkill -f mkdocs` (macOS or Linux)
- Or use different port: `mkdocs serve -a localhost:8001`

**Import errors:**
- Reinstall dependencies: `pip install -r requirements.txt` (Path A) or `pip install mkdocs mkdocs-material pymdown-extensions` (Path B)

**Theme not applying:**
- Check `mkdocs.yml` for typos in theme configuration
- Restart mkdocs server after configuration changes

---

Next step: [Plan your site](step-2-plan-site.md)
