# Contributing to Release Notes Automation Starter

Thank you for your interest in contributing. This project helps technical writers explore AI-assisted automation, and I welcome contributions from everyone.

## Ways to Contribute

### Report Bugs

If you find a bug:

1. Check existing issues to see if it has already been reported
2. Create a detailed bug report that includes:
   - What you expected to happen
   - What actually happened
   - Steps to reproduce the issue
   - Your environment (Python version, OS, etc.)
   - Error messages or logs

[Report a bug](https://github.com/rebeja/docs-automation-examples/issues/new)

### Suggest Enhancements

You can suggest improvements for:

- Documentation improvements (clarify confusing sections, add examples)
- New features (additional automation patterns, integrations)
- Examples (more prompt templates, sample outputs)
- Tutorial improvements (better explanations, additional steps)

[Suggest an enhancement](https://github.com/rebeja/docs-automation-examples/issues/new)

### Improve Documentation

Documentation contributions are welcome. You can:

- Fix typos or unclear explanations
- Add more examples to tutorials
- Improve prompt templates
- Create guides for new use cases

### Contribute Code

Code contributions are welcome. Consider:

- Bug fixes
- Performance improvements
- New AI provider integrations
- Additional categorization strategies
- Testing improvements

## Getting Started

### Development Setup

**1. Fork and clone the repository:**

```bash
git clone https://github.com/YOUR-USERNAME/docs-automation-examples.git
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

**4. Test your setup:**

```bash
cd 01-release-notes-automation
python generate_release_notes.py --sample
```

### Documentation Development

To work on the documentation site:

**1. Install MkDocs dependencies:**

```bash
pip install mkdocs-material
```

**2. Serve documentation locally:**

```bash
mkdocs serve
```

The site will be available at `http://127.0.0.1:8000/`

**3. Make your changes** in the `docs/` directory

**4. Preview changes** - The local server auto-reloads

## Contribution Guidelines

### Code Style

- **Python**: Follow PEP 8 style guidelines
- **Line length**: 100 characters maximum
- **Comments**: Clear, concise, explain "why" not "what"
- **Functions**: Keep them focused and well-named

### Documentation Style

- **Tone**: Clear, educational, professional
- **Audience**: Technical writers (may not have development background)
- **Format**: Use Markdown, follow existing structure
- **Examples**: Include practical, realistic examples
- **Links**: Always test that links work

### Commit Messages

Write clear commit messages:

- **Good**: "Fix API key validation error in config loader"
- **Good**: "Add example for multi-repo release notes"
- **Avoid**: "Fixed stuff" or "Updated files"

Format:
```
Brief description (50 chars or less)

More detailed explanation if needed. Explain the problem
this commit solves and why you chose this solution.
```

## Pull Request Process

### Before Submitting

- Test your changes thoroughly
- Update documentation if you changed functionality
- Add examples if you added features
- Check that all links in documentation still work
- Run the sample data test: `python generate_release_notes.py --sample`

### Submitting a PR

**1. Create a feature branch:**

```bash
git checkout -b feature/your-feature-name
```

**2. Make your changes and commit:**

```bash
git add .
git commit -m "Add feature: your feature description"
```

**3. Push to your fork:**

```bash
git push origin feature/your-feature-name
```

**4. Open a Pull Request**

Include in your PR description:
- What changes you made and why
- Any related issues (e.g., "Fixes #123")
- Screenshots if UI/documentation changes
- Testing you performed

### PR Review Process

- I will review your PR within a few days
- I may suggest changes or ask questions
- Once approved, I will merge your PR
- Your contribution will be credited in the release notes

## Types of Contributions

### High Priority

- Bug fixes, especially those affecting core functionality
- Documentation clarity to make tutorials easier to follow
- Example improvements with better prompt templates and realistic samples
- Error handling with better error messages and recovery

### Welcome Additions

- New AI provider support (Azure OpenAI, local models, etc.)
- Additional categorization strategies with domain-specific examples
- Integration guides (GitLab, Bitbucket, Azure DevOps)
- Internationalization (translations, i18n support)

### Out of Scope

- Major architectural changes (please discuss in an issue first)
- Platform-specific features (keep it cross-platform)
- Features requiring paid services (keep barrier to entry low)

## Questions

- **General questions**: [Open a discussion](https://github.com/rebeja/docs-automation-examples/discussions)
- **Bug reports**: [Open an issue](https://github.com/rebeja/docs-automation-examples/issues)
- **Security concerns**: Email the maintainer (see README)

## Recognition

Contributors will be:
- Listed in release notes
- Added to the repository contributors page
- Thanked in the documentation

## Code of Conduct

### Standards

I am committed to providing a welcoming and inclusive experience for everyone. I expect all contributors to:

- Use welcoming and inclusive language
- Be respectful of differing viewpoints and experiences
- Gracefully accept constructive criticism
- Focus on what is best for the community
- Show empathy towards other community members

### Unacceptable Behavior

- Harassment, trolling, or personal attacks
- Publishing others' private information
- Any conduct which could reasonably be considered inappropriate

### Enforcement

Instances of unacceptable behavior may be reported to me. All complaints will be reviewed and investigated promptly and fairly.

## Development Tips

### Testing with Real Repositories

When testing your changes:

1. Start with sample data using the `--sample` flag
2. Test with small repos (repositories with <50 commits)
3. Check API costs by monitoring your AI provider usage
4. Use test API keys, not production keys for development

### Documentation Testing

Before submitting documentation PRs:

```bash
# Build the full site
mkdocs build

# Check for broken links (if you have a link checker)
# Manually test all new links
```

### Common Issues

**"ModuleNotFoundError: No module named 'anthropic'"**
- Reinstall dependencies: `pip install -r requirements.txt`

**"GitHub API rate limit exceeded"**
- Use personal access token, not unauthenticated access
- Test with `--sample` flag to avoid API calls

**Documentation not updating**
- Hard refresh your browser (Ctrl+Shift+R or Cmd+Shift+R)
- Clear MkDocs cache: `mkdocs build --clean`

---

Check out the [good first issue](https://github.com/rebeja/docs-automation-examples/labels/good%20first%20issue) label for beginner-friendly tasks.
