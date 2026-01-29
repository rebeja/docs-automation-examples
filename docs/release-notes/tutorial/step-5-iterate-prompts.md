# Step 5: Iterate prompts

Take your improvement list from Step 4 and refine your prompts to achieve high-quality categorization.

**Time estimate:** 30-60 minutes (iterative)

**Key principle:** Plans are faster to iterate than code. The same applies to prompts. Refining prompts is faster than rewriting code. Small changes to your categorization instructions can improve results.

## Complete these tasks

- Learn prompt engineering basics
- Refine categorization instructions
- Use testing methodology for improvements
- Achieve 85%+ categorization accuracy
- Complete ready-to-use automation

## Understand the current prompt

### 1. Review the base prompt

Open `prompts/categorization_prompt.txt`:

```bash
cd 01-release-notes-automation
cat prompts/categorization_prompt.txt
```

Initial version (simple):

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

### 2. Identify weaknesses

The prompt might have these issues based on your Step 4 review:

- Too vague on category definitions
- Missing specific keyword indicators
- Insufficient examples
- Incomplete exclusion rules
- Unclear about edge cases

## Follow the iteration process

Follow this cycle: Test → Analyze → Refine → Repeat

### Iteration 1: Add specific examples

Problem: AI confused about features versus enhancements

Solution: Add concrete examples to each category

Create `prompts/categorization_prompt_v2.txt`:

```
You are helping categorize GitHub commits for release notes.

Review the following commits and categorize each one:

Categories with Examples:

**New Features** - Wholly new capabilities that didn't exist before
Examples:
- "Add user authentication system" (Correct)
- "Create new dashboard view" (Correct)
- "Introduce webhook support" (Correct)
NOT examples:
- "Improve existing search" (This is an enhancement)
- "Update authentication flow" (Enhancement to existing feature)

**Enhancements** - Improvements to existing features
Examples:
- "Improve search performance by 50%" (Correct)
- "Update API response format" (Correct)
- "Optimize database queries" (Correct)
NOT examples:
- "Add search feature" (This is a new feature)
- "Fix search bug" (This is a bug fix)

**Bug Fixes** - Corrections to existing functionality
Examples:
- "Fix memory leak in parser" (Correct)
- "Resolve login timeout issue" (Correct)
- "Correct validation logic" (Correct)
NOT examples:
- "Improve validation performance" (This is an enhancement)
- "Add validation to new field" (Part of new feature)

**Documentation** - Content updates, guides, API docs
Examples:
- "Update API documentation" (Correct)
- "Fix typo in README" (Correct)
- "Add usage examples to guide" (Correct)

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

Test this version:

```bash
python generate_release_notes.py \
  --repo octocat/Hello-World \
  --since 2024-01-01 \
  --prompt prompts/categorization_prompt_v2.txt \
  --output release_notes_v2.md
```

Compare results:

```bash
diff release_notes.md release_notes_v2.md
```

Measure improvement:

- Categorization accuracy increased
- Features versus enhancements clearer
- More appropriate items excluded

### Iteration 2: Add keyword indicators

Problem: Some confusion on edge cases

Solution: Add explicit keyword guidance

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

Test and compare:

```bash
python generate_release_notes.py \
  --repo octocat/Hello-World \
  --since 2024-01-01 \
  --prompt prompts/categorization_prompt_v3.txt \
  --output release_notes_v3.md
```

### Iteration 3: Refine exclusions

Problem: Internal changes still appearing

Solution: Add comprehensive exclusion patterns

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

## Measure success

Calculate these metrics after each iteration:

### Categorization accuracy

```
Accuracy = Correct Categories / Total Commits × 100%
```

| Version | Accuracy | Notes |
|---------|----------|-------|
| v1 (initial) | 65% | Many feature/enhancement confusions |
| v2 (with examples) | 78% | Better but still some issues |
| v3 (with keywords) | 88% | Much improved |
| v4 (refined exclusions) | 92% | Production ready |

### Time savings

```
Manual Time - (Automation Time + Review Time) = Time Saved
```

Example:

- Manual process: 90 minutes
- Automation run: 30 seconds
- Review or edit draft: 15 minutes
- Time saved: 74.5 minutes (83% reduction)

### Quality metrics

Track over multiple runs:

- False positives (incorrectly included) → Target: less than 5%
- False negatives (missed items) → Target: less than 3%
- Miscategorizations → Target: less than 10%

## Add advanced refinements

### Add contextual rules

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

### Create audience-specific variations

Create different prompts for different audiences:

Internal release notes (`prompts/internal_categorization.txt`):
- Include internal tool improvements
- Use technical language
- Include infrastructure changes

External release notes (`prompts/external_categorization.txt`):
- Exclude all internal items
- Focus on user-facing changes only
- Use customer-friendly language

Use with:
```bash
python generate_release_notes.py \
  --repo your/repo \
  --since 2024-01-01 \
  --prompt prompts/external_categorization.txt \
  --output external_release_notes.md
```

## Use testing methodology

### Run regression testing

Create a test set of commits with known correct categorizations:

1. Save 20-30 commits with their correct categories
2. Test each prompt version against this set
3. Track accuracy over iterations
4. Ensure new refinements don't break previous fixes

### Compare A/B results

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

## Know when to stop iterating

Stop iterating when these conditions are met:

- Accuracy is 85%+ consistently
- Time saved is significant (more than 70%)
- Manual review is manageable (less than 20 minutes)
- No new issues in last 2-3 iterations
- Prompt changes are becoming minor

Going from 85% to 95% accuracy might take more time than the automation saves. Recognize when "good enough" is excellent.

## Apply common patterns

These patterns work in real projects:

1. **Explicit examples** beat vague descriptions
2. **Keyword lists** help with boundary cases
3. **Negative examples** ("NOT this") clarify confusion
4. **Specific exclusions** more effective than general rules
5. **Shorter prompts with clear structure** better than long rambling prompts

## Create your final prompt

Your refined prompt should have these elements:

- Clear definitions for each category with examples
- Keyword indicators
- Comprehensive exclusion rules
- Handling for your specific edge cases
- Match to your documented manual process

Save this as your production prompt.

## Summary

You learned prompt engineering basics, iteratively refined categorization instructions, added examples, keywords, and exclusions, measured improvement objectively, achieved production-ready accuracy, and developed testing methodology.

## Next steps

You built your first documentation automation using AI coding agents.

- Integrate into workflow - Use for your next release
- Share with team - Show others how to use it
- Build on success - Try other automation opportunities
- Join community - Share learnings in Write the Docs

---

[View all examples](../examples/prompt-evolution.md) | [Back to tutorial home](index.md)

The skills you learned here—documenting processes, prompt engineering, iterative refinement—apply to all automation projects, not just release notes.
