# Release Notes Automation Starter

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

This project demonstrates how to automate release notes creation from GitHub commits using AI. It provides practical automation patterns for docs-as-code workflows.

---

## Documentation

Complete documentation is available at [rebeja.github.io/docs-automation-examples](https://rebeja.github.io/docs-automation-examples/)

Documentation includes:

- Step-by-step tutorial (2-3 hours)
- Prompt engineering examples with evolution
- Troubleshooting guide and FAQ
- Sample outputs and metrics
- Configuration reference

---

## Quick Start

### Prerequisites

- Python 3.8+ (check with `python --version`)
- Git
- AI API access (Anthropic Claude or OpenAI account)
- GitHub personal access token
- Basic terminal usage

No programming experience is required.

### Installation

**1. Clone the repository:**

```bash
git clone https://github.com/rebeja/docs-automation-examples.git
cd docs-automation-examples
```

**2. Create a virtual environment:**

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

**3. Install dependencies:**

```bash
pip install -r requirements.txt
```

**4. Set up configuration:**

```bash
cp config.example.yaml config.yaml
```

**5. Add your API keys:**

Edit `config.yaml` and add your API keys. See the [documentation](https://rebeja.github.io/docs-automation-examples/getting-started/) for instructions on obtaining API keys.

### Generate Your First Release Notes

```bash
cd 01-release-notes-automation
python generate_release_notes.py \
  --repo octocat/Hello-World \
  --since 2024-01-01
```

Review the generated `release_notes.md` file.

See the [full tutorial](https://rebeja.github.io/docs-automation-examples/tutorial/) for detailed instructions.

---

## What You'll Learn

This project demonstrates:

1. **Process documentation** - Capturing your manual workflow as the foundation for automation
2. **Prompt engineering** - Teaching AI to apply your categorization standards
3. **Iterative refinement** - Improving automation based on actual results
4. **API integration** - Connecting to GitHub and AI providers
5. **Human-in-the-loop workflows** - Balancing automation with quality control

---

## What's Included

- Working Python script with GitHub API integration
- Complete tutorial (2-3 hours)
- Prompt evolution examples showing iteration from simple to refined (65% to 91% accuracy)
- Sample outputs with metrics
- Troubleshooting guide
- FAQ
- Configuration templates

---

## Key Principles

### Document Your Process First

Before automating anything, write down your manual workflow. Your documented process becomes the foundation for your automation prompt.

### Plan Before Code

Ask AI to write a plan first, then implement. Plans are faster to iterate than code.

### Human-in-the-Loop

Automation generates drafts. Humans provide final review and context. This maintains quality while saving time.

### Iterate Based on Results

Your first prompt won't be perfect. Test, refine, and improve based on real outputs.

---

## Architecture

```
GitHub API → Fetch Commits → Filter → AI Categorization → Format → Human Review → Publish
                                       ↑
                                Your Standards
                                (via prompt)
```

**Components:**

1. **GitHub API** - Fetches commits in date range
2. **Filter Logic** - Excludes internal/WIP changes
3. **AI Categorization** - Applies your standards via prompt
4. **Markdown Generation** - Formats consistently
5. **Human Review** - Final quality check and context addition

---

## Security Best Practices

### Do

- Use `config.yaml` (already in `.gitignore`)
- Use environment variables for production
- Rotate keys every 90 days
- Use minimal GitHub token scopes
- Set token expiration dates

### Don't

- Never commit `config.yaml` with real keys
- Don't share keys via Slack or email
- Don't use production keys for testing
- Don't grant unnecessary permissions
- Don't hardcode keys in scripts

---

## Resources

### Documentation

- [Full Documentation Site](https://rebeja.github.io/docs-automation-examples/)
- [Tutorial](https://rebeja.github.io/docs-automation-examples/tutorial/)
- [FAQ](https://rebeja.github.io/docs-automation-examples/faq/)
- [Troubleshooting](https://rebeja.github.io/docs-automation-examples/troubleshooting/)

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
- **Have a question?** Check the [FAQ](https://rebeja.github.io/docs-automation-examples/faq/) first
- **Want to contribute?** See [CONTRIBUTING.md](./CONTRIBUTING.md)

---

## Project Resources

- [Contributing Guidelines](./CONTRIBUTING.md)
- [Code of Conduct](./CODE_OF_CONDUCT.md)
- [Changelog](./CHANGELOG.md)
- [License](./LICENSE)
