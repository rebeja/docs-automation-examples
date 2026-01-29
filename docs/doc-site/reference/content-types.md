# Content types reference

Guide to documentation types for technical writing portfolios.

## Overview

This reference describes different documentation types you can include in your portfolio, with characteristics, use cases, and examples for each.

## Reference documentation

Documentation that describes systems, APIs, or specifications in detail.

### API reference

Documents REST APIs, GraphQL APIs, or SDKs.

**Structure**:
- Overview and purpose
- Authentication methods
- Base URLs and versioning
- Endpoint specifications
- Request and response formats
- Error codes
- Rate limiting
- Code examples

**Key characteristics**:
- Precise and comprehensive
- Consistent formatting
- Complete parameter coverage
- Realistic examples
- Technical accuracy critical

**Example outline**:
```markdown
# EventStream API Reference

## Overview
## Authentication
## Base URL
## Endpoints
### POST /events
### GET /events/{id}
### DELETE /events/{id}
## Error codes
## Rate limiting
## SDKs and libraries
```

**Best for demonstrating**:
- Attention to detail
- Technical precision
- Structured thinking
- Specification comprehension

### CLI reference

Documents command-line tools and utilities.

**Structure**:
- Command synopsis
- Description
- Options and flags
- Arguments
- Exit codes
- Environment variables
- Configuration files
- Usage examples

**Key characteristics**:
- Man page format
- Consistent option documentation
- Short and long flag forms
- Complete examples
- Exit code documentation

**Example outline**:
```markdown
# git-deploy CLI Reference

## Synopsis
## Description
## Global options
## Commands
### git-deploy init
### git-deploy push
### git-deploy status
## Configuration
## Exit codes
## Examples
```

**Best for demonstrating**:
- Technical documentation skills
- Developer tool knowledge
- Precision
- Example quality

### Configuration reference

Documents settings, options, and configuration files.

**Structure**:
- Configuration file location
- File format (YAML, JSON, TOML)
- All available options
- Default values
- Valid value ranges
- Examples
- Troubleshooting

**Key characteristics**:
- Complete option coverage
- Clear default values
- Validation rules
- Example configurations
- Security considerations

**Example outline**:
```markdown
# Configuration Reference

## File location
## Format
## Database settings
## Server options
## Security configuration
## Feature flags
## Example configurations
### Development
### Production
## Environment variables
## Validation
```

**Best for demonstrating**:
- Systematic thinking
- Completeness
- User needs understanding

## Task-oriented documentation

Documentation that helps users accomplish specific goals.

### Getting started guide

Onboards new users to a product or tool.

**Structure**:
- What you will learn
- Prerequisites
- Installation steps
- Verification
- First meaningful task
- Explanation of what happened
- Next steps

**Key characteristics**:
- Clear learning path
- Quick wins
- Encouraging tone
- Expected output shown
- Success criteria defined
- Links to next steps

**Example outline**:
```markdown
# Getting Started with Docker

## What you will learn
## Prerequisites
## Install Docker
## Verify installation
## Run your first container
## Understand what happened
## Next steps
```

**Best for demonstrating**:
- User empathy
- Instructional design
- Onboarding skills
- Pedagogical thinking

### Tutorial

Teaches a skill or concept through hands-on practice.

**Structure**:
- Learning objectives
- Time estimate
- Prerequisites
- Step-by-step instructions
- Checkpoints
- Troubleshooting
- Summary
- What you learned
- Next challenges

**Key characteristics**:
- Learning-focused
- Builds skills progressively
- Includes practice exercises
- Celebrates progress
- Explicit learning outcomes
- Guided discovery

**Example outline**:
```markdown
# Tutorial: Build a REST API with Flask

## What you will learn
## Prerequisites
## Time required: 45 minutes

## Step 1: Set up project
## Step 2: Create basic app
## Step 3: Add database
## Step 4: Implement endpoints
## Step 5: Test your API

## Summary
## Next steps
```

**Best for demonstrating**:
- Teaching ability
- Task breakdown
- User guidance
- Learning design

### How-to guide

Solves a specific problem or accomplishes a particular task.

**Structure**:
- Goal statement
- Prerequisites
- Steps to complete task
- Verification
- Troubleshooting
- Related tasks

**Key characteristics**:
- Task-focused
- Assumes existing knowledge
- Efficient and direct
- Problem-solving oriented
- Actionable steps

**Example outline**:
```markdown
# How to set up multi-stage Docker builds

## Prerequisites
## Create builder stage
## Create production stage
## Copy artifacts between stages
## Test the build
## Verify image size reduction
## Troubleshooting
## Related guides
```

**Best for demonstrating**:
- Problem-solving skills
- Efficiency
- User task understanding
- Practical focus

## Explanatory documentation

Documentation that clarifies concepts and provides understanding.

### Conceptual guide

Explains how something works or why it matters.

**Structure**:
- Introduction
- Key concepts
- How it works
- Why it matters
- Trade-offs
- When to use
- Related concepts

**Key characteristics**:
- Educational focus
- Clear explanations
- Visual aids helpful
- Analogies appropriate
- Big picture view
- Context provided

**Example outline**:
```markdown
# Understanding API Versioning

## What is API versioning
## Why versioning matters
## Versioning strategies
### URL-based versioning
### Header-based versioning
### Content negotiation
## Choosing a strategy
## Best practices
## Common pitfalls
```

**Best for demonstrating**:
- Explanation skills
- Technical understanding
- Clarity
- Teaching ability

### Architecture guide

Explains system design, components, and relationships.

**Structure**:
- System overview
- Components
- Data flow
- Integration points
- Design decisions
- Trade-offs
- Diagrams

**Key characteristics**:
- High-level view
- Visual representation
- Design rationale
- Component relationships
- Technical depth

**Example outline**:
```markdown
# EventStream Architecture

## System overview
## Components
### API gateway
### Event processor
### Message queue
### Storage layer
## Data flow
## Scalability considerations
## Security model
## Deployment architecture
```

**Best for demonstrating**:
- Systems thinking
- Technical depth
- Design understanding
- Communication of complexity

### Comparison guide

Compares options, tools, or approaches.

**Structure**:
- Introduction
- Comparison criteria
- Option descriptions
- Feature comparison table
- Use case recommendations
- Decision framework

**Key characteristics**:
- Objective tone
- Clear criteria
- Fair comparison
- Practical guidance
- Decision support

**Example outline**:
```markdown
# REST versus GraphQL for APIs

## Introduction
## Key differences
## REST characteristics
## GraphQL characteristics
## Comparison table
## Use case recommendations
### Choose REST when
### Choose GraphQL when
## Migration considerations
```

**Best for demonstrating**:
- Analytical thinking
- Objectivity
- Decision guidance
- Practical wisdom

## Support documentation

Documentation that helps users solve problems.

### Troubleshooting guide

Helps users diagnose and fix problems.

**Structure**:
- Problem categories
- Symptom descriptions
- Diagnostic steps
- Solutions
- Prevention tips
- When to escalate

**Key characteristics**:
- Problem-solution format
- Clear symptoms
- Diagnostic guidance
- Step-by-step fixes
- Prevention advice

**Example outline**:
```markdown
# Troubleshooting Docker

## Installation issues
### Docker command not found
### Permission denied
## Runtime issues
### Container won't start
### Port already in use
### Network connectivity
## Performance issues
### Slow image builds
### High memory usage
## Getting help
```

**Best for demonstrating**:
- Problem-solving approach
- User support skills
- Systematic thinking
- Empathy

### FAQ

Answers frequently asked questions.

**Structure**:
- Question categories
- Clear questions
- Concise answers
- Links to detailed docs
- Search-friendly format

**Key characteristics**:
- Question format
- Anticipates user needs
- Concise answers
- Appropriate detail level
- Easy to scan

**Example outline**:
```markdown
# Frequently asked questions

## General questions
### What is Docker?
### Do I need Linux?
### How much does it cost?

## Technical questions
### How do containers work?
### Can I run Windows apps?
### What about security?

## Troubleshooting
### Why won't my container start?
### How do I fix port conflicts?
```

**Best for demonstrating**:
- User needs understanding
- Question anticipation
- Clarity
- Information organization

### Error reference

Documents error codes, messages, and resolutions.

**Structure**:
- Error code or message
- What it means
- Common causes
- How to fix
- Prevention
- Related errors

**Key characteristics**:
- Systematic coverage
- Clear explanations
- Actionable solutions
- Searchable format
- Complete coverage

**Example outline**:
```markdown
# Error Reference

## HTTP 400 errors
### INVALID_PARAMETER
### MISSING_REQUIRED_FIELD

## HTTP 401 errors
### INVALID_TOKEN
### TOKEN_EXPIRED

## HTTP 429 errors
### RATE_LIMIT_EXCEEDED

## HTTP 500 errors
### INTERNAL_SERVER_ERROR
```

**Best for demonstrating**:
- Systematic approach
- Problem-solving
- Completeness
- User support

## Portfolio-specific content

### Case study

Documents your process for creating a documentation sample.

**Structure**:
- Project overview
- Goals and constraints
- Research process
- Information architecture
- Content creation approach
- AI collaboration details
- Challenges and solutions
- Skills demonstrated
- Outcomes and learnings

**Key characteristics**:
- Process-focused
- Transparent about methods
- Honest about challenges
- Reflective
- Shows thinking

**Example outline**:
```markdown
# Case Study: EventStream API Documentation

## Project overview
## Research and planning
## Information architecture
## Content generation
## AI collaboration details
## Technical verification
## Challenges faced
## Skills demonstrated
## What I learned
## View the documentation
```

**Best for demonstrating**:
- Process documentation
- Self-awareness
- Professional growth
- Transparency

### About page

Introduces you and your expertise.

**Structure**:
- Professional summary
- Background and experience
- Specializations
- Tools and skills
- Approach to documentation
- AI collaboration philosophy
- Contact information

**Key characteristics**:
- Professional tone
- Specific examples
- Honest
- Confident without arrogance
- Shows personality

### Writing philosophy statement

Explains your documentation approach and values.

**Structure**:
- Core principles
- User-first focus
- Quality standards
- Collaboration approach
- Continuous learning

**Key characteristics**:
- Values-driven
- Specific examples
- Shows thinking
- Professional

## Choosing content types for your portfolio

### Minimum viable portfolio

Include at least 3 different types:
- 1 reference doc (API or CLI)
- 1 task-oriented doc (getting started or tutorial)
- 1 support doc (troubleshooting or FAQ)

This shows range and versatility.

### Recommended portfolio

Include 5 different types:
- 1 API reference
- 1 getting started guide
- 1 CLI reference or configuration guide
- 1 conceptual guide
- 1 troubleshooting guide

Plus case studies for each.

### Advanced portfolio

Include 7+ types covering:
- Reference documentation (2-3 types)
- Task-oriented content (2-3 types)
- Explanatory content (1-2 types)
- Support documentation (1-2 types)

Demonstrates full documentation skillset.

## Quality standards for each type

All documentation types should meet these standards:

- **Technical accuracy**: Verified and correct
- **Clarity**: Easy to understand
- **Completeness**: Covers necessary information
- **Examples**: Realistic and tested
- **Formatting**: Consistent and professional
- **Tone**: Appropriate for audience
- **Links**: Working and relevant

## Related resources

- [Tutorial Step 4: Write content](../tutorial/step-4-write-content.md)
- [AI collaboration reference](ai-collaboration.md)
- [Portfolio examples](../examples/portfolio-examples.md)
