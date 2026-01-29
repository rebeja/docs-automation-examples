# AI collaboration reference

Best practices and patterns for effective AI-assisted documentation creation.

## Overview

This reference provides strategies for collaborating with AI tools (Claude, ChatGPT) to create high-quality documentation for your portfolio.

## Principles of effective AI collaboration

### AI as collaborator, not replacement

Successful AI collaboration treats AI as a drafting partner:

**AI responsibilities**:
- Generate initial content structure
- Provide standard explanations
- Create example code patterns
- Suggest improvements
- Maintain formatting consistency

**Human responsibilities**:
- Define structure and requirements
- Verify technical accuracy
- Add domain expertise
- Make final decisions
- Ensure authentic voice

### Iterate, do not generate once

Effective process:

1. Start with detailed prompt
2. Review AI output critically
3. Identify what works and what needs improvement
4. Refine prompts based on output
5. Regenerate improved sections
6. Repeat until quality meets standards

Do not accept first output. Iteration produces better results.

### Be specific in prompts

Vague prompts produce generic output.

Bad:
```
Write API documentation.
```

Good:
```
Generate API reference documentation for a POST /events endpoint that 
creates webhook events. Include: authentication (Bearer token required), 
request parameters (name, type, payload), response format (201 success 
with event object), error responses (400, 401, 429), and complete 
JSON example request/response.

Target audience: Backend developers integrating this API
Tone: Technical, precise, professional
```

Specificity drives quality.

## Content generation patterns

### Pattern 1: Structure first, content second

Define structure yourself, use AI to fill sections.

Your work:
```markdown
# EventStream API Reference

## Overview
[AI will fill this]

## Authentication
[AI will fill this]

## Endpoints

### POST /events
[AI will fill this]

### GET /events/{id}
[AI will fill this]
```

AI prompt:
```
Fill the [AI will fill this] sections with appropriate content.
For Overview: Explain what this API does in 2-3 sentences.
For Authentication: Explain Bearer token authentication.
For each endpoint: Include full specifications.
```

This gives you control over structure while leveraging AI for content.

### Pattern 2: Example-driven generation

Provide examples, ask AI to follow the pattern.

Your prompt:
```
Generate three more API endpoint descriptions following this example:

Example:
### GET /users/{id}

Retrieve a specific user by ID.

**Authentication**: Required

**Parameters**:
- `id` (path, required): User ID

**Response** (200):
```json
{
  "id": "user_123",
  "name": "Jane Doe",
  "email": "jane@example.com"
}
```

Generate similar documentation for:
- POST /users
- PUT /users/{id}
- DELETE /users/{id}
```

Pattern-based generation ensures consistency.

### Pattern 3: Section-by-section generation

Generate one section at a time with full context.

Prompt sequence:

1. "Generate the Overview section for Docker getting started guide. Target audience: Developers new to containers."
2. "Generate the Installation section. Previous section explained Docker basics. Cover installation on macOS via Homebrew."
3. "Generate the First Container section. Previous sections covered overview and installation. Walk through running hello-world image."

Sequential generation maintains coherence.

### Pattern 4: Template instantiation

Create a template, use AI to fill with specific details.

Template:
```markdown
# [TECHNOLOGY] CLI Reference

## Synopsis
[COMMAND] [OPTIONS] <ARGUMENTS>

## Description
[WHAT IT DOES]

## Options
[OPTION LIST]

## Examples
[EXAMPLES]
```

Prompt:
```
Fill this CLI reference template for the git-deploy push command:
- TECHNOLOGY: git-deploy
- COMMAND: git-deploy push
- ARGUMENTS: environment name (staging or production)
- WHAT IT DOES: Deploys code to specified environment
- OPTIONS: --branch, --force, --dry-run, --verbose
- EXAMPLES: Basic deploy to staging, force deploy to production
```

Templates ensure consistent structure across similar content.

## Content refinement patterns

### Pattern 1: Clarity improvement

Prompt for improving existing content:

```markdown
Review this documentation section for clarity:

[Paste content]

Identify and fix:
1. Sentences longer than 25 words
2. Passive voice instances
3. Undefined jargon
4. Ambiguous pronouns
5. Redundant phrases

Maintain technical accuracy and professional tone.
```

Focus on specific improvements.

### Pattern 2: Tone consistency check

Ensure consistent voice across sections:

```markdown
Compare these two sections for tone consistency:

Section 1 (Getting Started):
[Paste]

Section 2 (API Reference):
[Paste]

Identify tone differences in:
- Formality level
- Use of "you" versus "we"
- Sentence complexity
- Technical depth

Suggest changes to make tone consistent. Target: Professional, 
user-focused, technically precise.
```

### Pattern 3: Technical accuracy review

Use AI to flag potential issues:

```markdown
Review this technical content for potential accuracy issues:

[Paste content]

Flag concerns as questions:
- "Is it accurate that X?" 
- "Does Y work in all cases?"
- "Should Z include caveats about...?"

Do not make corrections. Flag concerns for human verification.
```

AI identifies issues, humans verify and fix.

### Pattern 4: Example enhancement

Improve code examples:

```markdown
Improve this code example:

```python
r = requests.get('https://api.example.com/data')
print(r.json())
```

Make improvements:
1. Meaningful variable names
2. Error handling
3. Required imports
4. Comments explaining steps
5. Production-ready or marked as simplified

Context: API documentation for developers learning the API
```

## Prompt engineering techniques

### Technique 1: Role assignment

Give AI a specific perspective:

```markdown
You are a technical writer creating API documentation for backend 
developers. Your audience has 3-5 years of experience and expects 
precise, complete specifications without unnecessary explanation.

Generate documentation for...
```

Role-setting influences tone and depth.

### Technique 2: Constraint specification

Define what to avoid:

```markdown
Generate a tutorial for Docker basics.

Constraints:
- Do not assume prior container knowledge
- Do not use jargon without explanation
- Do not skip installation steps
- Do not show incomplete examples
- Do not exceed 2000 words

Include:
- Clear learning objectives
- Step-by-step instructions
- Expected output for each command
- Troubleshooting tips
```

Explicit constraints prevent common issues.

### Technique 3: Format specification

Define exact output format:

```markdown
Generate CLI command documentation in this exact format:

### COMMAND NAME

DESCRIPTION (1-2 sentences)

**Syntax**:
`command [options] <arguments>`

**Options**:
- `--option`: Description
- `-o`: Short form

**Arguments**:
- `arg`: Description

**Examples**:
```bash
# Example 1 description
command example

# Example 2 description
command --option example
```

Generate documentation for: git-deploy push
```

Format specification ensures consistency.

### Technique 4: Iterative refinement

Refine through conversation:

Initial prompt:
```
Generate API endpoint documentation for POST /events
```

After reviewing output:
```
Good start. Make these changes:
1. Add authentication section before parameters
2. Include all error codes (400, 401, 403, 429)
3. Make examples more realistic (use real-looking IDs)
4. Add rate limiting information
```

Conversational refinement reaches target quality.

## Common pitfalls and solutions

### Pitfall 1: Over-reliance on AI

Problem: Accepting AI output without critical review

Solution:
- Always verify technical accuracy
- Test all code examples
- Check for logical consistency
- Ensure appropriate tone
- Add human expertise

### Pitfall 2: Vague prompts

Problem: Generic prompts produce generic output

Solution:
- Specify audience explicitly
- Define tone and style
- Provide examples
- Include constraints
- Detail requirements

### Pitfall 3: Single-pass generation

Problem: Expecting perfect output on first try

Solution:
- Plan multiple iterations
- Review critically
- Identify specific improvements
- Refine prompts
- Regenerate improved versions

### Pitfall 4: Ignoring context limits

Problem: Trying to generate too much at once

Solution:
- Break into sections
- Generate incrementally
- Maintain context between sections
- Build on previous outputs

### Pitfall 5: Not documenting process

Problem: Losing track of prompts and iterations

Solution:
- Save all prompts used
- Document what worked
- Note what required changes
- Create reusable templates
- Build prompt library

## Documentation of AI use

### Case study inclusion

Document your AI collaboration:

```markdown
## AI collaboration details

**Tool**: Claude 3.5 Sonnet via Anthropic API

**Process**:
1. Created content outline manually
2. Generated initial drafts with AI (sections 1-4)
3. Verified technical accuracy against official docs
4. Rewrote examples with realistic data
5. Refined tone for consistency
6. Added domain expertise

**AI contribution**: ~45% initial generation, ~20% editing suggestions
**Human contribution**: ~35% verification and editing

**Prompts used**: [Link to prompts/api-reference-prompts.md]

**What worked well**:
- Structure generation
- Consistent formatting
- Standard explanations

**What required human oversight**:
- Technical accuracy
- Realistic examples
- Domain-specific context
```

Transparency demonstrates professionalism.

### Honest percentage estimates

Estimate AI versus human contribution:

- **40-60% AI**: Heavy AI generation with significant human editing
- **60-40% human**: AI-assisted editing of human-created content
- **20-80% human**: AI used sparingly for suggestions only

Be realistic about contributions.

### Prompt archiving

Save prompts for transparency:

Create `prompts/` directory:
```
prompts/
├── api-reference-prompts.md
├── getting-started-prompts.md
├── cli-reference-prompts.md
└── editing-prompts.md
```

Include in each file:
- Original prompt text
- Which sections it generated
- How output was modified
- What was learned

## Best practices summary

### Do:
- Provide detailed, specific prompts
- Iterate on output quality
- Verify all technical information
- Document your process
- Test all examples
- Maintain authentic voice
- Be transparent about AI use

### Do not:
- Accept first output without review
- Trust AI for technical accuracy
- Generate everything at once
- Use vague, generic prompts
- Skip human verification
- Pretend AI wasn't used
- Let AI make final decisions

## Related resources

- [Prompt templates](../examples/prompt-templates.md)
- [Tutorial Step 4: Write content](../tutorial/step-4-write-content.md)
- [Tutorial Step 5: Refine with AI](../tutorial/step-5-refine-with-ai.md)
