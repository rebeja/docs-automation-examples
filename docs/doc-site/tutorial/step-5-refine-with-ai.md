# Step 5: Refine with AI

Improve your documentation with AI-assisted editing and refinement.

## Complete these tasks

By the end of this step, you will have:

- Improved writing clarity and conciseness
- Consistent tone across all samples
- Enhanced technical accuracy
- Better code examples
- Professional polish

## Time estimate

1-2 hours

## Overview

This step focuses on using AI as an editing partner rather than a content generator. You will learn to:

- Identify areas needing improvement
- Prompt AI for specific enhancements
- Apply style guides and standards
- Maintain authentic voice while improving quality

## Technique 1: Improve clarity and conciseness

AI excels at identifying verbose or unclear writing.

### Prompt for clarity improvement

```markdown
Review this documentation section for clarity and conciseness:

[Paste your content]

Identify:
1. Sentences that are too long or complex
2. Jargon that should be simplified or explained
3. Passive voice that should be active
4. Redundant phrases
5. Unclear pronouns or references

Suggest specific improvements while maintaining technical accuracy.
Do not change code examples or technical terms that must remain precise.
```

### Example refinement

**Original**:
```markdown
The API endpoint that is used for the creation of new events in the 
system can be accessed by making a POST request to the /events path. 
Authentication is required and this is done through the use of a 
Bearer token that must be included in the Authorization header.
```

**AI-suggested improvement**:
```markdown
Create new events by sending a POST request to `/events`. Include a 
Bearer token in the Authorization header for authentication.
```

### Apply improvements selectively

AI suggestions are not always better. Evaluate each change:

- Is it actually clearer?
- Does it maintain technical precision?
- Does it match the documentation style?
- Is the tone still appropriate?

Accept improvements that genuinely enhance readability. Reject changes that sacrifice accuracy or appropriate technical language.

## Technique 2: Ensure consistent tone

Documentation should maintain consistent voice across all samples.

### Define your documentation voice

First, document your target voice. Create `style-guide.md`:

```markdown
# Documentation Style Guide

## Voice and tone

- **Professional but approachable**: Technical credibility without stuffiness
- **User-focused**: Address reader as "you", emphasize benefits
- **Confident without arrogance**: State facts clearly, acknowledge limitations
- **Encouraging**: Support learning, celebrate progress
- **Precise**: Use exact technical terms, avoid ambiguity

## Grammar and mechanics

- Active voice preferred (passive acceptable for operations or systems)
- Present tense for documentation
- Second person (you) for instructions
- Sentence case for headings
- Oxford comma in lists

## Specific preferences

- "Set up" (verb), "setup" (noun)
- "Log in" (verb), "login" (noun)
- "Command line" not "command-line" when used as noun
- Use "to" not "in order to"
- Use "because" not "since" for causation

## Code formatting

- Inline code: `variable`, `function()`, `command`
- Code blocks: Always specify language
- File paths: `path/to/file.md`
- Commands: Show with prompt or without based on context
```

### Prompt for tone consistency

```markdown
Review these two documentation sections for tone consistency:

## Section 1: Getting Started Guide
[Paste content]

## Section 2: API Reference
[Paste content]

Compare the voice and tone. Identify:
1. Inconsistent use of person (I/we/you)
2. Formality level differences
3. Sentence structure patterns that differ
4. Terminology inconsistencies

Suggest specific changes to make tone consistent across both sections.
Target voice: Professional, user-focused, encouraging, technically precise.
```

### Review for consistency

Check these common inconsistencies:

- Switching between "you" and "we"
- Varying levels of formality
- Inconsistent command presentation (`$` prompt or no prompt)
- Mixed capitalization styles
- Inconsistent use of contractions

### Batch consistency fixes

Use AI to apply consistent patterns:

```markdown
Update all code blocks in this document to follow this pattern:

Commands shown with bash prompt:
```bash
$ docker ps
CONTAINER ID   IMAGE     COMMAND    CREATED    STATUS
abc123         nginx     "nginx"    2m ago     Up 2m
```

But output examples without prompt:
```
CONTAINER ID   IMAGE     COMMAND    CREATED    STATUS
abc123         nginx     "nginx"    2m ago     Up 2m
```

Apply this consistently to all code blocks in:
[Paste document]
```

## Technique 3: Enhance technical accuracy

Use AI to identify potential technical errors or ambiguities.

### Prompt for accuracy review

```markdown
Review this technical documentation for accuracy issues:

[Paste content]

Check for:
1. Potentially incorrect technical statements
2. Ambiguous or imprecise technical language
3. Missing important caveats or limitations
4. Outdated practices or deprecated features
5. Code examples that might not work as shown

Flag concerns without making assumptions. Phrase as questions: 
"Is it accurate that...?" rather than corrections.
```

### Example accuracy review

**Content**:
```markdown
Always use `docker run --rm` to automatically remove containers 
when they stop. This ensures your system stays clean.
```

**AI flags potential issue**:
```markdown
Question: Is it accurate to say "always" use `--rm`? This flag 
removes containers immediately upon exit, which might not be 
desired when:
- Debugging failed containers
- Inspecting container logs after stopping
- Preserving container state for analysis

Consider qualifying this recommendation.
```

### Verify and correct

When AI flags potential issues:

1. Research the technical point
2. Test if possible
3. Update if AI is correct
4. Add caveats or qualifications
5. Improve precision

Never blindly accept AI technical corrections. Always verify.

## Technique 4: Improve code examples

Code examples are critical. Use AI to enhance them.

### Prompt for example improvement

```markdown
Review this code example for improvement:

```python
r = requests.get('https://api.example.com/events/123')
d = r.json()
print(d['name'])
```

Improve by:
1. Using meaningful variable names
2. Adding error handling
3. Including necessary imports
4. Adding comments explaining key steps
5. Making example production-ready or explicitly marking as simplified

Context: This is from an API documentation getting started guide 
for developers learning to use the API.
```

**AI-improved example**:
```python
import requests

# Fetch a specific event by ID
response = requests.get('https://api.example.com/events/123')

# Check if request was successful
if response.status_code == 200:
    event_data = response.json()
    print(f"Event name: {event_data['name']}")
else:
    print(f"Error: {response.status_code}")
```

### Balance realism with clarity

Examples should be:
- **Realistic enough** to be useful
- **Simple enough** to understand quickly
- **Complete enough** to actually run
- **Focused enough** to illustrate the point

Use comments to bridge gaps:

```python
# Error handling omitted for brevity
# In production, handle all possible HTTP status codes
```

## Technique 5: Add helpful callouts

Use admonitions to highlight important information.

### Types of callouts

MkDocs Material supports these admonition types:

```markdown
!!! note
    Additional information that helps understanding.

!!! tip
    Helpful suggestions or best practices.

!!! warning
    Important caveats or potential issues.

!!! danger
    Critical information about breaking changes or data loss.

!!! example
    Code samples or usage examples.
```

### Prompt for callout suggestions

```markdown
Review this documentation and suggest where to add callouts:

[Paste content]

Identify places where:
- NOTE: Would help explain context or background
- TIP: Could provide helpful best practices
- WARNING: Should alert about potential issues
- DANGER: Must warn about critical problems
- EXAMPLE: Could clarify with a code sample

Suggest specific callout text for each recommendation.
```

### Add callouts strategically

Do not overuse callouts. Add them for:
- Security considerations
- Breaking changes
- Common mistakes
- Important prerequisites
- Alternative approaches

Example addition:

**Before**:
```markdown
Run `docker system prune` to clean up unused containers, networks, 
and images. This frees up disk space.
```

**After**:
```markdown
Run `docker system prune` to clean up unused containers, networks, 
and images. This frees up disk space.

!!! warning
    This command removes all unused Docker objects. Review what 
    will be deleted with `docker system prune --dry-run` first.
```

## Technique 6: Enhance navigation and structure

Improve how readers move through your documentation.

### Prompt for structure review

```markdown
Review this documentation structure for improvements:

[Paste table of contents or navigation]

Evaluate:
1. Logical flow of topics
2. Appropriate nesting depth
3. Clear section naming
4. Helpful cross-references
5. Missing sections or topics

Suggest specific structural improvements to enhance usability.
```

### Add strategic cross-references

Link related content:

```markdown
For API authentication details, see [Authentication](authentication.md).

Related guides:
- [Getting Started](getting-started.md)
- [Error Handling](errors.md)
- [Rate Limiting](rate-limits.md)
```

### Improve section headings

Use AI to suggest better headings:

```markdown
Improve these section headings for clarity and scannability:

Current headings:
- Info
- Details
- How to use it
- Things to know
- Problems

These should be:
- Specific and descriptive
- Parallel structure
- Action-oriented where appropriate
- Easy to scan

Suggest improved headings.
```

## Technique 7: Polish for professionalism

Final review for professional presentation.

### Comprehensive review prompt

```markdown
Perform a final review of this documentation:

[Paste content]

Check for:
1. Spelling and grammar errors
2. Broken links
3. Missing code syntax highlighting
4. Inconsistent formatting
5. Unclear transitions between sections
6. Missing prerequisites
7. Incomplete examples
8. Unhelpful error messages in examples

Provide specific fixes for each issue found.
```

### Manual checks AI cannot do

Some checks require human review:

- Links to external sites (test manually)
- Code examples (run and verify)
- Screenshots (if included)
- Realistic data in examples
- Proper attribution of sources
- Accurate version numbers

## Create a refinement checklist

Document your refinement process in `refinement-checklist.md`:

```markdown
# Documentation Refinement Checklist

For each documentation sample, complete:

## Clarity
- [ ] Remove unnecessary words
- [ ] Simplify complex sentences
- [ ] Explain jargon or link to definitions
- [ ] Use active voice where appropriate

## Consistency
- [ ] Tone matches style guide
- [ ] Code examples formatted consistently
- [ ] Headings follow same pattern
- [ ] Terminology used consistently

## Technical accuracy
- [ ] All commands tested
- [ ] Code examples run successfully
- [ ] API details match spec
- [ ] Version numbers correct

## Examples
- [ ] Variable names are meaningful
- [ ] Error handling included or noted as omitted
- [ ] Comments explain key steps
- [ ] Examples are complete enough to use

## Navigation
- [ ] All links work
- [ ] Cross-references added
- [ ] Table of contents updated
- [ ] Related content linked

## Professional polish
- [ ] Spelling and grammar checked
- [ ] Code syntax highlighting added
- [ ] Callouts added where helpful
- [ ] Final review completed
```

## Update case studies with refinement details

Add a refinement section to each case study:

```markdown
## Refinement process

### Initial quality assessment
- [What needed improvement]

### AI-assisted refinement
- Clarity improvements: [Details]
- Consistency fixes: [Details]
- Technical accuracy reviews: [Details]

### Manual enhancements
- Code examples tested and improved
- Cross-references added
- Callouts placed strategically

### Final quality level
- [Self-assessment of quality]

### Refinement time investment
- AI-assisted review: [X minutes]
- Manual improvements: [X minutes]
- Testing and verification: [X minutes]
```

## Summary

You completed these tasks:

- ✓ Improved writing clarity and conciseness
- ✓ Ensured consistent tone across samples
- ✓ Enhanced technical accuracy
- ✓ Improved code examples
- ✓ Added helpful callouts
- ✓ Polished for professional presentation
- ✓ Created refinement checklist
- ✓ Updated case studies

Your documentation samples now meet professional standards.

## Before moving to deployment

Final verification:

- [ ] All documentation samples reviewed
- [ ] Style guide followed consistently
- [ ] Code examples tested
- [ ] Links verified
- [ ] Case studies updated
- [ ] Refinement process documented
- [ ] Professional quality achieved

---

Next step: [Deploy](step-6-deploy.md)
