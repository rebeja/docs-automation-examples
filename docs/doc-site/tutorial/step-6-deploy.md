# Step 6: Deploy

Publish your portfolio site to GitHub Pages.

## Complete these tasks

By the end of this step, you will have:

- Portfolio site live on GitHub Pages
- Custom domain configured (optional)
- Site ready to share with potential employers

## Time estimate

30-45 minutes

## Prerequisites

Before deploying, verify:

```bash
# Build succeeds without errors
mkdocs build

# Check for broken links
# Review output in site/ directory
ls -R site/
```

## Prepare your repository

### 1. Create GitHub repository

Create a new repository for your portfolio:

1. Go to [github.com/new](https://github.com/new)
2. Name: `portfolio-site` or `your-name-portfolio`
3. Description: "Technical writing portfolio showcasing software documentation samples"
4. Visibility: **Public** (required for free GitHub Pages)
5. Do not initialize with README (you have files already)
6. Click **Create repository**

### 2. Initialize Git in your project

If you used the template and already have Git initialized, skip to step 3. Otherwise:

```bash
cd my-portfolio
git init
```

### 3. Create .gitignore

Create `.gitignore` to exclude unnecessary files:

```bash
cat > .gitignore << 'EOF'
# Python
venv/
__pycache__/
*.py[cod]
*$py.class
*.so
.Python

# MkDocs
site/

# Environment
.env
.env.local

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db
EOF
```

### 4. Commit your files

```bash
git add .
git commit -m "Initial commit: Portfolio site with documentation samples"
```

### 5. Connect to GitHub repository

Replace `username` and `repository-name` with your details:

```bash
git remote add origin https://github.com/username/repository-name.git
git branch -M main
git push -u origin main
```

Enter your GitHub username and personal access token when prompted.

## Deploy to GitHub Pages

MkDocs provides a simple deployment command.

### 1. Deploy with mkdocs command

```bash
mkdocs gh-deploy
```

This command:
1. Builds your site
2. Creates or updates the `gh-pages` branch
3. Pushes built site to GitHub
4. Preserves your source files on `main` branch

Expected output:
```
INFO    - Cleaning site directory
INFO    - Building documentation to directory: site
INFO    - Documentation built in 0.52 seconds
INFO    - Copying site to gh-pages branch and pushing to GitHub
INFO    - Based on your gh-pages branch
Enumerating objects: 50, done.
INFO    - Your documentation should be available at: https://username.github.io/repository-name/
```

### 2. Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings**
3. Click **Pages** in left sidebar
4. Source should be set to: **Deploy from a branch**
5. Branch should be: **gh-pages** / **/ (root)**
6. Click **Save** if needed

### 3. Wait for deployment

GitHub Pages builds and deploys your site (usually 1-3 minutes).

Check deployment status:
1. Go to **Actions** tab in your repository
2. Look for "pages build and deployment" workflow
3. Green checkmark = deployed successfully
4. Red X = deployment failed (check logs)

### 4. Visit your live site

Your portfolio is now live at:
```
https://username.github.io/repository-name/
```

Replace with your actual GitHub username and repository name.

## Verify deployment

Check that everything works:

- [ ] Homepage loads correctly
- [ ] Navigation works
- [ ] All pages display properly
- [ ] Links work (internal and external)
- [ ] Code syntax highlighting appears
- [ ] Responsive design works on mobile

## Update your portfolio

When you make changes to your documentation:

```bash
# Edit files as needed
# Then rebuild and redeploy:
mkdocs gh-deploy
```

This single command updates your live site.

Changes appear on your site within 1-3 minutes.

## Optional: Set up custom domain

Use your own domain instead of github.io URL.

### 1. Buy a domain

Purchase a domain from:
- Namecheap
- Google Domains
- Cloudflare
- Any registrar

Recommended format: `yourname.dev` or `yourname.com`

### 2. Configure DNS

In your domain registrar DNS settings, add these records:

For apex domain (yourname.dev):
```
A    @    185.199.108.153
A    @    185.199.109.153
A    @    185.199.110.153
A    @    185.199.111.153
```

For www subdomain (www.yourname.dev):
```
CNAME    www    username.github.io
```

Replace `username` with your GitHub username.

### 3. Configure GitHub Pages

1. Go to repository **Settings** → **Pages**
2. Under "Custom domain", enter: `yourname.dev`
3. Click **Save**
4. Wait for DNS check (can take 24-48 hours)
5. Enable "Enforce HTTPS" once available

### 4. Update mkdocs.yml

Update your site URL:

```yaml
site_url: https://yourname.dev/
```

Rebuild and redeploy:

```bash
mkdocs gh-deploy
```

Your portfolio now appears at your custom domain.

## Optional: Add Google Analytics

Track portfolio visitors (useful for understanding reach).

### 1. Create Google Analytics account

1. Go to [analytics.google.com](https://analytics.google.com/)
2. Create account and property
3. Get Measurement ID (format: G-XXXXXXXXXX)

### 2. Add to mkdocs.yml

```yaml
extra:
  analytics:
    provider: google
    property: G-XXXXXXXXXX
```

Replace `G-XXXXXXXXXX` with your Measurement ID.

### 3. Redeploy

```bash
mkdocs gh-deploy
```

Analytics starts tracking after deployment.

## Optional: Add search functionality

MkDocs Material includes built-in search.

Verify it is enabled in `mkdocs.yml`:

```yaml
plugins:
  - search:
      lang: en
```

Search appears automatically in the navigation bar.

## Share your portfolio

Your portfolio is ready to share with:

### Potential employers

Include in job applications:
- Resume: Add URL in contact section
- Cover letter: Reference specific documentation samples
- Application forms: Include in portfolio URL field

### LinkedIn

Update your profile:
- Add to "Featured" section
- Include in "About" summary
- Mention in relevant posts

### Technical writing communities

Share in:
- Write the Docs Slack
- Technical writing LinkedIn groups
- Reddit r/technicalwriting
- Twitter with #TechnicalWriting hashtag

## Update and maintain

Keep your portfolio current:

### Regular updates

- Add new documentation samples quarterly
- Update about page with new skills
- Refresh examples to use current versions
- Fix any broken links or outdated content

### Continuous improvement

- Gather feedback from viewers
- Monitor analytics to see popular pages
- Improve samples based on what you learn
- Add case studies for significant projects

### Version control

Use Git effectively:

```bash
# Create feature branches for major changes
git checkout -b add-new-sample

# Make changes and commit
git add .
git commit -m "Add CLI documentation sample"

# Merge when ready
git checkout main
git merge add-new-sample

# Deploy
mkdocs gh-deploy
```

## Troubleshooting deployment

### Pages not updating

If changes do not appear:

1. Check Actions tab for deployment status
2. Clear browser cache (Ctrl+Shift+R / Cmd+Shift+R)
3. Wait 5 minutes and try again
4. Verify `gh-pages` branch was updated on GitHub

### 404 errors

If you get 404 errors:

1. Check repository is public
2. Verify GitHub Pages is enabled
3. Confirm `gh-pages` branch exists
4. Check repository name matches URL

### Build failures

If `mkdocs gh-deploy` fails:

1. Run `mkdocs build` to see specific errors
2. Fix any Markdown syntax issues
3. Verify all referenced files exist
4. Check `mkdocs.yml` for configuration errors

## Summary

You completed these tasks:

- ✓ Created GitHub repository
- ✓ Pushed portfolio source code
- ✓ Deployed to GitHub Pages
- ✓ Verified live site works
- ✓ Optionally configured custom domain
- ✓ Ready to share with employers

## What you built

You now have:

- **Live portfolio site** showcasing documentation skills
- **Multiple documentation samples** across different types
- **Case studies** explaining your process
- **Transparent AI collaboration** documentation
- **Professional presentation** suitable for job applications
- **Maintainable codebase** using docs-as-code workflow

## Next steps

Continue developing your portfolio:

1. **Add more samples** as you create documentation
2. **Gather feedback** from technical writing communities
3. **Update regularly** to show ongoing learning
4. **Apply to jobs** highlighting your portfolio
5. **Share your work** on professional networks

## Resources for continued learning

- [Write the Docs](https://www.writethedocs.org/) - Community and resources
- [MkDocs Documentation](https://www.mkdocs.org/) - Official MkDocs guides
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) - Theme documentation
- [Every Page Is Page One](http://everypageispageone.com/) - Documentation philosophy
- [Docs for Developers](https://docsfordevelopers.com/) - Developer documentation book

---

**Congratulations!** You completed the doc site portfolio tutorial.

Your portfolio demonstrates:
- Software documentation skills across multiple types
- Docs-as-code workflow proficiency
- AI collaboration capabilities
- Professional technical writing
- Modern documentation tooling

You are ready to apply for technical writing positions with a strong portfolio showcasing your skills.
