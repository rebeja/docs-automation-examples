# Step 4: Write content

Generate documentation samples with AI collaboration.

## Complete these tasks

By the end of this step, you will have:

- 3-5 complete documentation samples
- Different documentation types represented
- AI-generated content reviewed for accuracy
- Case studies documenting your process

## Time estimate

2-3 hours

## Overview of AI collaboration approach

This step teaches you to collaborate with AI effectively for different documentation types. You will learn:

- Specific prompting techniques for each doc type
- How to structure prompts for best results
- When to use AI generation versus editing
- How to verify and improve AI output

## Principle: Start with structure, then fill content

The most effective approach:

1. Define the structure and outline yourself
2. Use AI to generate initial content for each section
3. Review and edit for accuracy and tone
4. Add examples and specifics manually
5. Iterate based on quality

Do not: Ask AI to "write complete documentation" without structure.  
Do: Provide detailed outlines and generate section-by-section.

## Documentation type 1: API reference

API reference documentation requires precision and completeness.

### Create the structure first

Plan your API endpoints before generating content:

```markdown
# EventStream API Reference

## Overview
[Description of API purpose]

## Authentication
[How to authenticate]

## Base URL
[API base URL and versioning]

## Endpoints

### POST /events
[Endpoint details]

### GET /events/{id}
[Endpoint details]

### DELETE /events/{id}
[Endpoint details]

## Response codes
[HTTP status codes]

## Rate limiting
[Rate limit information]

## Examples
[Complete request/response examples]
```

### Prompt for API endpoint documentation

Create `prompts/api-endpoint-prompt.md`:

```markdown
Generate API reference documentation for this endpoint:

## Endpoint details
- Method: POST
- Path: /events
- Purpose: Create a new event in the EventStream system
- Authentication: Required (Bearer token)

## Request parameters

Body parameters:
- name (string, required): Event name
- type (string, required): Event type (webhook, scheduled, manual)
- payload (object, required): Event data
- timestamp (string, optional): ISO 8601 timestamp

## Response

Success (201):
- Returns created event object with ID
- Includes: id, name, type, payload, timestamp, created_at

Error responses:
- 400: Invalid parameters
- 401: Authentication failed
- 429: Rate limit exceeded

## Example

Request:
```json
{
  "name": "user.created",
  "type": "webhook",
  "payload": {
    "user_id": "12345",
    "email": "user@example.com"
  }
}
```

Response (201):
```json
{
  "id": "evt_abc123",
  "name": "user.created",
  "type": "webhook",
  "payload": {
    "user_id": "12345",
    "email": "user@example.com"
  },
  "timestamp": "2024-01-15T10:30:00Z",
  "created_at": "2024-01-15T10:30:00Z"
}
```

Generate clear, concise API reference documentation for this endpoint. 
Use standard API documentation format with sections for:
- Description
- Authentication
- Parameters
- Response format
- Error handling
- Example request and response

Target audience: Backend developers integrating this API
Tone: Technical, precise, professional
```

### Generate and review

1. Send prompt to your AI provider
2. Review generated content for:
   - Technical accuracy
   - Completeness (all parameters documented)
   - Consistent formatting
   - Clear examples
3. Add or correct details AI might have invented
4. Verify JSON syntax in examples

### What to check manually

AI often makes these mistakes in API docs:
- Invents parameter names not in your spec
- Inconsistent data types
- Missing required versus optional distinction
- Unrealistic example values
- Incomplete error handling

Always verify against your planned API structure.

## Documentation type 2: Getting started guide

Getting started guides need clear steps and user empathy.

### Structure the learning path

Plan the user journey:

```markdown
# Getting Started with Docker

## What you will learn
[Learning objectives]

## Prerequisites
[What users need before starting]

## Step 1: Install Docker
[Installation instructions]

## Step 2: Verify installation
[How to confirm it works]

## Step 3: Run your first container
[Simple, successful first experience]

## Step 4: Understand what happened
[Explain the concepts]

## Next steps
[Where to go from here]
```

### Prompt for getting started content

```markdown
Generate a "Getting Started" guide section with these requirements:

## Topic
Installing Docker on macOS

## Target audience
Developers new to Docker with basic command line experience

## Learning objective
User successfully installs Docker and runs their first container

## Key points to cover
- Installation via Homebrew (preferred method)
- Alternative: Docker Desktop download
- Verification steps
- Simple "hello world" container
- Explanation of what happened

## Tone
- Encouraging and supportive
- Assumes no prior Docker knowledge
- Celebrates small wins
- Anticipates common questions

## Format requirements
- Step-by-step numbered instructions
- Expected output shown for each command
- Troubleshooting tips for common issues
- Clear "success criteria" for each step

Generate the installation and verification section only. I will add 
the container running section separately.
```

### Effective techniques for tutorials

Use these approaches for better tutorial content:

**Show expected output**:
```markdown
Run the verification command:

```bash
docker --version
```

Expected output:
```
Docker version 24.0.6, build ed223bc
```
```

**Anticipate problems**:
```markdown
If you see "command not found":
- Restart your terminal
- Verify installation with: `which docker`
- Check PATH includes `/usr/local/bin`
```

**Celebrate progress**:
```markdown
✓ Docker is installed and ready to use!
```

## Documentation type 3: CLI reference

CLI documentation requires comprehensive command coverage.

### Structure command documentation

```markdown
# git-deploy CLI Reference

## Synopsis
git-deploy [OPTIONS] <COMMAND>

## Description
[What this tool does]

## Global options
[Options that apply to all commands]

## Commands

### git-deploy init
[Command details]

### git-deploy push
[Command details]

### git-deploy status
[Command details]

## Exit codes
[What different exit codes mean]

## Examples
[Real-world usage examples]
```

### Prompt for CLI command documentation

```markdown
Generate CLI reference documentation for this command:

## Command
git-deploy push

## Purpose
Deploy code to specified environment

## Usage
git-deploy push [OPTIONS] <environment>

## Arguments
- environment (required): Target environment (staging, production)

## Options
- `--branch <name>`: Deploy specific branch (default: current branch)
- `--force`: Force deployment (skip checks)
- `--dry-run`: Show what would be deployed without deploying
- `--verbose`: Show detailed output

## Behavior
1. Validates current branch is clean
2. Runs tests if configured
3. Builds deployment package
4. Pushes to target environment
5. Runs post-deploy checks

## Exit codes
- 0: Success
- 1: Validation failed
- 2: Tests failed
- 3: Deployment failed

## Examples needed
- Basic deployment to staging
- Force deployment to production
- Dry run to see what would deploy

Generate comprehensive CLI reference documentation.
Format: Standard man page style with clear sections.
Include all options with short and long forms.
Examples should be realistic and well-explained.
```

### CLI documentation best practices

**Use consistent formatting**:
```markdown
### Options

`-b, --branch <name>`
: Deploy specific Git branch instead of current branch.

`-f, --force`
: Skip safety checks and force deployment. Use with caution.

`-n, --dry-run`
: Show deployment plan without executing. Safe to run in production.
```

**Show complete examples**:
```markdown
Deploy current branch to staging:
```bash
git-deploy push staging
```

Deploy specific branch to production with verbose output:
```bash
git-deploy push --branch release-1.2 --verbose production
```
```

## Documentation type 4: Troubleshooting guide

Troubleshooting docs help users solve problems independently.

### Structure problem-solution format

```markdown
# Troubleshooting Docker

## Installation issues

### Docker command not found

**Symptom**: Running `docker` shows "command not found"

**Cause**: Docker not installed or not in PATH

**Solution**:
[Step-by-step fix]

### Permission denied error

**Symptom**: `docker ps` shows "permission denied"

**Cause**: User not in docker group

**Solution**:
[Step-by-step fix]

## Runtime issues

### Container won't start

[Problem details and solution]

### Port already in use

[Problem details and solution]
```

### Prompt for troubleshooting content

```markdown
Generate troubleshooting documentation for this problem:

## Problem
Docker containers fail to start with "port already in use" error

## Context
- Occurs when user tries: `docker run -p 8080:80 nginx`
- Error message: "Error starting userland proxy: listen tcp4 0.0.0.0:8080: bind: address already in use"
- Common scenario: User ran container before and it's still running

## Target audience
Developers new to Docker

## Solution structure needed
1. Explanation of what error means
2. How to identify what's using the port
3. Steps to fix (stop conflicting container or use different port)
4. Prevention tips

## Tone
- Calm and reassuring (errors are normal)
- Educational (explain why this happens)
- Practical (clear steps to fix)

Generate complete troubleshooting entry with:
- Clear symptom description
- Root cause explanation
- Step-by-step solution with commands
- Prevention guidance
```

### Troubleshooting documentation patterns

**Use consistent structure**:
```markdown
### Problem: Container fails to start

**Symptoms**:
- `docker start` command hangs
- No error message displayed
- Container status shows "Exited"

**Common causes**:
- Application error in container
- Missing environment variables
- Port conflict

**Diagnosis**:
```bash
# Check container logs
docker logs container-name

# Check container details
docker inspect container-name
```

**Solutions**:

If logs show missing environment variable:
```bash
docker rm container-name
docker run -e VAR=value image-name
```

If port conflict:
```bash
docker rm container-name
docker run -p 8081:80 image-name
```

**Prevention**:
- Always check logs first: `docker logs`
- Use `--rm` flag for temporary containers
- Document required environment variables
```

## Documentation type 5: Conceptual guide

Conceptual documentation explains how things work.

### Structure explanatory content

```markdown
# Understanding API Versioning

## What is API versioning

[Definition and purpose]

## Why API versioning matters

[Business and technical reasons]

## Versioning strategies

### URL-based versioning
[Explanation, pros, cons, example]

### Header-based versioning
[Explanation, pros, cons, example]

### Content negotiation
[Explanation, pros, cons, example]

## Choosing a strategy

[Decision framework]

## Best practices

[Recommendations]

## Summary

[Key takeaways]
```

### Prompt for conceptual content

```markdown
Generate a conceptual guide section explaining:

## Topic
URL-based API versioning strategy

## Target audience
Backend developers designing RESTful APIs

## Key points to explain
- What it is: Including version in URL path (/v1/, /v2/)
- How it works: Examples of versioned endpoints
- Advantages: Clear, explicit, easy to test
- Disadvantages: URL proliferation, routing complexity
- When to use: Public APIs, breaking changes, long support periods

## Format
- Start with clear definition
- Provide concrete examples
- Explain trade-offs objectively
- Include real-world scenarios
- End with decision criteria

## Tone
- Educational and objective
- Balanced (not prescriptive)
- Technical but accessible

Generate explanatory content that helps developers understand the concept 
and make informed decisions. Include code examples where helpful.
```

## Documentation type 6: How-to guide

How-to guides are task-focused and assume existing knowledge.

### Structure task-oriented content

```markdown
# How to set up Docker multi-stage builds

## Prerequisites
- Docker installed
- Existing Dockerfile
- Basic Docker knowledge

## Steps

### 1. Create base stage
[Instructions]

### 2. Add build stage
[Instructions]

### 3. Create production stage
[Instructions]

### 4. Test the build
[Instructions]

## Verification
[How to confirm it worked]

## Troubleshooting
[Common issues]

## Related guides
[Links to related content]
```

### Prompt for how-to content

```markdown
Generate a how-to guide for:

## Task
Configure Docker multi-stage builds for a Node.js application

## Audience
Developers familiar with Docker basics who want to optimize images

## Goal
Reduce final image size by separating build and runtime dependencies

## Steps to cover
1. Create builder stage with full dependencies
2. Build application in builder stage
3. Create production stage with minimal dependencies
4. Copy build artifacts from builder to production
5. Verify image size reduction

## Requirements
- Use specific, executable commands
- Show before/after Dockerfile comparison
- Include size comparison numbers
- Explain why each step matters

## Format
- Numbered steps
- Code blocks with syntax highlighting
- Inline explanations of what each section does
- Success criteria at the end

Generate practical how-to content that developers can follow immediately.
```

## Combine AI generation with manual expertise

The most effective approach combines AI and human input:

### AI is good for:
- Initial content structure
- Standard explanations
- Consistent formatting
- Example code patterns
- Common troubleshooting scenarios

### Humans must provide:
- Technical accuracy verification
- Realistic examples
- Context-specific details
- Tone adjustments
- Error checking

## Create case studies for each sample

For each documentation sample you create, write a case study explaining your process.

### Case study template

```markdown
# Case Study: [Documentation Sample Name]

## Project overview

**Documentation type**: [API Reference / Tutorial / etc.]  
**Topic**: [What you documented]  
**Approach**: [Open source / Fictional product / Own project]  
**Target audience**: [Who this is for]  
**Time investment**: [Hours spent]

## Process

### 1. Research and planning
[How you gathered information about the topic]
[What you decided to include or exclude]

### 2. Information architecture
[How you organized the content]
[Why you chose this structure]

### 3. Content generation
[Which sections you wrote manually]
[Which sections you generated with AI]
[How you used AI (specific prompts)]

### 4. Review and revision
[How you verified accuracy]
[What you changed from initial AI output]
[Testing or validation process]

## AI collaboration details

**Tool used**: [Claude 3.5 Sonnet / GPT-4 / etc.]

**Prompts created**: [Number of prompts]

**AI contribution**: [Percentage estimate]
- Content generation: [%]
- Editing suggestions: [%]
- Example creation: [%]

**Human contribution**: [Percentage estimate]
- Technical accuracy: [%]
- Information architecture: [%]
- Final editing: [%]

### Sample prompt

[Include one representative prompt you used]

### What worked well with AI

- [Specific success 1]
- [Specific success 2]

### What required human oversight

- [Area needing correction 1]
- [Area needing correction 2]

## Skills demonstrated

This sample demonstrates:
- [Skill 1]
- [Skill 2]
- [Skill 3]

## Outcomes

**Documentation quality**: [Self-assessment]

**What I learned**:
- [Learning 1]
- [Learning 2]

**What I would improve**:
- [Improvement 1]
- [Improvement 2]

[View the documentation →](../samples/[filename].md)
```

## Save all your prompts

Create a prompt file for each documentation sample:

```bash
mkdir prompts
touch prompts/api-reference-prompts.md
touch prompts/getting-started-prompts.md
touch prompts/cli-reference-prompts.md
touch prompts/troubleshooting-prompts.md
```

In each file, save:
- All prompts you used
- Which sections each prompt generated
- How you modified the output
- What you learned about prompting

This documentation shows your process and builds prompt engineering skills.

## Summary

You completed these tasks:

- ✓ Generated 3-5 complete documentation samples
- ✓ Used specific prompting techniques for each type
- ✓ Reviewed AI output for accuracy and completeness
- ✓ Created case studies documenting your process
- ✓ Saved all prompts for transparency
- ✓ Demonstrated multiple documentation types

Your portfolio now contains substantial, realistic documentation samples.

## Quality checklist

Before moving to the next step, verify each sample:

- [ ] Technical accuracy verified
- [ ] Examples tested and working
- [ ] Consistent formatting
- [ ] Appropriate tone for audience
- [ ] Complete coverage of topic
- [ ] Clear structure and navigation
- [ ] Case study written
- [ ] Prompts documented

---

Next step: [Refine with AI](step-5-refine-with-ai.md)
