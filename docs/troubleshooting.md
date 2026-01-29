# Troubleshooting

Common issues and solutions when using the release notes automation.

## Installation Issues

### Python Command Not Found

**Problem:** `python: command not found` or `python3: command not found`

**Solutions:**

1. **Check if Python is installed:**
   ```bash
   which python3
   python3 --version
   ```

2. **Install Python:**
   - macOS: `brew install python3`
   - Ubuntu/Debian: `sudo apt-get install python3`
   - Windows: Download from [python.org](https://www.python.org/downloads/)

3. **Use full path:**
   ```bash
   /usr/bin/python3 generate_release_notes.py --help
   ```

### Virtual Environment Activation Fails

**Problem (Windows):** `cannot be loaded because running scripts is disabled`

**Solution:**
```powershell
# Run PowerShell as Administrator
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Problem (macOS/Linux):** `source: command not found`

**Solution:**
```bash
# Use the correct shell activation
source venv/bin/activate  # bash/zsh
. venv/bin/activate       # alternative
```

### Module Import Errors

**Problem:** `ModuleNotFoundError: No module named 'anthropic'`

**Checklist:**

1. **Verify virtual environment is activated:**
   ```bash
   which python
   # Should show path ending in /venv/bin/python
   ```

2. **Reinstall dependencies:**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

3. **Check Python version:**
   ```bash
   python --version  # Must be 3.8+
   ```

4. **Verify installation:**
   ```bash
   pip list | grep anthropic
   ```

## Configuration Issues

### Invalid API Key

**Problem:** `401 Unauthorized` or `Invalid API key`

**Solutions:**

1. **Check for extra spaces:**
   ```bash
   # Bad: "sk-ant-123 " (trailing space)
   # Good: "sk-ant-123"
   ```

2. **Verify correct provider:**
   ```yaml
   # Make sure this matches your key type
   ai_provider: "anthropic"  # for sk-ant-* keys
   ai_provider: "openai"     # for sk-* keys (OpenAI)
   ```

3. **Check key is active:**
   - Log into your AI provider console
   - Verify key hasn't been revoked
   - Check billing is set up (after free tier)

4. **Regenerate key:**
   - Create a new API key
   - Update `config.yaml`
   - Try again

### GitHub Authentication Failed

**Problem:** `Bad credentials` or `401` when accessing GitHub

**Solutions:**

1. **Verify token format:**
   ```yaml
   github_token: "ghp_xxxxxxxxxxxx"  # Classic token
   github_token: "github_pat_xxxxx"  # Fine-grained token
   ```

2. **Check token scopes:**
   - For private repos: Need `repo` scope
   - For public repos: Need `public_repo` scope
   - Go to [github.com/settings/tokens](https://github.com/settings/tokens) to verify

3. **Token expiration:**
   - Check if token has expired
   - Generate new token if needed

4. **Repository access:**
   ```bash
   # Test access
   curl -H "Authorization: token YOUR_TOKEN" \
     https://api.github.com/repos/OWNER/REPO
   ```

### Configuration File Not Found

**Problem:** `FileNotFoundError: ../config.yaml`

**Solutions:**

1. **Check current directory:**
   ```bash
   pwd  # Should be in 01-release-notes-automation/
   ls ../config.yaml  # Should exist
   ```

2. **Create from example:**
   ```bash
   cd ..  # Go to repository root
   cp config.example.yaml config.yaml
   ```

3. **Use explicit path:**
   ```bash
   python generate_release_notes.py \
     --config /full/path/to/config.yaml \
     --repo owner/repo \
     --since 2024-01-01
   ```

## Runtime Issues

### No Commits Found

**Problem:** `Found 0 commits` even though commits exist

**Solutions:**

1. **Check date range:**
   ```bash
   # Make sure date is in the past
   --since 2024-01-01
   
   # Not future dates
   --since 2025-12-31  # ❌ Won't find anything
   ```

2. **Verify repository access:**
   ```bash
   # Can you access the repo?
   python -c "
   from github import Github
   import yaml
   config = yaml.safe_load(open('config.yaml'))
   g = Github(config['github_token'])
   repo = g.get_repo('owner/repo')
   print(f'Repo: {repo.name}')
   print(f'Commits: {repo.get_commits().totalCount}')
   "
   ```

3. **Check repository name:**
   ```bash
   # Correct format
   --repo octocat/Hello-World  # ✅ owner/repo
   
   # Incorrect formats
   --repo Hello-World          # ❌ Missing owner
   --repo github.com/octocat/Hello-World  # ❌ Include domain
   ```

4. **Private repository:**
   - Verify token has `repo` scope
   - Verify you have access to the repository

### Rate Limit Exceeded

**Problem:** `API rate limit exceeded`

**GitHub Rate Limits:**

- Authenticated: 5,000 requests/hour
- Unauthenticated: 60 requests/hour

**Solutions:**

1. **Wait for reset:**
   ```bash
   # Check when rate limit resets
   python -c "
   from github import Github
   import yaml
   config = yaml.safe_load(open('config.yaml'))
   g = Github(config['github_token'])
   rate = g.get_rate_limit()
   print(f'Remaining: {rate.core.remaining}')
   print(f'Resets at: {rate.core.reset}')
   "
   ```

2. **Reduce date range:**
   ```bash
   # Instead of --since 2023-01-01 (lots of commits)
   # Try --since 2024-01-01 (fewer commits)
   ```

3. **Use caching:**
   - Script should cache commits between runs
   - Implemented in improved version

**AI Provider Rate Limits:**

Check your provider's documentation:

- Anthropic: [docs.anthropic.com/rate-limits](https://docs.anthropic.com/)
- OpenAI: [platform.openai.com/docs/guides/rate-limits](https://platform.openai.com/)

### AI Categorization Errors

**Problem:** Commits consistently miscategorized

**Solutions:**

1. **Review prompt quality:**
   - Are examples clear?
   - Are definitions specific enough?
   - Are exclusions comprehensive?

2. **Test with smaller set:**
   ```bash
   # Use date range with fewer commits to iterate faster
   --since 2024-01-20 --until 2024-01-25
   ```

3. **Check commit message quality:**
   ```bash
   # Poor: "fix bug"
   # Good: "Fix memory leak in parser"
   ```
   - AI can only categorize based on commit message
   - Bad commit messages → bad categorization

4. **Iterate on prompt:**
   - See [Prompt Evolution](examples/prompt-evolution.md)
   - Add specific examples from your repository
   - Follow [Tutorial Step 5](tutorial/step-5-iterate-prompts.md)

### Output File Permission Denied

**Problem:** `PermissionError: [Errno 13] Permission denied: 'release_notes.md'`

**Solutions:**

1. **Check if file is open:**
   - Close file in your text editor
   - Try again

2. **Check file permissions:**
   ```bash
   ls -l release_notes.md
   chmod 644 release_notes.md
   ```

3. **Use different output file:**
   ```bash
   --output release_notes_new.md
   ```

## Output Quality Issues

### Internal Changes Appearing

**Problem:** CI/CD, test, or internal changes in output

**Solution:** Refine exclusion rules in prompt

```
Exclusions:
- Commits containing: "internal", "ci:", "test:"
- Commits from paths: /tests/, /.github/
- By author: dependabot[bot]
```

See [Prompt Engineering Reference](reference/prompt-engineering.md)

### Features vs Enhancements Confused

**Problem:** Improvements categorized as features

**Solution:** Add clearer examples in prompt

```
New Features: "Add" + "wholly new capability"
Examples: "Add user authentication" ✅
Not: "Add performance improvement" ❌ (enhancement)

Enhancements: "Improve", "Update", "Optimize"
Examples: "Improve search performance" ✅
```

### Missing Contextual Information

**Problem:** Output is accurate but lacks business context

**Solution:** This is expected!

The automation provides accurate categorization. Human review adds:

- Business value explanations
- Links to documentation
- Context for non-technical readers
- Emphasis on important changes

**Time savings still significant:** 90 minutes → 15 minutes

## Performance Issues

### Script Runs Very Slowly

**Problem:** Takes >5 minutes for small repository

**Checklist:**

1. **Check internet connection**
2. **Verify API provider status**
   - Anthropic: [status.anthropic.com](https://status.anthropic.com/)
   - OpenAI: [status.openai.com](https://status.openai.com/)
   - GitHub: [githubstatus.com](https://www.githubstatus.com/)

3. **Reduce commit count:**
   ```bash
   # Narrow date range
   --since 2024-01-20 --until 2024-01-31
   ```

4. **Check rate limiting:**
   - May be throttled by provider
   - Wait and retry

### High AI API Costs

**Problem:** Unexpectedly high API bills

**Solutions:**

1. **Check model selection:**
   ```yaml
   # More expensive
   model: "claude-3-opus-20240229"    # $$$$
   model: "gpt-4"                     # $$$
   
   # Cost-effective
   model: "claude-3-sonnet-20240229"  # $$
   model: "gpt-3.5-turbo"             # $
   ```

2. **Batch requests:**
   - Process multiple releases at once
   - Don't run for every commit

3. **Set budget alerts:**
   - Anthropic: Console → Billing → Budget Alerts
   - OpenAI: Console → Usage → Limits

## Getting Help

If you're still stuck:

### 1. Check Documentation

- [FAQ](faq.md) - Common questions
- [Tutorial](tutorial/index.md) - Step-by-step guide
- [Examples](examples/prompt-evolution.md) - Real-world cases

### 2. Review Error Messages

Enable verbose output:

```bash
python generate_release_notes.py \
  --repo owner/repo \
  --since 2024-01-01 \
  --verbose  # Add if available
```

### 3. Search Issues

Check if others have encountered this:

- [GitHub Issues](https://github.com/rebeja/docs-automation-examples/issues)

### 4. Ask for Help

Create a new issue with:

- Error message (full text)
- Steps to reproduce
- Your environment (OS, Python version)
- Relevant configuration (with API keys removed!)

**DO NOT share:**

- API keys
- GitHub tokens  
- Private repository details

---

**Still having issues?** [Open an issue](https://github.com/rebeja/docs-automation-examples/issues){ .md-button }
