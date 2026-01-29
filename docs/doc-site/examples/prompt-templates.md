# Prompt templates

Reusable AI prompts for creating portfolio documentation.

## How to use these templates

These templates provide starting points for AI prompts. Adapt them by:

1. Replacing [PLACEHOLDERS] with your specific details
2. Adding or removing sections based on your needs
3. Including examples relevant to your documentation
4. Adjusting tone and style for your audience

Save your customized prompts for reuse and iteration.

## Homepage prompts

### Template 1: Professional introduction

```markdown
Generate a homepage for a technical writing portfolio with these requirements:

## About me
- Technical writer with [X] years of experience
- Specialization in [API documentation / developer tools / etc.]
- Background in [relevant industry or technology]
- Target roles: [List 2-3 specific job titles]

## Key skills to highlight
- [Skill 1]
- [Skill 2]
- [Skill 3]
- [Skill 4]

## Portfolio contents
This site includes:
- [Number] documentation samples across [types]
- Case studies explaining approach
- Examples of [specific documentation types]

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

Generate homepage content in Markdown format suitable for MkDocs.
Target length: 300-400 words.
```

### Template 2: Skills-focused homepage

```markdown
Create a homepage emphasizing technical writing skills:

## Professional summary
[Your 2-3 sentence summary]

## Core competencies
Highlight these skills with brief examples:
- [Skill 1]: [Brief example or context]
- [Skill 2]: [Brief example or context]
- [Skill 3]: [Brief example or context]

## Documentation types
I create:
- [Type 1]: [What it involves]
- [Type 2]: [What it involves]
- [Type 3]: [What it involves]

## Recent projects
[List 3-5 project names]

## Call to action
[What you want visitors to do next]

Tone: Professional, confident, technically credible
Format: Scannable with clear headings
Length: 250-350 words
```

## About page prompts

### Template: Professional background

```markdown
Create an "About" page for a technical writing portfolio:

## Background
- [Years] of experience in technical writing
- Previous roles: [List 2-3 relevant positions or contexts]
- Transition story (if career change): [Brief explanation]
- Education: [Relevant degrees or certifications]

## Specializations
Primary focus areas:
- [Specialization 1]: [What you emphasize]
- [Specialization 2]: [What you emphasize]
- [Specialization 3]: [What you emphasize]

## Technical skills
Tools and technologies:
- Documentation: [MkDocs, Sphinx, etc.]
- Version control: [Git, GitHub, etc.]
- Languages: [Markdown, reStructuredText, etc.]
- Development: [Python, JavaScript, etc.]
- Platforms: [Linux, Docker, cloud services, etc.]

## Approach to documentation
My documentation philosophy:
- [Principle 1]: [Brief explanation]
- [Principle 2]: [Brief explanation]
- [Principle 3]: [Brief explanation]

## AI collaboration
How I use AI in my work:
- [Use case 1]
- [Use case 2]
- My commitment to accuracy and quality
- Balance between AI assistance and human expertise

## Contact
[How to reach you]

Tone: Professional, authentic, confident but humble
Target length: 500-600 words
Format: Well-structured with clear sections
```

## API reference prompts

### Template: Endpoint documentation

```markdown
Generate API reference documentation for this endpoint:

## Endpoint details
- Method: [GET/POST/PUT/DELETE]
- Path: [/path/to/endpoint]
- Purpose: [What this endpoint does]
- Authentication: [Required/Optional - type]

## Request parameters

Path parameters:
- [param]: [type, required/optional]: [Description]

Query parameters:
- [param]: [type, required/optional]: [Description]

Headers:
- [header]: [Description]

Body parameters (if applicable):
- [param]: [type, required/optional]: [Description]

## Response format

Success ([status code]):
[Describe response structure]

Fields:
- [field]: [type]: [Description]

Error responses:
- [status]: [Description and when it occurs]
- [status]: [Description and when it occurs]

## Rate limiting
[If applicable: requests per time period]

## Example

Request:
```[language]
[Complete example request]
```

Response ([status]):
```json
[Complete example response with realistic data]
```

Generate clear, concise API reference documentation.
Target audience: [Backend developers / Frontend developers / etc.]
Tone: Technical, precise, professional
Include all sections listed above.
```

### Template: API overview

```markdown
Create an API overview page:

## API information
- Name: [API name]
- Purpose: [What this API enables]
- Version: [Current version]
- Base URL: [https://api.example.com/v1]

## Key features
- [Feature 1]
- [Feature 2]
- [Feature 3]

## Authentication
Method: [Bearer token / API key / OAuth 2.0]
How to obtain: [Brief explanation]

## Common use cases
1. [Use case 1]: [Brief description]
2. [Use case 2]: [Brief description]
3. [Use case 3]: [Brief description]

## Quick start
[3-5 step quick start showing simplest possible use]

## Rate limits
[Limits and tier information]

## Support and resources
[Links to other documentation sections]

Tone: Welcoming but technical
Length: 400-500 words
Include code example in quick start
```

## Getting started prompts

### Template: Tool or product onboarding

```markdown
Generate a "Getting Started" guide:

## Product/tool
[Name and brief description]

## Target audience
[Who this is for and their experience level]

## Learning objectives
By the end, users will be able to:
- [Objective 1]
- [Objective 2]
- [Objective 3]

## Prerequisites
What users need before starting:
- [Prerequisite 1]
- [Prerequisite 2]

## Installation
Platform: [macOS / Linux / Windows / All]
Steps:
1. [Step with command if applicable]
2. [Step with command if applicable]
3. [Step with command if applicable]

For each step, show expected output

## Verification
How to confirm installation succeeded:
[Commands and expected output]

## First meaningful task
Walk through accomplishing:
[Specific, simple, successful first task]

Include:
- Clear steps
- Expected output
- Success criteria

## What you accomplished
[Recap of what was achieved]

## Next steps
[Where to go from here]

Tone: Encouraging, supportive, clear
Show expected output for all commands
Include troubleshooting tips for common issues
Target length: 600-800 words
```

## CLI reference prompts

### Template: Command documentation

```markdown
Generate CLI reference documentation for this command:

## Command
[command-name subcommand]

## Purpose
[What this command does in 1-2 sentences]

## Usage
```bash
[command] [subcommand] [OPTIONS] <ARGUMENTS>
```

## Arguments
- `<argument>`: [Description, valid values]

## Options
- `-s, --short <value>`: [Description, default if any]
- `-l, --long`: [Description, boolean flag]
- `--config <file>`: [Description, default if any]

## Behavior
What this command does:
1. [Action 1]
2. [Action 2]
3. [Action 3]

## Exit codes
- 0: Success
- 1: [Error condition]
- 2: [Error condition]

## Environment variables
[If applicable: variables that affect behavior]

## Examples

Example 1: [Basic usage]
```bash
[command with common options]
```
[Explanation of what this does]

Example 2: [Advanced usage]
```bash
[command with multiple options]
```
[Explanation of what this does]

Example 3: [Common scenario]
```bash
[realistic example]
```
[Explanation of what this does]

## Related commands
- [command]: [When to use instead]

Generate comprehensive CLI reference documentation.
Format: Standard man page style
Include all options with short and long forms
Examples should be realistic and well-explained
Target audience: [Developers / DevOps engineers / etc.]
```

## Troubleshooting prompts

### Template: Problem-solution documentation

```markdown
Generate troubleshooting documentation for this problem:

## Problem
[Name or description of the issue]

## Symptoms
Users experience:
- [Symptom 1]
- [Symptom 2]
- [Symptom 3]

## Error message (if applicable)
```
[Exact error message text]
```

## Common causes
This problem usually occurs because:
1. [Cause 1]
2. [Cause 2]
3. [Cause 3]

## Diagnosis
How to identify the root cause:

Step 1: [Diagnostic command or check]
```bash
[command if applicable]
```
[What to look for in output]

Step 2: [Next diagnostic step]
[What this reveals]

## Solutions

If [condition from diagnosis]:
```bash
[Solution commands]
```
[Explanation of what this does]

If [different condition]:
```bash
[Alternative solution commands]
```
[Explanation of what this does]

## Prevention
To avoid this problem in the future:
- [Prevention tip 1]
- [Prevention tip 2]

## Related issues
[Links to related problems]

Tone: Calm, helpful, systematic
Include complete diagnostic steps
Provide multiple solutions for different root causes
Target audience: [User type and experience level]
```

## Conceptual guide prompts

### Template: Technical concept explanation

```markdown
Generate a conceptual guide explaining:

## Concept
[Name of concept or technology]

## What it is
[Clear definition in 2-3 sentences]

## Why it matters
[Practical importance and use cases]

## Key concepts
Break down into understandable parts:
- [Sub-concept 1]: [Explanation]
- [Sub-concept 2]: [Explanation]
- [Sub-concept 3]: [Explanation]

## How it works
[Step-by-step explanation of the mechanism]

Use analogy if helpful: [Analogy relating to familiar concept]

## Real-world examples
Example 1: [Concrete example]
[How the concept applies]

Example 2: [Different scenario]
[How the concept applies]

## Trade-offs and considerations
Advantages:
- [Advantage 1]
- [Advantage 2]

Disadvantages:
- [Disadvantage 1]
- [Disadvantage 2]

## When to use
This approach is appropriate when:
- [Scenario 1]
- [Scenario 2]

This approach is not appropriate when:
- [Scenario 1]
- [Scenario 2]

## Common misconceptions
- Misconception: [Wrong belief]
  Reality: [Correct understanding]

## Related concepts
[Links to related topics]

Tone: Educational, objective, accessible
Target audience: [Experience level]
Include diagrams or analogies where helpful
Length: 800-1000 words
```

## Content refinement prompts

### Template: Clarity improvement

```markdown
Review this documentation section for clarity and conciseness:

[PASTE YOUR CONTENT HERE]

Identify and suggest improvements for:

1. Sentences longer than 25 words
   - Mark the sentence
   - Suggest clearer alternative

2. Passive voice instances
   - Identify passive constructions
   - Convert to active voice

3. Jargon or undefined terms
   - Flag technical terms needing explanation
   - Suggest definitions or links

4. Ambiguous pronouns or references
   - Identify unclear "it", "this", "that"
   - Suggest specific replacements

5. Redundant phrases
   - Find unnecessary repetition
   - Propose removal or consolidation

Do not change:
- Code examples
- Technical terms that must remain precise
- Proper nouns or product names

Maintain:
- Technical accuracy
- Professional tone
- Appropriate level of detail

Provide specific line-by-line suggestions.
```

### Template: Tone consistency

```markdown
Review these sections for tone consistency:

## Section 1: [Title]
[PASTE CONTENT]

## Section 2: [Title]
[PASTE CONTENT]

## Section 3: [Title]
[PASTE CONTENT]

Compare tone across all sections. Identify:

1. Inconsistent use of person (I/we/you)
2. Formality level differences
3. Varying sentence structures
4. Technical depth inconsistencies
5. Different addressing of reader

Target tone should be:
- [Characteristic 1: e.g., Professional but approachable]
- [Characteristic 2: e.g., User-focused (use "you")]
- [Characteristic 3: e.g., Confident and precise]
- [Characteristic 4: e.g., Encouraging]

Suggest specific changes to make tone consistent.
Maintain technical accuracy.
Preserve appropriate technical language.
```

### Template: Technical accuracy review

```markdown
Review this technical documentation for potential accuracy issues:

[PASTE YOUR CONTENT HERE]

Context:
- Topic: [Subject matter]
- Target audience: [Who reads this]
- Technology/platform: [What it documents]

Check for and flag:

1. Potentially incorrect technical statements
   - Flag as question: "Is it accurate that...?"
   - Note why you question it

2. Ambiguous or imprecise technical language
   - Identify vague technical claims
   - Suggest more precise wording

3. Missing important caveats or limitations
   - Note where qualifications needed
   - Suggest what to add

4. Outdated practices or deprecated features
   - Flag anything that might be outdated
   - Note current best practices

5. Code examples that might not work
   - Check for syntax issues
   - Verify imports and setup
   - Flag unrealistic examples

Do not make assumptions or corrections.
Phrase concerns as questions for human verification.
Focus on technical accuracy, not style.
```

### Template: Example enhancement

```markdown
Review and improve this code example:

```[language]
[PASTE CODE EXAMPLE HERE]
```

Context:
- Documentation type: [API reference / Tutorial / etc.]
- Target audience: [Experience level]
- Purpose: [What example demonstrates]

Improve by:

1. Variable naming
   - Replace single letters with meaningful names
   - Use conventional naming for the language

2. Error handling
   - Add appropriate error handling
   - Or explicitly note it's omitted for brevity

3. Imports and setup
   - Include all necessary imports
   - Show any required setup steps

4. Comments
   - Add comments explaining key steps
   - Keep comments focused and helpful

5. Production readiness
   - Make production-ready if appropriate
   - Or mark clearly as simplified example

Provide:
- Improved code example
- Explanation of changes made
- Any caveats or notes needed

Maintain:
- Core demonstration purpose
- Clarity and readability
- Language best practices
```

## Case study prompts

### Template: Project case study

```markdown
Generate a case study for this documentation sample:

## Project information
- Sample name: [Title of documentation]
- Documentation type: [API reference / Tutorial / etc.]
- Topic: [What you documented]
- Approach: [Open source / Fictional / Own project]
- Target audience: [Who this is for]

## Project context
Why this sample was created:
[Explain motivation and goals]

## Research and planning
How I gathered information:
- [Research method 1]
- [Research method 2]
- [Research method 3]

Key decisions made:
- [Decision 1 and rationale]
- [Decision 2 and rationale]

## Information architecture
How I organized the content:
- [Organizational approach]
- [Why this structure]
- [Alternative considered and rejected]

## Content creation process
Step 1: [What you did]
Step 2: [What you did]
Step 3: [What you did]

## AI collaboration
Tool used: [Claude / GPT-4 / etc.]

What AI generated:
- [Section 1: percentage and approach]
- [Section 2: percentage and approach]

What I did manually:
- [Technical verification]
- [Examples creation]
- [Domain expertise]

Prompts used: [Link to saved prompts]

## Challenges and solutions
Challenge 1: [What was difficult]
Solution: [How you solved it]

Challenge 2: [What was difficult]
Solution: [How you solved it]

## Skills demonstrated
This sample shows:
- [Skill 1]
- [Skill 2]
- [Skill 3]

## Outcomes and learning
What worked well:
- [Success 1]
- [Success 2]

What I would improve:
- [Improvement 1]
- [Improvement 2]

Key learnings:
- [Learning 1]
- [Learning 2]

Link to documentation: [URL or path]

Tone: Professional, reflective, honest
Show both successes and challenges
Be specific about process and methods
Length: 600-800 words
```

## Saving and organizing prompts

### Create a prompts directory

Organize your prompts for reuse:

```
prompts/
├── homepage-prompts.md
├── about-page-prompts.md
├── api-reference-prompts.md
├── getting-started-prompts.md
├── cli-reference-prompts.md
├── troubleshooting-prompts.md
├── conceptual-guide-prompts.md
├── refinement-prompts.md
└── case-study-prompts.md
```

### Document prompt effectiveness

In each prompt file, note:

```markdown
# [Documentation Type] Prompts

## Prompt version: 2.0
## Last updated: 2024-11-15

## What works well
- [Observation about effective elements]
- [What produces good results]

## What needs improvement
- [Areas where output requires heavy editing]
- [Aspects that need more specificity]

## Iterations made
- v1.0: Initial version
- v1.1: Added [specific improvement]
- v2.0: Refined [aspect] based on results

## Example output
[Link to documentation created with this prompt]
```

## Tips for adapting templates

### Make prompts more specific

Generic prompt:
```
Write API documentation.
```

Specific prompt:
```
Generate API reference documentation for a POST /events endpoint...
[Full detailed template from above]
```

### Include examples

Add "Follow this pattern:" sections with concrete examples from similar documentation.

### Iterate based on results

After using a template:
1. Save the output
2. Note what worked well
3. Identify what needed editing
4. Update template for next use
5. Version your prompts

### Maintain a prompt library

Keep successful prompts for reuse across projects.

## Related resources

- [Tutorial Step 4: Write content](../tutorial/step-4-write-content.md)
- [AI collaboration reference](../reference/ai-collaboration.md)
- [Content types reference](../reference/content-types.md)
