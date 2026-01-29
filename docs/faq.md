# Frequently Asked Questions

## General Questions

### What is this project?

A starter kit for automating release notes generation from GitHub commits using AI coding agents. It demonstrates practical automation patterns for technical writers working in docs-as-code environments.

### Who is this for?

Technical writers and documentation teams who:

- Work in docs-as-code workflows
- Use GitHub, GitLab, or similar version control
- Want to automate repetitive documentation tasks
- Are exploring AI-assisted automation
- Have basic command line and Git knowledge

**No programming experience required!**

### Do I need to know how to code?

No! This project teaches you how to work with AI coding agents to build automation. You'll learn:

- How to document workflows (you already do this!)
- How to write clear instructions for AI (like writing documentation!)
- How to iterate based on results (like editing!)

Your technical writing skills are exactly what you need.

### What AI tools does this work with?

The example uses **Anthropic Claude** or **OpenAI GPT**, but the principles apply to:

- Cursor with Claude
- GitHub Copilot
- ChatGPT
- Any AI coding assistant

The key is the **approach**, not the specific tool.

### What version control systems are supported?

The code uses GitHub, but patterns work with:

- GitHub (implemented)
- GitLab (similar API)
- Bitbucket (similar API)
- Azure DevOps (similar API)

The same automation pattern applies—just different API calls.

## Setup Questions

### How long does setup take?

- Initial setup: 15-20 minutes
- Document your process: 30-45 minutes
- First successful run: 10 minutes
- Prompt iteration: 30-60 minutes

**Total: 2-3 hours** for complete tutorial

**Worth it?** You'll save 4-8 hours per release cycle going forward.

### What if I don't have API keys?

You can still:

1. Read through all documentation
2. Run with sample data (no API keys needed)
3. Learn the concepts and approach
4. Get API keys when ready to use with real repos

Free tier available for both Anthropic and OpenAI.

### How much do API calls cost?

**Per release notes generation:**

- GitHub API: Free (rate limited)
- AI API: $0.01 - $0.05 per run

**For typical biweekly releases:**

- **~$0.50 - $1.00 per month**

Compare to hours of manual work saved!

### Can I use this with private repositories?

Yes! Just ensure:

1. Your GitHub token has `repo` scope (not just `public_repo`)
2. You have access to the private repositories
3. Your token permissions are appropriate

The automation works the same for public or private repos.

## Usage Questions

### How accurate is the categorization?

Depends on prompt refinement:

- Initial run: 60-70%
- After iteration: 85-95%

**Remember:** 90% accuracy with 10 minutes of human review beats 100% manual work taking 90 minutes.

### What if the AI miscategorizes commits?

This is expected and normal! That's why human review is part of the workflow:

1. AI generates draft (accurate ~90%)
2. Human reviews and corrects (~10 minutes)
3. Human adds business context
4. Publish

Still **80%+ time savings** over fully manual process.

### Can I customize categories?

Yes! You can:

- Change category names
- Add new categories
- Remove categories
- Customize for different audiences

See [Prompt Engineering Reference](reference/prompt-engineering.md).

### How do I handle different release note audiences?

Create different prompt files:

- `prompts/internal_categorization.txt` - For internal team
- `prompts/external_categorization.txt` - For customers
- `prompts/technical_categorization.txt` - For developers

Use with `--prompt` flag:

```bash
python generate_release_notes.py \
  --repo owner/repo \
  --since 2024-01-01 \
  --prompt prompts/external_categorization.txt
```

### What about merge commits?

By default, merge commits are excluded unless they contain meaningful changes. You can customize this in your prompt's exclusion rules.

### Can I generate notes for specific file paths?

Not in the current version, but you could:

1. Modify the script to filter commits by path
2. Use your AI coding tool to add this feature
3. Ask: "How can I filter commits by file path?"

This is a great example of extending the automation!

## Prompt Engineering Questions

### How do I improve categorization accuracy?

Follow the iteration process in [Tutorial Step 5](tutorial/step-5-iterate-prompts.md):

1. Run with current prompt
2. Review output systematically
3. Identify patterns of errors
4. Add examples to prompt
5. Test improvements
6. Repeat until 85%+ accuracy

### What makes a good categorization prompt?

Key elements:

- ✅ Clear category definitions
- ✅ Concrete examples (positive and negative)
- ✅ Keyword indicators
- ✅ Comprehensive exclusion rules
- ✅ Decision rules for edge cases

See [Prompt Evolution Example](examples/prompt-evolution.md).

### Should I use examples from my actual commits?

Yes! The more domain-specific your examples, the better. Generic examples work OK, but examples from your actual repository work better.

### How long should my prompt be?

**Sweet spot: 500-1000 words**

- Too short (<300 words): Vague, inconsistent results
- Just right (500-1000 words): Clear, consistent, maintainable
- Too long (>1500 words): Diminishing returns, hard to maintain

Focus on quality over quantity.

### Can I use the same prompt for all repositories?

Start with one prompt, then customize per repository:

- Frontend repos might emphasize UI changes
- Backend repos might separate breaking changes
- Documentation repos have different categories

Clone and customize rather than using one prompt for all.

## Workflow Questions

### When should I run this automation?

**Recommended timing:**

- Before release (1-2 days prior)
- After all commits are merged
- When you have time to review output

**Workflow:**

1. Development team finalizes release
2. Run automation to generate draft
3. Review and refine draft (10-15 min)
4. Add business context
5. Publish

### Can I integrate this into CI/CD?

Yes! You could:

1. Run automatically on release branch
2. Create pull request with draft notes
3. Human reviews and approves
4. Publish on merge

This requires additional setup not covered in the tutorial, but ask your AI coding tool: "How can I run this in GitHub Actions?"

### What if my team uses poor commit messages?

The automation can only work with what it has. If commit messages are vague:

1. **Short term:** Add context during review
2. **Long term:** Improve commit message standards

Consider creating a commit message template or guide for your team.

### How do I handle breaking changes?

Add a custom category or marker:

```
Categories:
- New Features
- Enhancements  
- Breaking Changes  # New category
- Bug Fixes
- Documentation
```

Or mark in existing categories:

```
## Enhancements
- Update API format **(Breaking Change)** - New JSON structure
```

## Integration Questions

### Can I output in different formats?

The default is Markdown, but you can modify the script to output:

- HTML
- JSON
- Confluence wiki format
- Jira description format

Ask your AI coding tool: "How can I output release notes as HTML instead of Markdown?"

### Can this create GitHub releases automatically?

Not by default, but you could extend it:

```bash
# After generating notes, create GitHub release
gh release create v1.0.0 \
  --title "Release 1.0.0" \
  --notes-file release_notes.md
```

### Can I post results to Slack or email?

Not built-in, but you could add:

```python
# After generation, post to Slack
import requests
webhook_url = "your-slack-webhook"
requests.post(webhook_url, json={"text": notes})
```

These are great examples of extending the automation!

### Does this work with Jira or other issue trackers?

The current version focuses on Git commits, but you could:

1. Fetch Jira tickets closed in date range
2. Categorize tickets instead of commits
3. Link tickets to commits

This requires additional API integration.

## Security Questions

### Is it safe to use API keys?

Yes, if you follow best practices:

- ✅ Use `config.yaml` (in `.gitignore`)
- ✅ Use environment variables for production
- ✅ Rotate keys regularly (every 90 days)
- ✅ Use minimal scopes needed
- ❌ Never commit keys to version control
- ❌ Don't share keys in Slack/email

### What data is sent to AI providers?

Only commit messages and metadata:

- Commit message text
- Commit dates
- Author names
- Commit SHA

**Not sent:**

- Actual code changes
- File contents
- Repository code

### Can I run this without cloud AI?

The current version requires cloud AI (Anthropic or OpenAI), but you could:

1. Use local LLMs (Ollama, llama.cpp)
2. Self-hosted AI models
3. Azure OpenAI (enterprise)

This requires code modifications.

### How do I handle sensitive repositories?

For sensitive code:

1. Use self-hosted AI if available
2. Review what's sent (only commit messages)
3. Ensure commit messages don't contain secrets
4. Use fine-grained GitHub tokens with minimal access
5. Consider internal-only AI solutions

## Maintenance Questions

### Do I need to update prompts regularly?

Not usually! Once refined, prompts remain stable. Update when:

- Team's commit message style changes
- New categories needed
- Accuracy drops below 80%
- Repository patterns change

### What if the automation stops working?

Check:

1. API keys still valid (not expired)
2. GitHub token has correct permissions
3. Rate limits not exceeded
4. Dependencies up to date: `pip install --upgrade -r requirements.txt`

See [Troubleshooting Guide](troubleshooting.md).

### How do I onboard new team members?

Share:

1. This documentation site
2. Your customized prompts
3. Your documented manual process
4. Example outputs from your repository

The [Tutorial](tutorial/index.md) is designed for onboarding.

## Advanced Questions

### Can I use this for other documentation tasks?

Absolutely! The same pattern applies to:

- Translation status tracking
- Broken link checking
- Documentation quality analysis
- Automated screenshots
- API reference generation

**The approach:** Document manual process → Convert to automation prompt → Iterate

### Can I contribute improvements?

Yes! See [Contributing Guidelines](https://github.com/rebeja/docs-automation-examples/blob/main/CONTRIBUTING.md).

Ways to contribute:

- Improve documentation
- Add examples
- Fix bugs
- Share your refined prompts
- Add new features

### Where can I learn more?

**Resources:**

- [Write the Docs](https://www.writethedocs.org/)
- [Anthropic Prompt Library](https://docs.anthropic.com/claude/prompt-library)
- [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)

**Community:**

- Write the Docs Slack
- Technical Writer HQ
- r/technicalwriting

---

**Have a question not answered here?** [Open an issue](https://github.com/rebeja/docs-automation-examples/issues){ .md-button }
