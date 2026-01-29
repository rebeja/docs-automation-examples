# Contributing to Release Notes Automation Starter

Thank you for your interest in contributing! This project helps technical writers explore AI-assisted automation, and we welcome contributions from everyone—whether you're a seasoned developer or just starting with automation.

## Ways to Contribute

### 🐛 Report Bugs

Found something broken? Help us fix it:

1. **Check existing issues** - Someone might have already reported it
2. **Create a detailed bug report** - Include:
   - What you expected to happen
   - What actually happened
   - Steps to reproduce the issue
   - Your environment (Python version, OS, etc.)
   - Error messages or logs

[Report a bug →](https://github.com/rebeja/docs-automation-examples/issues/new)

### 💡 Suggest Enhancements

Have an idea to improve the project?

- **Documentation improvements** - Clarify confusing sections, add examples
- **New features** - Additional automation patterns, integrations
- **Examples** - More prompt templates, sample outputs
- **Tutorial improvements** - Better explanations, additional steps

[Suggest an enhancement →](https://github.com/rebeja/docs-automation-examples/issues/new)

### 📝 Improve Documentation

Documentation contributions are highly valued! You can:

- Fix typos or unclear explanations
- Add more examples to tutorials
- Improve prompt templates
- Create guides for new use cases
- Translate documentation (future)

### 💻 Contribute Code

Code contributions welcome! Consider:

- Bug fixes
- Performance improvements
- New AI provider integrations
- Additional categorization strategies
- Testing improvements

## Getting Started

### Development Setup

1. **Fork and clone the repository**

```bash
git clone https://github.com/YOUR-USERNAME/docs-automation-examples.git
cd docs-automation-examples
```

2. **Create a virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Test your setup**

```bash
cd 01-release-notes-automation
python generate_release_notes.py --sample
```

### Documentation Development

To work on the documentation site:

1. **Install MkDocs dependencies** (if not already installed)

```bash
pip install mkdocs-material
```

2. **Serve documentation locally**

```bash
mkdocs serve
```

The site will be available at `http://127.0.0.1:8000/`

3. **Make your changes** in the `docs/` directory

4. **Preview changes** - The local server auto-reloads

## Contribution Guidelines

### Code Style

- **Python**: Follow PEP 8 style guidelines
- **Line length**: 100 characters maximum
- **Comments**: Clear, concise, explain "why" not "what"
- **Functions**: Keep them focused and well-named

### Documentation Style

- **Tone**: Friendly, educational, encouraging
- **Audience**: Technical writers (may not be developers)
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

- [ ] Test your changes thoroughly
- [ ] Update documentation if you changed functionality
- [ ] Add examples if you added features
- [ ] Check that all links in documentation still work
- [ ] Run the sample data test: `python generate_release_notes.py --sample`

### Submitting a PR

1. **Create a feature branch**

```bash
git checkout -b feature/your-feature-name
```

2. **Make your changes and commit**

```bash
git add .
git commit -m "Add feature: your feature description"
```

3. **Push to your fork**

```bash
git push origin feature/your-feature-name
```

4. **Open a Pull Request**

Include in your PR description:
- What changes you made and why
- Any related issues (e.g., "Fixes #123")
- Screenshots if UI/documentation changes
- Testing you performed

### PR Review Process

- A maintainer will review your PR within a few days
- We may suggest changes or ask questions
- Once approved, a maintainer will merge your PR
- Your contribution will be credited in the release notes!

## Types of Contributions We're Looking For

### High Priority

- **Bug fixes** - Especially those affecting core functionality
- **Documentation clarity** - Making tutorials easier to follow
- **Example improvements** - Better prompt templates, realistic samples
- **Error handling** - Better error messages and recovery

### Welcome Additions

- **New AI provider support** - Azure OpenAI, local models, etc.
- **Additional categorization strategies** - Domain-specific examples
- **Integration guides** - GitLab, Bitbucket, Azure DevOps
- **Internationalization** - Translations, i18n support

### Out of Scope (for now)

- Major architectural changes - Please discuss in an issue first
- Platform-specific features - Keep it cross-platform
- Features requiring paid services - Keep barrier to entry low

## Questions?

- **General questions**: [Open a discussion](https://github.com/rebeja/docs-automation-examples/discussions)
- **Bug reports**: [Open an issue](https://github.com/rebeja/docs-automation-examples/issues)
- **Security concerns**: Email the maintainer (see README)

## Recognition

Contributors will be:
- Listed in release notes
- Added to the repository contributors page
- Thanked in the documentation

## Code of Conduct

### Our Standards

We are committed to providing a welcoming and inclusive experience for everyone. We expect all contributors to:

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

Instances of unacceptable behavior may be reported to the project maintainers. All complaints will be reviewed and investigated promptly and fairly.

## Development Tips

### Testing with Real Repositories

When testing your changes:

1. **Start with sample data** - Use `--sample` flag
2. **Test with small repos** - Use repositories with <50 commits
3. **Check API costs** - Monitor your AI provider usage
4. **Use test API keys** - Don't use production keys for development

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

## Thank You! 🎉

Your contributions make this project better for the entire technical writing community. Whether you're fixing a typo, adding a feature, or helping others in discussions—every contribution matters.

---

**Ready to contribute?** Check out the [good first issue](https://github.com/rebeja/docs-automation-examples/labels/good%20first%20issue) label for beginner-friendly tasks!
