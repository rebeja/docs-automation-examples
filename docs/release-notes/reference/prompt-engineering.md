# Prompt Engineering Reference

Complete guide to writing effective categorization prompts for release notes automation.

## What is Prompt Engineering?

Prompt engineering is the practice of crafting clear, specific instructions that help AI understand your categorization standards and produce consistent, high-quality results.

**Key insight:** Your prompt is essentially documentation of your manual process, translated into instructions for AI.

## Anatomy of a Good Prompt

An effective categorization prompt has five key components:

### 1. Clear Purpose Statement

Tell the AI what it's doing:

```
You are helping categorize GitHub commits for release notes.
```

### 2. Category Definitions

Define each category with:
- **Clear definition** - What belongs in this category
- **Positive examples** - Commits that should be categorized here
- **Negative examples** - Commits that should NOT be here
- **Keyword indicators** - Words that suggest this category

**Example:**

```
**New Features** - Wholly new capabilities that didn't exist before

Examples:
- "Add user authentication system" (Correct)
- "Create new dashboard view" (Correct)

NOT examples:
- "Improve existing search" (This is an enhancement)

Keywords: "add", "new", "create", "introduce"
```

### 3. Exclusion Rules

Be specific about what to exclude:

```
Exclusions (do not include):
- Commits containing: "WIP", "temp", "test only"
- Commits starting with: "Merge pull request", "chore:"
- Commits from paths: /tests/, /.github/
- By author: dependabot[bot]
```

### 4. Decision Rules

Handle edge cases with clear priority:

```
When keywords conflict:
1. Is this completely new? → New Feature
2. Does it improve existing? → Enhancement
3. Does it fix a bug? → Bug Fix
```

### 5. Output Format

Specify exactly how you want the response:

```
Format your response as:

## New Features
- [commit message] - Brief explanation if needed

## Enhancements
- [commit message] - Brief explanation if needed
```

## Common Prompt Patterns

### Pattern 1: Simple Categorization

**Use when:** Basic four-category release notes

```
Categories:
- New Features: Wholly new capabilities
- Enhancements: Improvements to existing
- Bug Fixes: Corrections only
- Documentation: Content updates
```

**Pros:** Quick to write, easy to understand  
**Cons:** May not handle edge cases well

### Pattern 2: Detailed with Examples

**Use when:** Need better accuracy and consistency

```
**New Features**
Definition: [clear definition]
Examples: [3-5 real examples]
NOT Examples: [2-3 counter-examples]
Keywords: [list of indicators]
```

**Pros:** Much better accuracy (15-20% improvement)  
**Cons:** Takes time to create examples

### Pattern 3: Domain-Specific

**Use when:** Specialized repositories (frontend, backend, docs)

```
**Frontend: New Components**
- New React components
- New UI pages
- New user-facing features

**Frontend: UI Improvements**
- Component updates
- Style changes
- Layout improvements
```

**Pros:** Highly accurate for specific domains  
**Cons:** Requires separate prompts per repository type

## Iteration Strategy

### Start Simple

Begin with basic definitions:

```
Categories:
- Features
- Enhancements
- Fixes
- Docs
```

### Add Examples

After first test run, add specific examples:

```
**Features**
Examples:
- "Add user login" (Correct)
- "Create API endpoint" (Correct)
```

### Refine Based on Errors

For each miscategorization, add counter-examples:

```
**Features**
NOT Examples:
- "Improve login performance" (Enhancement)
```

### Add Keywords

For remaining issues, add keyword guidance:

```
**Features**
Keywords: "add", "new", "create"
Only when describing wholly new functionality
```

## Testing Your Prompt

### Create a Test Set

Save 20-30 commits with known correct categories:

```json
[
  {
    "commit": "Add user authentication",
    "correct_category": "New Features"
  },
  {
    "commit": "Improve search speed",
    "correct_category": "Enhancements"
  }
]
```

### Measure Accuracy

```
Accuracy = Correct / Total × 100%
```

**Targets:**
- First iteration: 60-70%
- After refinement: 85-90%
- Optimized: 90-95%

### Track Improvements

| Version | Changes | Accuracy | Notes |
|---------|---------|----------|-------|
| v1 | Basic definitions | 65% | Too vague |
| v2 | Added examples | 78% | Better boundaries |
| v3 | Added keywords | 88% | Production ready |

## Common Issues and Solutions

### Issue: Features vs Enhancements Confused

**Problem:** AI categorizes improvements as features

**Solution:**
```
**New Features** - Must be COMPLETELY new
Examples: "Add authentication" (Correct)
NOT: "Add better error messages" (Enhancement)

**Enhancements** - Improvements to EXISTING
Examples: "Improve search performance" (Correct)
NOT: "Add search feature" (New feature)
```

### Issue: Internal Changes Appearing

**Problem:** CI/CD, tests, internal tools in output

**Solution:**
```
Exclusions:
- Commits containing: "internal", "ci:", "test:"
- From paths: /tests/, /.github/, /scripts/
- By author: github-actions[bot], dependabot[bot]
```

### Issue: Inconsistent Categorization

**Problem:** Similar commits categorized differently

**Solution:** Add more examples from your actual repository:

```
From YOUR repository:
- "Add caching layer" → New Feature (new capability)
- "Improve cache performance" → Enhancement (improves existing)
- "Fix cache corruption" → Bug Fix (corrects behavior)
```

## Best Practices

### Do

- **Use examples from your repository** - Domain-specific examples work best
- **Test iteratively** - Measure improvement after each change
- **Be specific** - "Add new capability" is clearer than "Add something"
- **Include counter-examples** - "NOT this" clarifies boundaries
- **Document your decisions** - Keep notes on why you categorized things

### Don't

- **Don't make prompts too long** - Over 1500 words has diminishing returns
- **Don't use vague language** - "Generally", "usually", "often" are unclear
- **Don't assume context** - AI doesn't know your team's conventions
- **Don't skip testing** - Assumptions about accuracy are often wrong
- **Don't aim for perfection** - 90% is often better ROI than 98%

## Prompt Templates

### Basic Template

```
You are helping categorize GitHub commits for release notes.

Categories:
- [Category 1]: [Definition]
- [Category 2]: [Definition]
- [Category 3]: [Definition]

Exclusions:
- [Exclusion rule 1]
- [Exclusion rule 2]

Commits to categorize:
{COMMITS}

Format: [Your desired output format]
```

### Advanced Template

See [Prompt Evolution Example](../examples/prompt-evolution.md) for a complete production-ready template.

## Further Reading

- [Tutorial Step 5: Iterate Prompts](../tutorial/step-5-iterate-prompts.md)
- [Prompt Evolution Example](../examples/prompt-evolution.md)
- [Sample Outputs](../examples/sample-outputs.md)

---

**Need help?** Check the [FAQ](../faq.md) or [Troubleshooting Guide](../troubleshooting.md).
