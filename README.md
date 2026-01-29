# Documentation Automation Examples

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

Practical examples and tutorials for technical writers exploring AI-assisted documentation automation.

---

## Projects

This repository contains two complete automation examples:

### 1. Release Notes Automation

Automate release notes creation from GitHub commits using AI categorization.

**What it does:** Fetches commits, filters internal changes, categorizes content, and generates formatted Markdown drafts.

**Best for:** Technical writers in docs-as-code environments releasing software regularly.

[View Tutorial](https://rebeja.github.io/docs-automation-examples/release-notes/tutorial/)

### 2. Doc Site Portfolio

Build a professional technical writing portfolio site with AI assistance.

**What it does:** Provides MkDocs template, guides content generation with AI, and deploys to GitHub Pages.

**Best for:** Technical writers building portfolios and showcasing documentation projects.

[View Tutorial](https://rebeja.github.io/docs-automation-examples/doc-site/tutorial/)

---

## Documentation

Complete documentation is available at [rebeja.github.io/docs-automation-examples](https://rebeja.github.io/docs-automation-examples/)

Documentation includes:

- Step-by-step tutorials for both projects
- Prompt engineering examples with evolution
- Troubleshooting guides and FAQs
- Sample outputs and metrics
- Configuration references

---

## Quick Start

### Choose Your Project

**Release Notes Automation** - Automate release notes from Git commits  
**Doc Site Portfolio** - Build a portfolio website with AI

Both projects share similar prerequisites and setup steps.

### Prerequisites

- Python 3.8+ (check with `python --version`)
- Git
- AI API access (Anthropic Claude or OpenAI account)
- Text editor
- Basic terminal usage

No programming experience is required.

### Installation

**1. Clone the repository:**

```bash
git clone https://github.com/rebeja/docs-automation-examples.git
cd docs-automation-examples
```

**2. Choose your project:**

Navigate to the project directory:

```bash
cd 01-release-notes-automation  # For release notes
# or
cd 02-doc-site-portfolio        # For portfolio site
```

**3. Create a virtual environment:**

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

**4. Install dependencies:**

For release notes automation:
```bash
pip install -r ../requirements.txt
```

For doc site portfolio:
```bash
pip install -r template/requirements.txt
```

**5. Follow the tutorial:**

See the [full documentation](https://rebeja.github.io/docs-automation-examples/getting-started/) for project-specific setup and API key instructions.

---

## What You'll Learn

Both projects demonstrate fundamental automation skills:

1. **Process documentation** - Capturing your manual workflow as the foundation for automation
2. **Prompt engineering** - Teaching AI to apply your standards
3. **Iterative refinement** - Improving automation based on actual results
4. **API integration** - Connecting to services and tools
5. **Human-in-the-loop workflows** - Balancing automation with quality control

---

## What's Included

### Release Notes Automation

- Working Python script with GitHub API integration
- Complete tutorial (2-3 hours)
- Prompt evolution examples (65% to 91% accuracy improvement)
- Sample outputs with metrics
- Configuration templates

### Doc Site Portfolio

- MkDocs template for portfolio sites
- AI-assisted content generation scripts
- Reusable prompts for portfolio pages
- Step-by-step tutorial (4-6 hours)
- Deployment guide for GitHub Pages

---

## Key Principles

These projects demonstrate important automation principles:

### Document Your Process First

Before automating anything, write down your manual workflow. Your documented process becomes the foundation for your automation.

### Plan Before Code

Ask AI to write a plan first, then implement. Plans are faster to iterate than code.

### Human-in-the-Loop

Automation generates drafts. Humans provide final review and context. This maintains quality while saving time.

### Iterate Based on Results

Your first prompt won't be perfect. Test, refine, and improve based on real outputs.

---

## Security Best Practices

### Do

- Use `config.yaml` (already in `.gitignore`)
- Use environment variables for production
- Rotate keys every 90 days
- Use minimal API token scopes
- Set token expiration dates

### Don't

- Never commit configuration files with real keys
- Don't share keys via Slack or email
- Don't use production keys for testing
- Don't grant unnecessary permissions
- Don't hardcode keys in scripts

---

## Resources

### Documentation

- [Full Documentation Site](https://rebeja.github.io/docs-automation-examples/)
- [Getting Started](https://rebeja.github.io/docs-automation-examples/getting-started/)
- [Release Notes Tutorial](https://rebeja.github.io/docs-automation-examples/release-notes/tutorial/)
- [Portfolio Tutorial](https://rebeja.github.io/docs-automation-examples/doc-site/tutorial/)

### Community

- [Write the Docs](https://www.writethedocs.org/)
- [Technical Writer HQ](https://technicalwriterhq.com/)
- [Docs-as-Code Guide](https://www.writethedocs.org/guide/docs-as-code/)

### AI & Prompt Engineering

- [Anthropic Prompt Library](https://docs.anthropic.com/claude/prompt-library)
- [OpenAI Prompt Engineering](https://platform.openai.com/docs/guides/prompt-engineering)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)

---

## License

This work is licensed under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/).

You are free to share and adapt this material for any purpose, even commercially, as long as you give appropriate credit.

---

## Support

- **Documentation:** [rebeja.github.io/docs-automation-examples](https://rebeja.github.io/docs-automation-examples/)
- **Found a bug?** [Open an issue](https://github.com/rebeja/docs-automation-examples/issues)
- **Have a question?** Check the [FAQ](https://rebeja.github.io/docs-automation-examples/release-notes/faq/)
- **Want to contribute?** See [CONTRIBUTING.md](./CONTRIBUTING.md)

---

## Project Resources

- [Contributing Guidelines](./CONTRIBUTING.md)
- [Code of Conduct](./CODE_OF_CONDUCT.md)
- [Changelog](./CHANGELOG.md)
- [License](./LICENSE)
