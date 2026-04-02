# Step 1: Setup environment

Set up your local development environment and choose your starting point.

## Choose your path

Select the approach that matches your goals:

**[Path A: Use the template](#path-a-use-the-template)** (Recommended for first-time users)
- Pre-configured MkDocs site with Material theme
- Basic structure already in place
- Focus on content creation
- Estimated time: 30 minutes

**[Path B: Build from scratch](#path-b-build-from-scratch)**
- Learn complete MkDocs configuration
- Full customization control
- Understand every component
- Estimated time: 1-2 hours

**[Path C: Use Claude Code CLI](#path-c-use-claude-code-cli)** (Recommended if you prefer interactive AI)
- Conversational workflow — no scripts or API keys
- Claude reads and writes files directly in your terminal
- Requires a claude.ai Pro or Max subscription
- Estimated time: 30 minutes setup, then interactive

This guide covers all three paths. Skip to the section that matches your choice.

**Which path is right for you?** If you want a repeatable, automated workflow and are comfortable managing an API key and running Python scripts, choose Path A or B. Path A gets you started faster with a pre-built template; Path B gives you full control by building from scratch. If you'd rather skip API keys and scripts entirely and instead have a back-and-forth conversation with Claude directly in your terminal — where Claude reads and writes files for you — choose Path C. Path C requires a claude.ai Pro or Max subscription but has no additional setup beyond installing the Claude Code CLI.

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

Now you have your own copy to modify without affecting the template. Jump ahead to [Configure AI access](#configure-ai-access) to continue.

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

## Path C: Use Claude Code CLI

Claude Code is Anthropic's CLI that lets you interact with Claude directly in your terminal. Instead of running scripts, you describe what you want and Claude reads, creates, and edits files for you.

### 1. Install Claude Code

```bash
npm install -g @anthropic-ai/claude-code
```

Requires Node.js 18 or higher. Verify with `node --version`.

### 2. Authenticate

```bash
claude
```

This opens a browser login prompt. Sign in with your Anthropic account. A **claude.ai Pro or Max subscription** is required — no separate API key is needed.

### 3. Open your project directory

```bash
cd docs-automation-examples/02-doc-site-portfolio/my-portfolio
claude
```

Claude Code starts in your project directory and can see all your files.

### 4. Verify it works

Type a quick test prompt:

```
What files are in this directory?
```

Claude will list your project files, confirming it has access.

From here, instead of running Python scripts in later steps, you will type prompts directly in this terminal session. Claude will generate content and write it to the correct files.

## Configure AI access

> **Path C users**: Skip this section. Claude Code handles authentication through your claude.ai account — no API key or `config.yaml` needed. Jump ahead to [Customize theme](#customize-theme-optional).

Paths A and B require AI provider setup for content generation.

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

### Set up config.yaml

The content generation scripts read credentials from `config.yaml` at the root of the repository. Copy the example file and fill in your details:

```bash
# From the docs-automation-examples/ root directory
cp config.example.yaml config.yaml
```

Open `config.yaml` and update these fields:

For Anthropic (Claude):
```yaml
ai_provider: anthropic
ai_api_key: sk-ant-your-key-here
model: claude-3-5-sonnet-20241022
```

For OpenAI (GPT):
```yaml
ai_provider: openai
ai_api_key: sk-your-key-here
model: gpt-4
```

`config.yaml` is already listed in `.gitignore` and will not be committed to version control.

## Customize theme (optional)

Basic theme customization makes your portfolio unique. These changes are optional but recommended.

### Choose colors

Edit `mkdocs.yml` to change color scheme:

```yaml
theme:
  name: material
  palette:
    scheme: default  # or 'slate' for dark mode
    primary: indigo  # Change to: blue, teal, purple, etc.
    accent: cyan     # Change to: light blue, green, orange, etc.
```

**Color options**: red, pink, purple, deep purple, indigo, blue, light blue, cyan, teal, green, light green, lime, yellow, amber, orange, deep orange

**Recommended combinations**:
- Professional: `primary: blue`, `accent: light blue`
- Modern: `primary: indigo`, `accent: cyan`
- Vibrant: `primary: teal`, `accent: green`

### Enable dark mode toggle

Allow visitors to switch between light and dark:

```yaml
theme:
  name: material
  palette:
    # Light mode
    - media: "(prefers-color-scheme: light)"
      scheme: default
      primary: indigo
      accent: cyan
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode
    
    # Dark mode
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      primary: indigo
      accent: cyan
      toggle:
        icon: material/brightness-4
        name: Switch to light mode
```

This adds a theme toggle button in the header.

### Choose fonts (optional)

Change text and code fonts:

```yaml
theme:
  name: material
  font:
    text: Inter       # or: Open Sans, Ubuntu, Roboto
    code: Fira Code   # or: Source Code Pro, Roboto Mono
```

Or use system fonts for faster loading:

```yaml
theme:
  font: false
```

### Test your customizations

After making changes:

```bash
# Restart the server
# Press Ctrl+C to stop, then:
mkdocs serve
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) to see your customizations.

For more customization options, see [Theme customization reference](../reference/theme-customization.md).

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
