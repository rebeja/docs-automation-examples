# Step 3: Generate structure

Create your site navigation and page templates with AI assistance.

## Complete these tasks

By the end of this step, you will have:

- Site navigation configured in `mkdocs.yml`
- Page templates created for all documentation samples
- Project showcase structure established
- Homepage drafted

## Time estimate

45-60 minutes

## Plan your navigation structure

Good navigation shows information architecture skills. Plan a structure that highlights your documentation samples.

### Recommended structure

```
Home (index.md)
├── About (about.md)
├── Projects (projects/)
│   ├── Overview (index.md)
│   ├── Project 1 (project-1.md)
│   ├── Project 2 (project-2.md)
│   └── Project 3 (project-3.md)
├── Samples (samples/)
│   ├── Overview (index.md)
│   ├── API Reference (api-reference.md)
│   ├── Getting Started (getting-started.md)
│   ├── CLI Reference (cli-reference.md)
│   ├── Tutorial (tutorial.md)
│   └── Troubleshooting (troubleshooting.md)
└── Contact (contact.md)
```

### Alternative structure (documentation-type focused)

```
Home (index.md)
├── About (about.md)
├── API Documentation (api-docs/)
│   ├── REST API Reference (rest-api.md)
│   └── Webhooks Guide (webhooks.md)
├── Tutorials (tutorials/)
│   ├── Getting Started (getting-started.md)
│   └── Advanced Features (advanced.md)
├── Reference (reference/)
│   ├── CLI Commands (cli.md)
│   └── Configuration (config.md)
└── Contact (contact.md)
```

Choose the structure that best showcases your planned documentation types.

## Configure navigation in mkdocs.yml

Open `mkdocs.yml` and update the `nav` section:

```yaml
nav:
  - Home: index.md
  - About: about.md
  - Projects:
      - Overview: projects/index.md
      - EventStream API: projects/eventstream-api.md
      - Docker Guide: projects/docker-guide.md
      - Git CLI Reference: projects/git-cli.md
  - Samples:
      - Overview: samples/index.md
      - API Reference: samples/api-reference.md
      - Getting Started: samples/getting-started.md
      - CLI Reference: samples/cli-reference.md
      - Troubleshooting: samples/troubleshooting.md
  - Contact: contact.md
```

Adjust based on your planning document from Step 2.

## Create directory structure

Create all necessary directories and placeholder files:

```bash
# Create directories
mkdir -p docs/projects
mkdir -p docs/samples

# Create project pages
touch docs/projects/index.md
touch docs/projects/eventstream-api.md
touch docs/projects/docker-guide.md
touch docs/projects/git-cli.md

# Create sample pages
touch docs/samples/index.md
touch docs/samples/api-reference.md
touch docs/samples/getting-started.md
touch docs/samples/cli-reference.md
touch docs/samples/troubleshooting.md

# Create other pages
touch docs/contact.md
```

Adjust filenames to match your planned documentation samples.

## Use AI to draft your homepage

Create a prompt that generates your homepage content. Save this prompt for transparency in your portfolio.

### Example prompt

Create `prompts/homepage-prompt.md`:

```markdown
# Homepage Generation Prompt

Create a homepage for a technical writing portfolio site with these requirements:

## About me
- Technical writer with [X] years of experience
- Specialization in [API documentation / developer tools / etc.]
- Background in [relevant industry or technology]

## Key skills to highlight
- API documentation
- Developer experience (DevEx)
- Docs-as-code workflows
- Technical tutorials
- Information architecture

## Portfolio contents
This site includes:
- [List your planned documentation types]
- Case studies explaining approach to each sample
- Examples of API reference, tutorials, CLI docs, troubleshooting guides

## Tone
- Professional but approachable
- Confident without being boastful
- Clear and concise
- Technical credibility

## Call to action
- Review documentation samples
- View projects
- Download resume
- Contact for opportunities

Generate the homepage content in Markdown format suitable for MkDocs.
```

### Generate content with AI

Use your AI provider to generate the content:

**Using Claude (via CLI or web interface)**:
```
I need help creating a homepage for my technical writing portfolio. 
[Paste your prompt from above]
```

**Using ChatGPT**:
```
I am creating a technical writing portfolio site. Please generate homepage content based on these requirements:
[Paste your prompt from above]
```

### Review and customize output

AI will generate something like:

```markdown
# Welcome

I am a technical writer specializing in developer documentation and API references. 
With 5 years of experience creating clear, accurate documentation for software 
products, I help developers understand complex systems quickly.

## What I do

I create documentation that developers actually want to read:

- **API documentation** - REST APIs, GraphQL, and SDK references
- **Developer guides** - Getting started tutorials and how-to guides
- **CLI documentation** - Command-line tool references and examples
- **Troubleshooting** - Problem-solving guides and error references

## Portfolio highlights

This site showcases documentation samples across multiple types and domains. 
Each project includes a case study explaining my approach, research process, 
and collaboration methods.

Browse the [Projects](projects/index.md) section to see examples of my work, 
or visit [Samples](samples/index.md) for specific documentation types.

## Skills and tools

- Docs-as-code workflows (Git, MkDocs, Markdown)
- API testing and documentation (Postman, curl, OpenAPI)
- Developer empathy and user research
- Information architecture and content strategy
- Technical accuracy and attention to detail

## Get in touch

Interested in working together? [View my resume](about.md#resume) or 
[contact me](contact.md) to discuss opportunities.
```

Save this content to `docs/index.md` after reviewing and customizing.

## Create page templates

Generate templates for your documentation samples. Each template should include standard sections that you will fill with content in Step 4.

### Template for project case studies

Create `templates/project-template.md`:

```markdown
# [Project Name]

[One-sentence description of what this documentation covers]

## Project context

**Type**: [API Reference / Tutorial / CLI Documentation / etc.]  
**Audience**: [Target users - e.g., Backend developers, DevOps engineers]  
**Format**: [Single page / Multi-page guide / Reference documentation]  
**Tools used**: [MkDocs, OpenAPI, etc.]

## Documentation approach

### Research phase

[How you gathered information]
- [Research method 1]
- [Research method 2]
- [Research method 3]

### Content strategy

[Your approach to organizing and presenting information]

### AI collaboration

**AI tool**: [Claude / ChatGPT / etc.]  
**Use cases**:
- [Specific use case 1]
- [Specific use case 2]

**Human oversight**:
- [What you verified manually]
- [What you created without AI]

## Documentation samples

[Link to the actual documentation or include excerpts]

[View full documentation →](../samples/[filename].md)

## Outcomes and learnings

**What worked well**:
- [Success 1]
- [Success 2]

**What I would improve**:
- [Improvement 1]
- [Improvement 2]

**Skills demonstrated**:
- [Skill 1]
- [Skill 2]
- [Skill 3]
```

Copy this template for each project:

```bash
# Copy template for each planned project
cp templates/project-template.md docs/projects/eventstream-api.md
cp templates/project-template.md docs/projects/docker-guide.md
cp templates/project-template.md docs/projects/git-cli.md
```

### Template for documentation samples

Create `templates/sample-template.md`:

```markdown
# [Documentation Sample Title]

[Brief description of what this documentation covers and who it is for]

---

[MAIN DOCUMENTATION CONTENT GOES HERE]

This will be filled in Step 4 with actual documentation content.

---

## About this sample

This documentation sample demonstrates [specific skill or documentation type]. 

**Created for**: [Fictional product / Open source project / Personal project]  
**Documentation type**: [API Reference / Tutorial / CLI Guide / etc.]  
**Target audience**: [Specific user persona]

[View the case study →](../projects/[related-project].md)
```

## Use AI to generate about page

Your about page should be professional and highlight relevant experience.

### Prompt for about page

```markdown
Create an "About" page for a technical writing portfolio with these details:

## Background
- [Your years of experience]
- [Previous roles or companies - can be generalized if needed]
- [Relevant education or certifications]

## Specializations
- [Primary doc types you create]
- [Industries or domains you know]
- [Technical tools and platforms you use]

## Approach to documentation
- [Your documentation philosophy - e.g., "user-first", "developer empathy"]
- [Your process - e.g., "research, draft, test, iterate"]
- [What makes your documentation effective]

## AI transparency
- [How you use AI in your work]
- [Your commitment to accuracy and quality]
- [Balance between AI assistance and human expertise]

Generate professional, authentic content that would appeal to hiring managers.
Tone should be confident but humble, specific but not verbose.
```

Generate with your AI provider and save to `docs/about.md`.

## Create contact page

Create `docs/contact.md`:

```markdown
# Contact

Get in touch to discuss documentation opportunities.

## Professional profiles

- **LinkedIn**: [your-linkedin-url]
- **GitHub**: [your-github-url]
- **Email**: your.email@example.com

## What I can help with

- API documentation and developer guides
- Docs-as-code implementation
- Documentation strategy and planning
- Content migration and improvement
- Technical writing consultation

## Response time

I typically respond to inquiries within 24-48 hours.

## Resume

[Download my resume (PDF)](files/resume.pdf) or [view online version](about.md#resume).
```

## Test your structure

Run your local server and verify navigation:

```bash
mkdocs serve
```

Check that:
- All navigation links work
- No 404 errors for planned pages
- Structure makes logical sense
- Breadcrumbs display correctly

## Summary

You completed these tasks:

- ✓ Planned site navigation structure
- ✓ Configured `mkdocs.yml` with navigation
- ✓ Created directory structure and placeholder files
- ✓ Generated homepage content with AI
- ✓ Created templates for projects and samples
- ✓ Generated about and contact pages
- ✓ Tested site structure locally

Your site now has a complete structure ready for content.

## Save your prompts

Create a `prompts/` directory to track all AI prompts used:

```bash
mkdir prompts
```

Save each prompt you used:
- `prompts/homepage-prompt.md`
- `prompts/about-page-prompt.md`
- `prompts/project-template-prompt.md`

This demonstrates transparency and process documentation skills.

---

Next step: [Write content](step-4-write-content.md)
