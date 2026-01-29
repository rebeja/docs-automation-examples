# Step 5: Iterate Prompts

This is where the magic happens. You'll take your improvement list from Step 4 and systematically refine your prompts to achieve high-quality categorization.

!!! info "Time Estimate"
    30-60 minutes (iterative)

!!! success "Key Principle"
    **"Plans are faster to iterate than code."**
    
    The same applies to prompts: Refining prompts is faster than rewriting code. Small changes to your categorization instructions can dramatically improve results.

## What You'll Accomplish

By the end of this step:

- ✅ Understanding of prompt engineering basics
- ✅ Refined categorization instructions
- ✅ Testing methodology for improvements
- ✅ 85%+ categorization accuracy
- ✅ Ready-to-use automation

## Understanding the Current Prompt

### 1. Review the Base Prompt

Open `prompts/categorization_prompt.txt`:

```bash
cd 01-release-notes-automation
cat prompts/categorization_prompt.txt
```

**Initial version (simple):**

```
You are helping categorize GitHub commits for release notes.

Review the following commits and categorize each one:

Categories:
- New Features: Wholly new capabilities that didn't exist before
- Enhancements: Improvements to existing features
- Bug Fixes: Corrections to existing functionality
- Documentation: Content updates, typo fixes, documentation improvements

Exclusions (do not include):
- Typo fixes in code comments
- Internal tooling changes
- Work-in-progress commits
- Merge commits without meaningful changes

Commits to categorize:
{COMMITS}

Format your response as:

## New Features
- [commit message] - Brief explanation if needed

## Enhancements
- [commit message] - Brief explanation if needed

## Bug Fixes
- [commit message] - Brief explanation if needed

## Documentation
- [commit message] - Brief explanation if needed

If a commit doesn't fit any category or should be excluded, omit it from the output.
```

### 2. Identify Weaknesses

Based on your Step 4 review, the prompt might be:

- ❌ Too vague on category definitions
- ❌ Missing specific keyword indicators
- ❌ Insufficient examples
- ❌ Incomplete exclusion rules
- ❌ Unclear about edge cases

## The Iteration Process

Follow this cycle: **Test → Analyze → Refine → Repeat**

### Iteration 1: Add Specific Examples

**Problem:** AI confused about features vs enhancements

**Solution:** Add concrete examples to each category

Create `prompts/categorization_prompt_v2.txt`:

```
You are helping categorize GitHub commits for release notes.

Review the following commits and categorize each one:

Categories with Examples:

**New Features** - Wholly new capabilities that didn't exist before
Examples:
- "Add user authentication system" ✅
- "Create new dashboard view" ✅
- "Introduce webhook support" ✅
NOT examples:
- "Improve existing search" ❌ (this is an enhancement)
- "Update authentication flow" ❌ (enhancement to existing feature)

**Enhancements** - Improvements to existing features
Examples:
- "Improve search performance by 50%" ✅
- "Update API response format" ✅
- "Optimize database queries" ✅
NOT examples:
- "Add search feature" ❌ (this is a new feature)
- "Fix search bug" ❌ (this is a bug fix)

**Bug Fixes** - Corrections to existing functionality
Examples:
- "Fix memory leak in parser" ✅
- "Resolve login timeout issue" ✅
- "Correct validation logic" ✅
NOT examples:
- "Improve validation performance" ❌ (this is an enhancement)
- "Add validation to new field" ❌ (part of new feature)

**Documentation** - Content updates, guides, API docs
Examples:
- "Update API documentation" ✅
- "Fix typo in README" ✅
- "Add usage examples to guide" ✅

Exclusions (do not include):
- Commits containing: "WIP", "temp", "test only", "internal"
- Commits starting with: "Merge pull request", "chore:", "ci:"
- Commits from paths: /tests/, /internal-tools/, /.github/
- Typo fixes in code comments
- Dependency updates (unless user-facing)

Commits to categorize:
{COMMITS}

Format your response as:

## New Features
- [commit message] - Brief explanation if needed

## Enhancements
- [commit message] - Brief explanation if needed

## Bug Fixes
- [commit message] - Brief explanation if needed

## Documentation
- [commit message] - Brief explanation if needed

If a commit doesn't fit any category or should be excluded, omit it from the output.
```

**Test this version:**

```bash
python generate_release_notes.py \
  --repo octocat/Hello-World \
  --since 2024-01-01 \
  --prompt prompts/categorization_prompt_v2.txt \
  --output release_notes_v2.md
```

**Compare results:**

```bash
diff release_notes.md release_notes_v2.md
```

**Measure improvement:**

- Did categorization accuracy increase?
- Are features vs enhancements clearer?
- Were more appropriate items excluded?

### Iteration 2: Add Keyword Indicators

**Problem:** Still some confusion on edge cases

**Solution:** Add explicit keyword guidance

Create `prompts/categorization_prompt_v3.txt`:

```
[Keep everything from v2, but add this section after categories:]

Keyword Indicators:

**New Features keywords:**
- "add", "new", "create", "introduce", "implement"
- BUT only if describing wholly new functionality

**Enhancements keywords:**
- "improve", "update", "enhance", "optimize", "increase", "better"
- "refactor" (if improves existing)

**Bug Fixes keywords:**
- "fix", "bug", "resolve", "issue", "correct", "repair"
- "hotfix", "patch"

**Documentation keywords:**
- "docs", "documentation", "readme", "guide"
- "typo", "spelling" (in documentation only)

When keywords conflict (e.g., "add improvement"), prioritize based on:
1. Is this a completely new capability? → New Feature
2. Does this improve something that exists? → Enhancement
3. Does this correct unintended behavior? → Bug Fix
```

**Test and compare:**

```bash
python generate_release_notes.py \
  --repo octocat/Hello-World \
  --since 2024-01-01 \
  --prompt prompts/categorization_prompt_v3.txt \
  --output release_notes_v3.md
```

### Iteration 3: Refine Exclusions

**Problem:** Internal changes still appearing

**Solution:** Add comprehensive exclusion patterns

```
[Add to exclusion section:]

Exclusions (do not include):

**By keywords:**
- Contains: "WIP", "wip", "work in progress"
- Contains: "temp", "temporary", "TODO", "FIXME"
- Contains: "test only", "testing", "test coverage"
- Contains: "internal", "internal only", "for team"

**By commit prefix:**
- Starts with: "Merge pull request", "Merge branch"
- Starts with: "chore:", "ci:", "build:", "test:"
- Starts with: "Revert", "Bump version"

**By file path patterns:**
- Changes only in: /tests/, /test/, /__tests__/
- Changes only in: /internal/, /scripts/, /.github/
- Changes only in: package-lock.json, Gemfile.lock, yarn.lock

**By author:**
- Bot commits: dependabot[bot], renovate[bot]
- CI systems: github-actions[bot]

**By description content:**
- Only formatting changes (prettier, linting)
- Only whitespace changes
- Only comment changes (unless in documentation files)

When unsure if something should be excluded, include it with a note.
```

## Measuring Success

After each iteration, calculate:

### Categorization Accuracy

```
Accuracy = Correct Categories / Total Commits × 100%
```

| Version | Accuracy | Notes |
|---------|----------|-------|
| v1 (initial) | 65% | Many feature/enhancement confusions |
| v2 (with examples) | 78% | Better but still some issues |
| v3 (with keywords) | 88% | Much improved |
| v4 (refined exclusions) | 92% | Production ready |

### Time Savings

```
Manual Time - (Automation Time + Review Time) = Time Saved
```

**Example:**

- Manual process: 90 minutes
- Automation run: 30 seconds
- Review/edit draft: 15 minutes
- **Time saved: 74.5 minutes** (83% reduction)

### Quality Metrics

Track over multiple runs:

- False positives (incorrectly included) → Target: <5%
- False negatives (missed items) → Target: <3%
- Miscategorizations → Target: <10%

## Advanced Refinements

### Adding Contextual Rules

```
Special handling:

**Security updates:**
Categorize as Bug Fixes even if adding new validation, because fixing security issue

**Breaking changes:**
Mark as Enhancements with "(Breaking Change)" prefix

**Deprecations:**
Categorize as Enhancements with "(Deprecation Notice)" prefix

**Performance improvements:**
Categorize as Enhancements unless fixing a performance bug
```

### Audience-Specific Variations

Create different prompts for different audiences:

**Internal release notes** (`prompts/internal_categorization.txt`):
- Include internal tool improvements
- More technical language OK
- Include infrastructure changes

**External release notes** (`prompts/external_categorization.txt`):
- Exclude all internal items
- Focus on user-facing changes only
- Use customer-friendly language

**Use with:**
```bash
python generate_release_notes.py \
  --repo your/repo \
  --since 2024-01-01 \
  --prompt prompts/external_categorization.txt \
  --output external_release_notes.md
```

## Testing Methodology

### Regression Testing

Create a test set of commits with known correct categorizations:

1. Save 20-30 commits with their correct categories
2. Test each prompt version against this set
3. Track accuracy over iterations
4. Ensure new refinements don't break previous fixes

### A/B Comparison

```bash
# Generate with two prompt versions
python generate_release_notes.py \
  --repo your/repo \
  --since 2024-01-01 \
  --prompt prompts/v3.txt \
  --output notes_v3.md

python generate_release_notes.py \
  --repo your/repo \
  --since 2024-01-01 \
  --prompt prompts/v4.txt \
  --output notes_v4.md

# Compare side by side
diff -y notes_v3.md notes_v4.md
```

## When to Stop Iterating

You've reached a good stopping point when:

- ✅ Accuracy is 85%+ consistently
- ✅ Time saved is significant (>70%)
- ✅ Manual review is manageable (<20 minutes)
- ✅ No new issues in last 2-3 iterations
- ✅ Prompt changes are becoming very minor

!!! warning "Diminishing Returns"
    Going from 85% to 95% accuracy might take more time than the automation saves. Know when "good enough" is actually excellent.

## Common Patterns That Work

Based on real projects:

1. **Explicit examples** beat vague descriptions
2. **Keyword lists** help with boundary cases
3. **Negative examples** ("NOT this") clarify confusion
4. **Specific exclusions** more effective than general rules
5. **Shorter prompts with clear structure** > long rambling prompts

## Your Final Prompt

By now, you should have a refined prompt that:

- ✅ Clearly defines each category with examples
- ✅ Includes keyword indicators
- ✅ Has comprehensive exclusion rules
- ✅ Handles your specific edge cases
- ✅ Matches your documented manual process

Save this as your production prompt!

## What You've Learned

In this step, you:

- ✅ Understood prompt engineering basics
- ✅ Iteratively refined categorization instructions
- ✅ Added examples, keywords, and exclusions
- ✅ Measured improvement objectively
- ✅ Achieved production-ready accuracy
- ✅ Developed testing methodology

## You're Done! 🎉

Congratulations! You've built your first documentation automation using AI coding agents.

### Next Steps

- **Integrate into workflow** - Use for your next release
- **Share with team** - Show others how to use it
- **Build on success** - Try other automation opportunities
- **Join community** - Share learnings in Write the Docs

---

[View All Examples →](../examples/prompt-evolution.md){ .md-button } [Back to Tutorial Home](index.md){ .md-button }

!!! tip "Keep Learning"
    The skills you've learned here—documenting processes, prompt engineering, iterative refinement—apply to ALL automation projects, not just release notes.
