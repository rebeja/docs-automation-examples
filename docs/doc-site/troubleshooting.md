# Troubleshooting

Common issues and solutions when building portfolio documentation sites.

## Setup issues

### Python command not found

Problem: `python: command not found` or `python3: command not found`

Solutions:

1. Check if Python is installed:
   ```bash
   which python3
   python3 --version
   ```

2. Install Python:
   - macOS: `brew install python3`
   - Ubuntu or Debian: `sudo apt-get install python3`
   - Windows: Download from [python.org](https://www.python.org/downloads/)

3. Use full path:
   ```bash
   /usr/bin/python3 -m pip install mkdocs
   ```

### Virtual environment activation fails

Problem (Windows): `cannot be loaded because running scripts is disabled`

Solution:
```powershell
# Run PowerShell as Administrator
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Problem (macOS or Linux): `source: command not found`

Solution:
```bash
# Use correct shell activation
source venv/bin/activate  # bash or zsh
. venv/bin/activate       # alternative
```

### MkDocs not found after installation

Problem: `mkdocs: command not found` after `pip install mkdocs`

Solutions:

1. Verify virtual environment is activated:
   ```bash
   which python
   # Should show path ending in /venv/bin/python
   ```

2. Reinstall in active environment:
   ```bash
   pip install --upgrade pip
   pip install mkdocs mkdocs-material
   ```

3. Check Python scripts directory in PATH:
   ```bash
   echo $PATH | grep venv
   ```

### Material theme not loading

Problem: Site displays but theme does not apply

Solutions:

1. Verify Material is installed:
   ```bash
   pip list | grep mkdocs-material
   ```

2. Check `mkdocs.yml` theme configuration:
   ```yaml
   theme:
     name: material  # Must be exactly "material"
   ```

3. Reinstall Material theme:
   ```bash
   pip uninstall mkdocs-material
   pip install mkdocs-material
   ```

4. Clear MkDocs build cache:
   ```bash
   rm -rf site/
   mkdocs build
   ```

## MkDocs server issues

### Port already in use

Problem: `[Errno 48] Address already in use`

Solutions:

1. Kill existing MkDocs processes:
   ```bash
   # macOS or Linux
   pkill -f mkdocs
   
   # Windows
   taskkill /F /IM python.exe
   ```

2. Use different port:
   ```bash
   mkdocs serve -a localhost:8001
   ```

3. Find and kill process using port:
   ```bash
   # macOS or Linux
   lsof -ti:8000 | xargs kill -9
   
   # Windows
   netstat -ano | findstr :8000
   taskkill /PID <process_id> /F
   ```

### Changes not appearing in browser

Problem: Edits not reflected when viewing local site

Solutions:

1. Force refresh browser:
   - Chrome or Firefox: `Ctrl+Shift+R` (Windows or Linux)
   - Chrome or Firefox: `Cmd+Shift+R` (macOS)
   - Safari: `Cmd+Option+R`

2. Restart MkDocs server:
   ```bash
   # Stop with Ctrl+C
   mkdocs serve
   ```

3. Clear browser cache completely

4. Check file was actually saved in editor

### Build errors in terminal

Problem: `mkdocs build` or `mkdocs serve` shows errors

Common causes and solutions:

Broken link error:
```
WARNING - Doc file 'page.md' contains a link to 'other.md', 
          but the target 'other.md' is not found
```
Solution: Fix the link or create the missing file

YAML syntax error:
```
ERROR   - Config file 'mkdocs.yml' is invalid.
          Error: ...
```
Solution: Check YAML indentation and syntax. Use YAML validator.

Markdown parsing error:
```
ERROR   - Error reading page 'file.md'
```
Solution: Check for invalid Markdown syntax in the file

## GitHub Pages deployment issues

### gh-deploy command fails

Problem: `mkdocs gh-deploy` shows errors

Solutions:

1. Verify Git repository is initialized:
   ```bash
   git status
   # Should show "On branch main"
   ```

2. Check remote is configured:
   ```bash
   git remote -v
   # Should show origin with GitHub URL
   ```

3. Verify credentials:
   ```bash
   git config user.name
   git config user.email
   ```

4. Push access issues:
   - Use personal access token instead of password
   - Check repository permissions
   - Verify you own the repository

### Site not updating after deployment

Problem: Changes deployed but site shows old content

Solutions:

1. Wait 2-3 minutes for GitHub Pages to rebuild

2. Force refresh browser (clear cache):
   - `Ctrl+Shift+R` or `Cmd+Shift+R`

3. Check GitHub Actions:
   - Go to repository **Actions** tab
   - Look for "pages build and deployment" workflow
   - Check for errors

4. Verify `gh-pages` branch updated:
   - Go to repository on GitHub
   - Switch to `gh-pages` branch
   - Check commit timestamp

5. Clear DNS cache:
   ```bash
   # macOS
   sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder
   
   # Windows
   ipconfig /flushdns
   
   # Linux
   sudo systemd-resolve --flush-caches
   ```

### 404 error on GitHub Pages

Problem: Site shows "404 There is not a GitHub Pages site here."

Solutions:

1. Verify repository is public:
   - Go to repository **Settings**
   - Check visibility under "Danger Zone"
   - Change to Public if needed

2. Check GitHub Pages settings:
   - Go to **Settings** → **Pages**
   - Source should be "Deploy from a branch"
   - Branch should be `gh-pages` / `/ (root)`
   - Click Save

3. Verify `gh-pages` branch exists:
   ```bash
   git branch -a
   # Should list remotes/origin/gh-pages
   ```

4. Run deployment again:
   ```bash
   mkdocs gh-deploy --force
   ```

### Custom domain not working

Problem: Custom domain shows error or does not connect

Solutions:

1. Wait for DNS propagation (24-48 hours after setup)

2. Check DNS configuration:
   ```bash
   dig yourname.dev
   # Should show GitHub Pages IP addresses
   ```

3. Verify GitHub Pages custom domain setting:
   - Go to **Settings** → **Pages**
   - Custom domain field shows your domain
   - "Enforce HTTPS" should be enabled

4. Check domain registrar settings:
   - A records point to GitHub Pages IPs
   - CNAME record for www points to username.github.io

5. Remove and re-add custom domain:
   - Delete custom domain in GitHub settings
   - Wait 5 minutes
   - Add it back and save

## AI and API issues

### API rate limit exceeded

Problem: AI provider shows rate limit errors

Solutions:

1. Wait for rate limit to reset:
   - Check provider dashboard for reset time
   - Anthropic and OpenAI show limits in console

2. Reduce frequency of requests:
   - Generate content section by section
   - Save prompts and reuse outputs
   - Use smaller content chunks

3. Upgrade to paid tier:
   - Free tiers have strict rate limits
   - Paid tiers offer higher limits

### Invalid API key error

Problem: `401 Unauthorized` or `Invalid API key`

Solutions:

1. Check for extra spaces:
   ```bash
   # Bad: "sk-ant-123 " (trailing space)
   # Good: "sk-ant-123"
   ```

2. Verify correct provider:
   - Anthropic keys start with `sk-ant-`
   - OpenAI keys start with `sk-`

3. Check key is active:
   - Log into provider console
   - Verify key has not been revoked
   - Check billing is set up

4. Regenerate key:
   - Create new API key
   - Update your `.env` file
   - Try again

### AI generates incorrect technical information

Problem: AI output contains technical errors

Solutions:

This is expected behavior. Always:

1. Verify technical accuracy manually
2. Test all code examples
3. Check API specifications
4. Research unfamiliar concepts
5. Consult official documentation

AI is a drafting tool requiring human verification.

### AI output too generic or vague

Problem: Generated content lacks specific details

Solutions:

1. Provide more detailed prompts:
   - Include specific technical requirements
   - Give concrete examples
   - Specify exact format needed

2. Generate section by section:
   - Break documentation into smaller pieces
   - Provide detailed context for each section

3. Add specifics manually:
   - Use AI for structure
   - Add technical details yourself
   - Incorporate domain knowledge

## Content and writing issues

### Documentation reads as AI-generated

Problem: Content feels generic or lacks authentic voice

Solutions:

1. Edit heavily for voice:
   - Remove generic phrases
   - Add specific examples
   - Include personality
   - Use authentic language

2. Add domain expertise:
   - Include insider knowledge
   - Reference real-world scenarios
   - Explain trade-offs
   - Share experiences

3. Review and rewrite:
   - Use AI as first draft only
   - Rewrite in your own voice
   - Add unique perspective

### Code examples do not work

Problem: Code samples generate errors

Solutions:

1. Test all examples:
   - Run every code sample
   - Fix syntax errors
   - Verify imports
   - Check versions

2. Include necessary context:
   ```python
   # Add all required imports
   import requests
   
   # Show complete working example
   response = requests.get('https://api.example.com')
   ```

3. Add error handling:
   ```python
   try:
       response = requests.get('https://api.example.com')
       response.raise_for_status()
   except requests.exceptions.RequestException as e:
       print(f"Error: {e}")
   ```

### Navigation structure confusing

Problem: Site organization unclear or illogical

Solutions:

1. Review information architecture:
   - Group related content
   - Use clear categories
   - Limit nesting depth (3 levels maximum)

2. Test with fresh eyes:
   - Ask someone to review
   - Observe where they get confused
   - Simplify structure

3. Add navigation aids:
   - Breadcrumbs (enabled by default in Material)
   - Cross-references between pages
   - Clear page titles

### Markdown formatting broken

Problem: Content does not display correctly

Common issues:

Headings not rendering:
```markdown
# Bad: #No space after hash
# Good: # Space after hash
```

Lists not formatting:
```markdown
Bad:
-No space after dash
- Inconsistent indentation
  - Two spaces
    - Four spaces

Good:
- Space after dash
- Consistent indentation
  - Two spaces for nesting
    - Two more spaces
```

Code blocks not highlighting:
````markdown
Bad:
```
code without language
```

Good:
```python
code with language specified
```
````

Links not working:
```markdown
Bad: [Link](page.md)  # Wrong extension
Good: [Link](page.md)  # Use .md not .html
```

## Performance and optimization issues

### Site builds slowly

Problem: `mkdocs build` takes long time

Solutions:

1. Remove large files from docs:
   - Move images to external hosting
   - Compress images before including
   - Limit PDF file sizes

2. Simplify navigation:
   - Reduce number of pages
   - Flatten deep nesting
   - Remove unused plugins

3. Use `.gitignore` to exclude build artifacts:
   ```
   site/
   __pycache__/
   ```

### Site loads slowly

Problem: Pages take long time to display

Solutions:

1. Optimize images:
   - Compress images (use TinyPNG, ImageOptim)
   - Use appropriate formats (WebP for modern browsers)
   - Limit image dimensions

2. Minimize custom CSS:
   - Remove unused styles
   - Avoid large font files
   - Use system fonts

3. Enable Material theme optimization:
   ```yaml
   theme:
     name: material
     features:
       - navigation.instant  # Faster page loading
   ```

## Get help

If you are still stuck:

### 1. Check documentation

- [MkDocs documentation](https://www.mkdocs.org/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [GitHub Pages documentation](https://docs.github.com/en/pages)

### 2. Search for similar issues

- [MkDocs GitHub issues](https://github.com/mkdocs/mkdocs/issues)
- [Material GitHub issues](https://github.com/squidfunk/mkdocs-material/issues)
- Stack Overflow with `mkdocs` tag

### 3. Ask for help

Create new issue with:

- Error message (full text)
- Steps to reproduce
- Your environment (OS, Python version, MkDocs version)
- Relevant configuration (with sensitive data removed)

Do not share:
- API keys
- Personal access tokens
- Private repository details

---

[Open an issue](https://github.com/rebeja/docs-automation-examples/issues) if you encounter problems not covered here.
