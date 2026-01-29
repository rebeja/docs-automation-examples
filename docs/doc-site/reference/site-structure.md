# Site structure reference

Information architecture guidance for technical writing portfolio sites.

## Overview

Good site structure makes your portfolio easy to navigate and demonstrates information architecture skills. This reference provides patterns and best practices for organizing portfolio content.

## Core principles

### Principle 1: Clarity over cleverness

Use straightforward navigation labels:

Good:
- "About"
- "Projects"
- "Samples"
- "Contact"

Avoid:
- "Who I Am" (clever but less scannable)
- "My Work" (vague)
- "Stuff I've Made" (unprofessional)

Clear labels help visitors find content quickly.

### Principle 2: Shallow hierarchy

Limit nesting to 2-3 levels maximum:

Good:
```
Home
├── About
├── Projects
│   ├── EventStream API
│   ├── Docker Guide
│   └── Git CLI
└── Contact
```

Too deep:
```
Home
└── Work
    └── Documentation
        └── API Docs
            └── REST APIs
                └── EventStream
```

Shallow hierarchies are easier to navigate.

### Principle 3: Consistent patterns

Use same structure for similar content:

```
Projects/
├── eventstream-api.md
│   - Overview
│   - Approach
│   - Skills demonstrated
├── docker-guide.md
│   - Overview
│   - Approach
│   - Skills demonstrated
└── git-cli.md
    - Overview
    - Approach
    - Skills demonstrated
```

Consistency helps visitors know what to expect.

## Navigation patterns

### Pattern 1: Documentation-focused

Organizes by documentation type.

```
Home
├── About
├── API Documentation
│   ├── REST API Reference
│   └── Webhooks Guide
├── Tutorials
│   ├── Getting Started
│   └── Advanced Features
├── CLI Reference
│   ├── Commands
│   └── Configuration
└── Contact
```

**Advantages**:
- Clearly shows documentation range
- Easy to find specific type
- Professional organization

**Best for**:
- API documentation specialists
- Developer experience roles
- Reference-heavy portfolios

**Example**: Writer specializing in developer tools

### Pattern 2: Project-focused

Organizes by project or case study.

```
Home
├── About
├── Projects
│   ├── Project 1: EventStream API
│   │   ├── Case Study
│   │   └── Documentation
│   ├── Project 2: Docker Guide
│   │   ├── Case Study
│   │   └── Documentation
│   └── Project 3: Git CLI
│       ├── Case Study
│       └── Documentation
└── Contact
```

**Advantages**:
- Shows complete projects
- Tells story of each
- Demonstrates process

**Best for**:
- Showcasing methodology
- Highlighting variety
- Process-oriented portfolios

**Example**: Writer emphasizing user research and process

### Pattern 3: Hybrid approach

Combines projects with samples library.

```
Home
├── About
├── Projects (case studies)
│   ├── EventStream API
│   ├── Docker Guide
│   └── Git CLI
├── Samples (documentation)
│   ├── API Reference
│   ├── Getting Started
│   ├── CLI Documentation
│   └── Troubleshooting
└── Contact
```

**Advantages**:
- Shows both process and output
- Flexible organization
- Comprehensive view

**Best for**:
- Balanced portfolios
- Multiple documentation types
- Versatile skill demonstration

**Example**: Generalist technical writer (recommended)

### Pattern 4: Industry-focused

Organizes by domain or industry.

```
Home
├── About
├── Developer Tools
│   ├── CLI Documentation
│   └── API Reference
├── Cloud Infrastructure
│   ├── Getting Started
│   └── Architecture Guide
├── SaaS Applications
│   ├── User Guides
│   └── API Documentation
└── Contact
```

**Advantages**:
- Shows domain expertise
- Relevant grouping
- Industry knowledge

**Best for**:
- Specialists in specific industry
- Domain experts
- Niche portfolios

**Example**: Writer targeting DevOps tools companies

## Page types and their roles

### Homepage

**Purpose**: Introduce yourself and guide visitors

**Essential elements**:
- Brief introduction (2-3 sentences)
- Key skills highlight
- Navigation to main content areas
- Call to action (view samples, contact)

**Typical length**: 200-400 words

**Example structure**:
```markdown
# Welcome

I am a technical writer specializing in API documentation 
and developer tools.

## What I do
[2-3 documentation types with brief descriptions]

## Portfolio highlights
[Link to key projects]

## Skills and tools
[Brief list]

## Get in touch
[Link to contact or about page]
```

### About page

**Purpose**: Provide professional background and expertise

**Essential elements**:
- Professional summary
- Relevant experience
- Specializations
- Tools and skills
- Approach to documentation
- Contact information or resume link

**Typical length**: 400-600 words

**Example structure**:
```markdown
# About

## Background
[2-3 paragraphs on experience]

## Specializations
[What you focus on]

## Tools and skills
[Technical skills]

## Approach
[Your documentation philosophy]

## Contact
[How to reach you]
```

### Project case study page

**Purpose**: Explain process and demonstrate skills

**Essential elements**:
- Project context
- Goals and constraints
- Research and planning
- Information architecture
- Content creation approach
- AI collaboration details
- Challenges and solutions
- Skills demonstrated
- Link to actual documentation

**Typical length**: 600-1000 words

**Example structure**:
```markdown
# Project: EventStream API Documentation

## Overview
[What this project covers]

## Approach
[How you created it]

## AI collaboration
[How AI was used]

## Skills demonstrated
[What this shows]

## View documentation
[Link to the actual docs]
```

### Documentation sample page

**Purpose**: Show actual documentation work

**Essential elements**:
- Clear documentation content
- Appropriate formatting
- Realistic examples
- Professional polish
- Link back to case study

**Typical length**: Varies by type (500-2000 words)

**Example structure**:
```markdown
# EventStream API Reference

[Complete API documentation]

---

## About this sample
[Brief context]

[Link to case study]
```

### Contact page

**Purpose**: Make it easy to reach you

**Essential elements**:
- Professional email
- LinkedIn profile
- GitHub profile (if relevant)
- Response time expectation
- What you can help with

**Typical length**: 100-200 words

**Example structure**:
```markdown
# Contact

## Professional profiles
[Links to LinkedIn, GitHub, etc.]

## What I can help with
[Brief list]

## Response time
[Set expectations]

## Resume
[Download link]
```

## Organization strategies

### Strategy 1: Chronological ordering

Order projects or samples by creation date.

```
Projects/
├── 2024-11-eventstream-api.md (newest)
├── 2024-10-docker-guide.md
└── 2024-09-git-cli.md (oldest)
```

**Advantages**:
- Shows recent work first
- Demonstrates progression
- Easy to maintain

**Disadvantages**:
- Best work may not be first
- Less logical grouping

**Best for**: Portfolios with clear improvement over time

### Strategy 2: Quality ordering

Order by quality or importance.

```
Projects/
├── eventstream-api.md (best work)
├── docker-guide.md
└── git-cli.md (good but less impressive)
```

**Advantages**:
- Best work appears first
- Strong first impression
- Strategic presentation

**Disadvantages**:
- Subjective ordering
- May need reordering

**Best for**: Portfolios with clear standout pieces

### Strategy 3: Type-based ordering

Group by documentation type.

```
Samples/
├── API Reference/
│   ├── rest-api.md
│   └── webhooks.md
├── Tutorials/
│   ├── getting-started.md
│   └── advanced.md
└── CLI Documentation/
    └── commands.md
```

**Advantages**:
- Easy to find specific types
- Shows documentation range
- Professional organization

**Disadvantages**:
- May fragment related projects
- Less narrative flow

**Best for**: Portfolios emphasizing versatility

### Strategy 4: Difficulty ordering

Order from simple to complex.

```
Samples/
├── getting-started.md (simple)
├── cli-reference.md (moderate)
└── api-reference.md (complex)
```

**Advantages**:
- Progressive complexity
- Gentle introduction
- Shows range

**Disadvantages**:
- May not highlight best work
- Arbitrary complexity judgment

**Best for**: Tutorial-focused portfolios

## Navigation best practices

### Use descriptive labels

Labels should explain content:

Good:
- "API Documentation Samples"
- "Getting Started Tutorials"
- "Case Studies"

Avoid:
- "Docs" (too vague)
- "Stuff" (unprofessional)
- "Things" (not descriptive)

### Limit top-level items

Keep main navigation to 4-6 items:

Recommended:
```
- Home
- About
- Projects
- Samples
- Contact
```

Too many:
```
- Home
- About Me
- My Background
- Projects
- Work Samples
- Case Studies
- Writing Philosophy
- Tools I Use
- Contact
- Resume
```

### Include breadcrumbs

Help visitors understand location:

```
Home > Projects > EventStream API
```

MkDocs Material includes breadcrumbs by default.

### Add search functionality

Enable search for easy navigation:

```yaml
plugins:
  - search
```

Especially important for portfolios with many samples.

### Provide clear entry points

From homepage, make it obvious where to start:

```markdown
## Portfolio highlights

Browse my [Projects](projects/index.md) to see case studies, 
or jump directly to [Documentation Samples](samples/index.md).
```

## File naming conventions

### Use descriptive names

Good:
- `eventstream-api.md`
- `docker-getting-started.md`
- `git-cli-reference.md`

Avoid:
- `project1.md`
- `sample.md`
- `doc.md`

### Use consistent naming patterns

Choose a pattern and stick to it:

**Kebab case** (recommended):
- `eventstream-api.md`
- `docker-guide.md`

**Snake case**:
- `eventstream_api.md`
- `docker_guide.md`

**Avoid**:
- `EventStreamAPI.md` (camelCase)
- `eventstream api.md` (spaces)

### Include type in filename

When organizing by type:

```
samples/
├── api-reference-eventstream.md
├── tutorial-docker-basics.md
├── cli-reference-git-deploy.md
```

Or use directories:

```
samples/
├── api-reference/
│   └── eventstream.md
├── tutorials/
│   └── docker-basics.md
├── cli-reference/
    └── git-deploy.md
```

## Scaling your portfolio

### Starting with 3 samples

Minimal structure:

```
Home
├── About
├── Samples
│   ├── API Reference
│   ├── Getting Started
│   └── CLI Documentation
└── Contact
```

Simple, focused, manageable.

### Growing to 5-7 samples

Add organization:

```
Home
├── About
├── Projects
│   └── [Case studies for each]
├── Samples
│   └── [Organized by type]
└── Contact
```

Separate process from output.

### Expanding to 10+ samples

Add categories:

```
Home
├── About
├── Developer Documentation
│   ├── API Reference
│   ├── CLI Tools
│   └── SDKs
├── User Documentation
│   ├── Getting Started
│   ├── Tutorials
│   └── How-to Guides
├── Technical Concepts
│   ├── Architecture
│   ├── Best Practices
│   └── Troubleshooting
└── Contact
```

Organize into meaningful groups.

## Common mistakes to avoid

### Mistake 1: Too much nesting

Problem: Visitors lost in deep hierarchy

Solution: Flatten structure, use 2-3 levels maximum

### Mistake 2: Vague labels

Problem: Navigation unclear

Solution: Use specific, descriptive labels

### Mistake 3: Inconsistent structure

Problem: Similar pages organized differently

Solution: Use templates and consistent patterns

### Mistake 4: Missing context

Problem: Samples without explanation

Solution: Include case studies or introductions

### Mistake 5: No clear entry point

Problem: Visitors don't know where to start

Solution: Provide clear paths on homepage

## Testing your structure

### Navigation test

Ask someone unfamiliar with your portfolio:

1. Find an API reference sample
2. Find information about your background
3. Locate your contact information
4. Return to homepage

If they struggle, simplify navigation.

### Scan test

Can visitors understand your portfolio structure in 10 seconds?

Check:
- Clear labels
- Obvious organization
- Limited top-level items
- Visible navigation

### Mobile test

Verify structure works on mobile:

```bash
# Test with MkDocs local server
mkdocs serve
# Visit on mobile or use browser dev tools
```

Material theme is responsive by default, but test your specific structure.

## Related resources

- [Tutorial Step 3: Generate structure](../tutorial/step-3-generate-structure.md)
- [Content types reference](content-types.md)
- [Portfolio examples](../examples/portfolio-examples.md)
