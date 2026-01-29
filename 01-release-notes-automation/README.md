# Release Notes Automation

Automate release notes generation from GitHub commits using AI categorization.

**Part of the Doc360Talk webinar:** _"From Writer to Tool Builder: AI Coding Agents for Technical Documentation"_

---

## 📚 Full Documentation

**👉 [View Complete Documentation →](https://rebeja.github.io/docs-automation-examples/)**

This README provides quick reference. For the complete tutorial, troubleshooting, examples, and detailed guides, visit the documentation site.

---

## The Problem

Manually reviewing commits and creating release notes takes significant time:

- ⏱️ **4-8 hours per release** - Reviewing each commit individually
- 🔍 **Easy to miss changes** - Important updates buried in commit history
- 📝 **Inconsistent categorization** - Different reviewers categorize differently
- 🔄 **Repetitive work** - Same process every release cycle

## The Solution

AI-powered automation that:

1. ✅ Fetches commits from GitHub API
2. ✅ Categorizes using your documented standards
3. ✅ Generates formatted markdown draft
4. ✅ Human reviews and adds context (10-15 minutes)

**Result:** 86% time reduction while maintaining quality

## How It Works

```
GitHub API → Fetch Commits → Filter → AI Categorization → Draft → Human Review → Publish
                                      ↑
                              Your Standards
                              (via prompt)
```

## Prerequisites

- **Python 3.8+** - Check: `python --version`
- **GitHub API token** - [Get one here](https://github.com/settings/tokens)
- **AI API key** - [Anthropic](https://console.anthropic.com/) or [OpenAI](https://platform.openai.com/)
- **Command line basics** - Ability to run terminal commands

**No programming experience required!**

## Quick Start

### 1. Set Up Environment

```bash
# From repository root
cd docs-automation-examples

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure API Keys

```bash
# Copy example configuration
cp config.example.yaml config.yaml

# Edit config.yaml with your API keys
# - ai_api_key: Get from console.anthropic.com or platform.openai.com
# - github_token: Get from github.com/settings/tokens
```

### 3. Test with Sample Data

```bash
cd 01-release-notes-automation

# Run with built-in sample commits (no API calls)
python generate_release_notes.py \
  --repo sample/repo \
  --since 2024-01-01 \
  --sample

# Review output
cat release_notes.md
```

### 4. Run with Real Repository

```bash
# Generate release notes from actual commits
python generate_release_notes.py \
  --repo octocat/Hello-World \
  --since 2024-01-01

# Review and refine
cat release_notes.md
```

**📖 [Complete setup guide →](https://rebeja.github.io/docs-automation-examples/tutorial/step-1-setup/)**

## Usage

### Command Line Options

```bash
python generate_release_notes.py [OPTIONS]

Required:
  --since DATE          Start date (YYYY-MM-DD)

Optional:
  --repo OWNER/REPO     Repository (or set default_repo in config.yaml)
  --until DATE          End date (defaults to today)
  --output FILE         Output file (default: release_notes.md)
  --prompt FILE         Custom prompt file (default: prompts/categorization_prompt.txt)
  --sample              Use sample data (no API calls)
  --config FILE         Config file path (default: ../config.yaml)
```

### Examples

**Test with sample data (no API keys needed):**
```bash
python generate_release_notes.py --since 2024-01-01 --sample
```

**Generate for specific repository:**
```bash
python generate_release_notes.py \
  --repo your-username/your-repo \
  --since 2024-01-01
```

**Custom date range:**
```bash
python generate_release_notes.py \
  --repo owner/repo \
  --since 2024-01-01 \
  --until 2024-01-31
```

**Use custom prompt:**
```bash
python generate_release_notes.py \
  --repo owner/repo \
  --since 2024-01-01 \
  --prompt prompts/external_categorization.txt
```

## Customization

### Refine Your Prompt

The categorization prompt is key to quality output. Iterate based on results:

**📖 [Complete prompt engineering guide →](https://rebeja.github.io/docs-automation-examples/tutorial/step-5-iterate-prompts/)**

**Quick tips:**

1. **Add specific examples** from your repository
2. **Define clear exclusion rules** for internal changes
3. **Specify keyword indicators** for each category
4. **Test and measure** improvement in accuracy

See the **[Prompt Evolution Example](https://rebeja.github.io/docs-automation-examples/examples/prompt-evolution/)** showing improvement from 65% to 91% accuracy.

### Create Audience-Specific Versions

```bash
# Internal release notes (more technical, include infrastructure)
--prompt prompts/internal_categorization.txt

# External release notes (customer-focused, strict filtering)
--prompt prompts/external_categorization.txt
```

## Expected Results

### Accuracy Metrics

| Stage | Accuracy | Time | Notes |
|-------|----------|------|-------|
| Initial run (v1 prompt) | 65-70% | 45 min review | Needs significant refinement |
| After iteration (v3) | 85-90% | 15 min review | Production ready |
| Optimized (v4) | 90-95% | 10 min review | Excellent |

### Output Quality

**Generated draft includes:**

- ✅ Accurate categorization (85%+ after iteration)
- ✅ Consistent markdown formatting
- ✅ Commit links for verification
- ✅ Emoji icons for visual scanning

**Human review adds:**

- Business context and impact
- Links to documentation
- Audience-appropriate language
- Final quality check

## Common Issues

### AI Miscategorizes Some Commits

**This is normal!** Expected accuracy is 85-95%, not 100%.

**Solution:** Refine your prompt with more specific examples. See [Tutorial Step 5](https://rebeja.github.io/docs-automation-examples/tutorial/step-5-iterate-prompts/).

### Internal Changes Appear in Output

**Cause:** Exclusion rules not specific enough

**Solution:** Add comprehensive exclusions:
```
- Commits containing: "internal", "ci:", "test:"
- From paths: /tests/, /.github/
- By author: dependabot[bot]
```

### Rate Limit Errors

**GitHub:** 5,000 requests/hour (authenticated)  
**AI Provider:** Check your plan limits

**Solution:** Reduce date range or wait for limit reset

**📖 [Full troubleshooting guide →](https://rebeja.github.io/docs-automation-examples/troubleshooting/)**

## Next Steps

After completing this starter:

1. **📖 [Follow the complete tutorial](https://rebeja.github.io/docs-automation-examples/tutorial/)** - 2-3 hours to full proficiency
2. **🔄 Iterate on your prompt** - Refine for your repository patterns
3. **📊 Track metrics** - Measure time savings and accuracy
4. **🚀 Integrate into workflow** - Use for your next release
5. **🤝 Share learnings** - Help others in the Write the Docs community

---

**Questions?** Check the **[FAQ](https://rebeja.github.io/docs-automation-examples/faq/)** or **[open an issue](https://github.com/rebeja/docs-automation-examples/issues)**.
