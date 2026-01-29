# Frequently asked questions

Common questions about building technical writing portfolio sites with AI collaboration.

## General questions

### Do I need existing documentation samples to build a portfolio?

No. This tutorial teaches you how to create portfolio samples from scratch using three approaches:

- Document open source tools you already use
- Create documentation for realistic fictional products
- Document your own projects or scripts

You can build a complete portfolio without any prior documentation work.

### How much does this cost?

Costs breakdown:

- MkDocs and Material theme: Free (open source)
- GitHub account: Free
- GitHub Pages hosting: Free for public repositories
- Domain name: $10-15 per year (optional)
- AI API access: $5-20 per month depending on usage

Total minimum cost: $0 (free tier AI credits usually sufficient)

### How long does it take to build a portfolio site?

Time estimates:

- Initial setup: 30 minutes
- Creating 3-5 documentation samples: 4-6 hours
- Refinement and polish: 1-2 hours
- Deployment: 30 minutes

Total: 6-9 hours spread over 1-2 weeks

You can start with 2-3 samples and add more over time.

### Can I use this portfolio for job applications?

Yes. This portfolio is designed specifically for job applications. It demonstrates:

- Software documentation skills
- Docs-as-code workflow knowledge
- Modern tooling proficiency (Git, Markdown, MkDocs)
- AI collaboration capabilities
- Professional presentation

Include the URL on your resume and in job applications.

### Do I need to disclose that I used AI?

Yes, transparency is important. The tutorial includes case studies that document:

- Which AI tool you used
- What percentage was AI-generated versus human-created
- What you verified manually
- How you improved AI output

This demonstrates honesty and shows you understand AI's role as a tool, not a replacement for human expertise.

### What if I do not have technical writing experience?

This portfolio demonstrates your capabilities regardless of job history. Focus on:

- Creating high-quality documentation samples
- Following professional standards
- Demonstrating technical accuracy
- Showing learning and growth

Entry-level positions value demonstrated skills over years of experience.

### Can I include documentation from my current job?

Check your employment agreement first. Many companies consider documentation proprietary. Safer approaches:

- Create similar documentation for fictional products
- Document open source alternatives
- Focus on different domains than your current work
- Get explicit written permission if including actual work

When in doubt, create new samples.

## AI and automation questions

### Which AI provider should I use?

Both Anthropic Claude and OpenAI GPT work well:

Anthropic Claude:
- Strengths: Technical accuracy, following instructions precisely
- Pricing: $15-20 per month for regular use
- Best for: API documentation, technical explanations

OpenAI GPT:
- Strengths: Creative writing, conversational tone
- Pricing: $20 per month (ChatGPT Plus) or pay-per-use API
- Best for: Tutorials, getting started guides

Recommendation: Start with whichever you have access to. You can create excellent documentation with either.

### How much of my portfolio should be AI-generated?

Recommended balance:

- AI-generated initial drafts: 40-60%
- Human verification and editing: 40-60%

AI handles:
- Initial content structure
- Standard explanations
- Example code patterns
- Consistent formatting

Humans must provide:
- Technical accuracy verification
- Information architecture
- Final editing and polish
- Real-world context

### Will employers care that I used AI?

Forward-thinking employers value AI skills. Demonstrating effective AI collaboration shows:

- Modern workflow understanding
- Efficiency and productivity
- Critical thinking (knowing what to verify)
- Adaptability to new tools

Be transparent about your process. The case studies show your methodology.

### What if AI generates incorrect technical information?

This is why human oversight is critical. Always:

1. Verify technical accuracy of AI output
2. Test all code examples
3. Check API specifications
4. Research unfamiliar concepts
5. Consult official documentation

AI is a drafting tool, not a replacement for technical knowledge.

### Can I use AI for everything?

AI works best for:
- Initial content generation
- Editing and refinement
- Example code patterns
- Consistent formatting

AI struggles with:
- Technical accuracy (requires verification)
- Domain-specific knowledge
- Realistic examples with correct details
- Understanding user context

Balance AI assistance with human expertise.

## Technical questions

### Do I need to know how to code?

Basic familiarity helps but is not required:

Must know:
- Markdown formatting basics
- Command line basics (navigate directories, run commands)
- Git basics (commit, push)

Nice to have:
- Python basics (for understanding MkDocs)
- HTML/CSS basics (for customization)
- YAML basics (for configuration)

The tutorial teaches what you need to know.

### What if I want to use a different static site generator?

MkDocs is recommended because:
- Designed specifically for documentation
- Simple configuration
- Excellent Material theme
- Easy deployment

Alternatives that work:
- Hugo (faster, more complex)
- Docusaurus (React-based, feature-rich)
- Sphinx (Python ecosystem standard)

Choose MkDocs for simplicity and documentation focus.

### Can I customize the theme?

Yes. Material for MkDocs supports extensive customization without requiring custom code:

**Basic customization** (no code required):
- Color schemes (light and dark mode)
- Primary and accent colors
- Fonts (text and code)
- Logo and favicon
- Navigation features
- Social links

**Advanced customization**:
- Custom CSS
- Custom templates
- JavaScript enhancements
- Homepage layouts

**Quick example** - Change colors:
```yaml
theme:
  name: material
  palette:
    primary: teal
    accent: green
```

See [Theme customization reference](reference/theme-customization.md) for complete guide.

### How do I add a resume or PDF?

Create a `files/` directory and add your resume:

```bash
mkdir docs/files
cp ~/Documents/resume.pdf docs/files/
```

Link from your about page:

```markdown
[Download my resume (PDF)](files/resume.pdf)
```

The file deploys with your site.

### Can I use my own domain?

Yes. Custom domains cost $10-15 per year. Steps:

1. Purchase domain from registrar (Namecheap, Google Domains, etc.)
2. Configure DNS settings (detailed in [Step 6](tutorial/step-6-deploy.md))
3. Add domain to GitHub Pages settings
4. Update `site_url` in `mkdocs.yml`

Your portfolio appears at `yourname.dev` instead of `username.github.io`.

### How do I update my portfolio after deploying?

Simple workflow:

```bash
# Edit files locally
# Test with: mkdocs serve

# Deploy changes
mkdocs gh-deploy
```

Changes appear live within 1-3 minutes.

### What if my site does not deploy?

Common issues:

- Repository must be public (free GitHub Pages requires public repos)
- GitHub Pages must be enabled in settings
- `gh-pages` branch must exist (created by `mkdocs gh-deploy`)
- No build errors (test with `mkdocs build`)

See [Troubleshooting guide](troubleshooting.md) for detailed solutions.

## Content questions

### What documentation types should I include?

Include variety to demonstrate range:

Minimum (3 types):
- API reference
- Getting started guide  
- One of: CLI reference, troubleshooting, or how-to

Recommended (5 types):
- API reference
- Getting started guide
- CLI reference
- Troubleshooting guide
- Conceptual guide or how-to

This shows versatility across documentation types.

### How detailed should my documentation samples be?

Aim for realistic but focused samples:

- API reference: 3-5 endpoints fully documented
- Getting started: Complete first-time user experience
- CLI reference: 5-8 commands with examples
- Tutorial: 30-45 minute learning experience
- Troubleshooting: 5-8 common problems

Quality over quantity. Three excellent samples beat five mediocre ones.

### Should I create documentation for real or fictional products?

Both approaches work:

Fictional products:
- Advantages: Complete control, no conflicts
- Disadvantages: Must be convincingly realistic
- Best for: Demonstrating structure and style

Open source tools:
- Advantages: Real technical depth, verifiable
- Disadvantages: May duplicate existing docs
- Best for: Demonstrating research and accuracy

Recommendation: Mix both approaches for variety.

### How technical should my writing be?

Match your target audience:

For developer tools:
- Use technical terminology correctly
- Include code examples
- Assume technical background
- Be precise and accurate

For broader audiences:
- Explain technical concepts clearly
- Provide context
- Use analogies when helpful
- Define jargon

Know your audience and write for them.

### What if my documentation has errors?

Some errors are acceptable in portfolio samples if:

- You note them in case studies
- They demonstrate learning
- You explain what you would improve
- Technical accuracy is still strong

Perfect documentation is less important than demonstrating good process and judgment.

### How do I write case studies?

Follow the template in [Step 4](tutorial/step-4-write-content.md). Include:

- Project context and goals
- Research and planning process
- AI collaboration details
- Challenges and solutions
- Skills demonstrated
- What you learned

Case studies show your process and thinking, not just final output.

### Should I include screenshots?

Use screenshots strategically:

Good uses:
- UI documentation requiring visual reference
- Before and after comparisons
- Complex interface explanations

Avoid:
- API documentation (text is better)
- CLI tools (code blocks are clearer)
- Overuse (slows page loading)

Use screenshots when they add value beyond text.

## Career and job search questions

### How do I share my portfolio with employers?

Multiple channels:

- Resume: Include URL in header or contact section
- LinkedIn: Add to Featured section and About summary
- Cover letters: Reference specific samples
- Job applications: Include in portfolio URL field
- Email: Link when reaching out to recruiters

Make it easy to find and access.

### What should I say about my portfolio in interviews?

Prepare to discuss:

- Why you chose specific documentation types
- Your process for creating samples
- How you collaborated with AI
- Technical accuracy verification methods
- What you learned building the portfolio
- How you would approach documentation for their product

Treat portfolio as conversation starter, not just work samples.

### Can this portfolio help me get my first technical writing job?

Yes. Entry-level positions value:

- Demonstrated skills over years of experience
- Modern tooling knowledge
- Learning ability
- Professional presentation

A strong portfolio compensates for limited job history.

### How often should I update my portfolio?

Recommended frequency:

- Add new sample: Quarterly
- Update about page: Every 6 months
- Refresh examples: Annually
- Fix issues: As discovered

Active maintenance shows ongoing learning.

### What if I get feedback that my documentation needs improvement?

Use feedback to improve:

1. Thank the reviewer
2. Ask specific questions
3. Implement suggested changes
4. Document improvements in case studies
5. Show growth over time

Portfolios demonstrate learning, not perfection.

---

Still have questions? [Open an issue](https://github.com/rebeja/docs-automation-examples/issues) or check the [troubleshooting guide](troubleshooting.md).
