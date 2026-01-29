# Release Notes Automation Starter

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

> AI-assisted release notes generation for technical writers

Automate release notes creation from GitHub commits using AI coding agents. This starter project demonstrates practical automation patterns for docs-as-code workflows—no programming experience required.

---

## 📚 Documentation Site

**👉 [View Full Documentation →](https://rebeja.github.io/docs-automation-examples/)**

Complete documentation includes:

- ✅ Step-by-step tutorial (2-3 hours)
- ✅ Prompt engineering examples with evolution
- ✅ Troubleshooting guide and FAQ
- ✅ Sample outputs and metrics
- ✅ Configuration reference

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.8+** - Check with `python --version`
- **Git** - For cloning repository
- **AI API access** - Anthropic (Claude) or OpenAI account
- **GitHub token** - For accessing repositories
- **Command line comfort** - Basic terminal usage

**No programming experience required!**

### Installation

```bash
# 1. Clone repository
git clone https://github.com/rebeja/docs-automation-examples.git
cd docs-automation-examples

# 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create configuration file
cp config.example.yaml config.yaml

# 5. Add your API keys to config.yaml
# (See documentation for getting API keys)
```

### First Run

Generate release notes:

```bash
cd 01-release-notes-automation
python generate_release_notes.py \
  --repo octocat/Hello-World \
  --since 2024-01-01
```

Review the generated `release_notes.md` file.

**📖 [Read the full tutorial →](https://rebeja.github.io/docs-automation-examples/tutorial/)**

---

## ⏱️ Time Savings

| Manual Process | With Automation |
|---------------|----------------|
| 4-8 hours per release | 15-30 minutes |
| Review 50+ commits individually | Review AI-generated draft |
| Manual categorization | AI categorization with your standards |
| Inconsistent formatting | Consistent, templated output |

**86% time reduction** while maintaining quality through human review.

---

## 🎯 What You'll Learn

1. **Document process first** - How to capture your manual workflow
2. **Prompt engineering** - Teaching AI your categorization standards
3. **Iterative refinement** - Improving automation based on results
4. **API integration** - Connecting to GitHub and AI providers
5. **Human-in-the-loop** - Balancing automation with quality control

---

## 📂 What's Included

- **Working Python script** - Actual GitHub API integration
- **Tutorial (2-3 hours)** - Complete step-by-step guide
- **Prompt evolution** - Shows iteration from simple to refined (65% → 91% accuracy)
- **Sample outputs** - Real examples with metrics
- **Troubleshooting guide** - Solutions to common issues
- **FAQ** - Answers to frequent questions
- **Configuration templates** - Easy setup

---

## 🔑 Key Principles

!!! success "Document Your Process First"
    Before automating anything, write down your manual workflow. Your documented process becomes the foundation for your automation prompt.

!!! success "Plan Before Code"
    Ask AI to write a plan first, then implement. Plans are faster to iterate than code.

!!! success "Human-in-the-Loop"
    Automation generates drafts; humans provide final review and context. This maintains quality while saving time.

!!! success "Iterate Based on Results"
    Your first prompt won't be perfect. Test, refine, and improve based on real outputs.

---

## 🛠️ Architecture

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

## 🔒 Security Best Practices

### DO ✅

- Use `config.yaml` (already in `.gitignore`)
- Use environment variables for production
- Rotate keys every 90 days
- Use minimal GitHub token scopes
- Set token expiration dates

### DON'T ❌

- Never commit `config.yaml` with real keys
- Don't share keys via Slack/email
- Don't use production keys for testing
- Don't grant unnecessary permissions
- Don't hardcode keys in scripts

---

## 📚 Resources

### Documentation

- **[Full Documentation Site →](https://rebeja.github.io/docs-automation-examples/)**
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

## 📝 License

[![CC BY 4.0][cc-by-shield]][cc-by]

This work is licensed under a [Creative Commons Attribution 4.0 International License][cc-by].

You are free to share and adapt this material for any purpose, even commercially, as long as you give appropriate credit.

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg

---

## 💬 Support

- **📖 Documentation:** [rebeja.github.io/docs-automation-examples](https://rebeja.github.io/docs-automation-examples/)
- **🐛 Found a bug?** [Open an issue](https://github.com/rebeja/docs-automation-examples/issues)
- **💡 Have a question?** Check the [FAQ](https://rebeja.github.io/docs-automation-examples/faq/) first
- **🤝 Want to contribute?** See [CONTRIBUTING.md](./CONTRIBUTING.md) - all contributions welcome!

---

## 🙏 Acknowledgments

Created for the technical writing community to demonstrate practical AI-assisted automation patterns.

**Special thanks to:**

- Write the Docs community
- AI tool developers (Anthropic, Cursor, OpenAI)
- Everyone exploring AI-assisted automation

## 📋 Project Resources

- [Contributing Guidelines](./CONTRIBUTING.md) - How to contribute
- [Code of Conduct](./CODE_OF_CONDUCT.md) - Community standards
- [Changelog](./CHANGELOG.md) - Version history
- [License](./LICENSE) - CC BY 4.0 License

---

**Ready to automate your release notes?** [Get Started →](https://rebeja.github.io/docs-automation-examples/getting-started/){ .md-button .md-button--primary }
