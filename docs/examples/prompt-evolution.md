# Prompt Evolution Example

This page shows the real journey of refining a release notes categorization prompt from simple to production-ready.

## The Journey: Simple → Refined

### Version 1: Initial (Simple)

**When:** First attempt after documenting manual process

**Approach:** Basic categories with minimal guidance

```
Categorize GitHub commits as:
- New Features: New capabilities
- Enhancements: Improvements
- Bug Fixes: Corrections
- Documentation: Docs updates

Commits:
{COMMITS}
```

**Results:**

- ✅ Basic categorization working
- ❌ 35% of commits miscategorized
- ❌ Internal changes included
- ❌ Feature vs Enhancement boundary unclear
- ❌ No exclusion logic

**Accuracy: 65%** - Not usable

---

### Version 2: Add Definitions

**When:** After reviewing first test results

**Changes:** Added clearer category definitions

```
Categorize GitHub commits as:

Categories:
- New Features: Wholly new capabilities that didn't exist before
- Enhancements: Improvements to existing features  
- Bug Fixes: Corrections to existing functionality
- Documentation: Content updates, typo fixes, documentation improvements

Exclusions:
- Internal tooling changes
- Work-in-progress commits
- Merge commits

Commits:
{COMMITS}
```

**Results:**

- ✅ Better feature/enhancement distinction
- ✅ Some internal changes filtered
- ❌ Still many edge case confusions
- ❌ "Wholly new" vs "existing" ambiguous
- ❌ Exclusions too vague

**Accuracy: 72%** - Improved but not production-ready

---

### Version 3: Add Examples

**When:** After seeing specific patterns of confusion

**Changes:** Added concrete examples of each category

```
Categorize GitHub commits for release notes.

Categories with examples:

**New Features** - Wholly new capabilities
Examples: "Add user authentication", "Create dashboard view"
Not examples: "Improve search" (enhancement)

**Enhancements** - Improvements to existing
Examples: "Improve search performance", "Update API format"
Not examples: "Add search feature" (new feature)

**Bug Fixes** - Corrections only
Examples: "Fix memory leak", "Resolve timeout"
Not examples: "Improve performance" (enhancement)

**Documentation** - Content updates
Examples: "Update API docs", "Fix typo in README"

Exclusions (do not include):
- Commits containing: "WIP", "temp", "test only"
- Commits starting with: "Merge pull request", "chore:"
- Internal tooling changes

Commits:
{COMMITS}

Format:
## New Features
- [commit message]

## Enhancements
- [commit message]

## Bug Fixes
- [commit message]

## Documentation
- [commit message]
```

**Results:**

- ✅ Feature vs Enhancement much clearer
- ✅ Better exclusion of WIP commits
- ✅ More consistent categorization
- ❌ Still some internal changes leaking
- ❌ Test-related commits sometimes included

**Accuracy: 83%** - Getting close!

---

### Version 4: Refined Production

**When:** After several test runs on different repositories

**Changes:** Added keyword indicators, comprehensive exclusions, and format specifications

```
You are helping categorize GitHub commits for release notes.

Review the following commits and categorize each one according to these standards:

## Categories

### New Features
**Definition:** Wholly new capabilities that didn't exist before

**Examples:**
- "Add user authentication system" ✅
- "Create new dashboard view" ✅
- "Introduce webhook support" ✅

**NOT Examples:**
- "Improve existing search" ❌ (this is an enhancement)
- "Update authentication flow" ❌ (enhancement to existing)

**Keywords:** "add", "new", "create", "introduce", "implement"
(Only if describing wholly new functionality)

### Enhancements
**Definition:** Improvements to existing features or functionality

**Examples:**
- "Improve search performance by 50%" ✅
- "Update API response format" ✅
- "Optimize database queries" ✅

**NOT Examples:**
- "Add search feature" ❌ (new feature)
- "Fix search bug" ❌ (bug fix)

**Keywords:** "improve", "update", "enhance", "optimize", "increase", "better", "refactor"

### Bug Fixes
**Definition:** Corrections to existing functionality that wasn't working as intended

**Examples:**
- "Fix memory leak in parser" ✅
- "Resolve login timeout issue" ✅
- "Correct validation logic error" ✅

**NOT Examples:**
- "Improve validation performance" ❌ (enhancement)
- "Add validation to new field" ❌ (part of new feature)

**Keywords:** "fix", "bug", "resolve", "issue", "correct", "repair", "hotfix", "patch"

### Documentation
**Definition:** Updates to documentation, guides, or API docs

**Examples:**
- "Update API documentation" ✅
- "Fix typo in README" ✅
- "Add usage examples to guide" ✅

**Keywords:** "docs", "documentation", "readme", "guide", "typo" (in docs)

## Exclusions

**Do NOT include commits that:**

**By keywords:**
- Contain: "WIP", "wip", "work in progress", "temp", "temporary"
- Contain: "test only", "testing", "test coverage" (unless adding new test features for users)
- Contain: "internal", "internal only", "for team", "do not publish"

**By commit prefix:**
- Start with: "Merge pull request", "Merge branch"
- Start with: "chore:", "ci:", "build:", "test:", "style:"
- Start with: "Revert", "Bump version", "Update dependencies"

**By file paths:**
- Only change files in: /tests/, /test/, /__tests__/
- Only change files in: /internal/, /scripts/, /.github/, /.ci/
- Only change: package-lock.json, Gemfile.lock, yarn.lock, poetry.lock

**By author:**
- Commits by bots: dependabot[bot], renovate[bot], github-actions[bot]

**By change type:**
- Only formatting changes (prettier, linting, whitespace)
- Only comment updates (unless in documentation files)

## Decision Rules

When keywords conflict (e.g., "add improvement to existing feature"):

1. **Is this a completely new capability users couldn't do before?** → New Feature
2. **Does this improve/enhance something that already exists?** → Enhancement  
3. **Does this correct unintended behavior or bugs?** → Bug Fix
4. **Is this only documentation?** → Documentation

When unsure, default to Enhancement rather than New Feature.

## Output Format

Format your response exactly as:

## New Features
- [commit message] - [Brief explanation if commit message is unclear]

## Enhancements
- [commit message] - [Brief explanation if commit message is unclear]

## Bug Fixes
- [commit message] - [Brief explanation if commit message is unclear]

## Documentation
- [commit message] - [Brief explanation if commit message is unclear]

**Important:**
- Omit any commits that match exclusion criteria
- If a section has no commits, omit that section entirely
- Preserve the commit message but clarify if needed
- Add brief context only if the commit message is vague

## Commits to Categorize

{COMMITS}
```

**Results:**

- ✅ Consistent categorization across different repositories
- ✅ Effective filtering of internal changes
- ✅ Clear decision rules for edge cases
- ✅ Appropriate format and context
- ✅ Minimal manual cleanup needed

**Accuracy: 91%** - Production ready! 🎉

---

## What Changed and Why

### Adding Examples (v1 → v3)

**Problem:** "Wholly new" vs "improvements" was ambiguous

**Solution:** Concrete examples with both positive and negative cases

**Impact:** +18 percentage points in accuracy

### Adding Keywords (v3 → v4)

**Problem:** AI struggling with commits using unexpected wording

**Solution:** Explicit keyword indicators for each category

**Impact:** +8 percentage points in accuracy

### Refining Exclusions (v2 → v4)

**Problem:** Internal changes appearing in release notes

**Solution:** Comprehensive exclusion rules by keyword, prefix, path, and author

**Impact:** Reduced false positives by 85%

### Adding Decision Rules (v4)

**Problem:** Edge cases with conflicting signals

**Solution:** Priority-based decision tree

**Impact:** More consistent categorization of ambiguous commits

## Metrics Summary

| Version | Accuracy | False Positives | False Negatives | Review Time |
|---------|----------|----------------|----------------|-------------|
| v1 | 65% | 25% | 10% | 45 min |
| v2 | 72% | 20% | 8% | 35 min |
| v3 | 83% | 12% | 5% | 20 min |
| v4 | 91% | 4% | 5% | 12 min |

**Time Savings:**

- Manual process: 90 minutes
- v4 automation + review: 12.5 minutes
- **Saved: 77.5 minutes (86% reduction)**

## Lessons Learned

### What Worked

1. **Concrete examples** were more effective than abstract definitions
2. **Negative examples** ("NOT this") clarified boundaries
3. **Keyword lists** helped with pattern matching
4. **Comprehensive exclusions** better than general guidelines
5. **Decision trees** resolved conflicts

### What Didn't Work

1. **Overly complex prompts** (>2000 words) - diminishing returns
2. **Too many categories** (7+ categories became confusing)
3. **Vague language** like "generally" or "usually"
4. **Assuming context** the AI couldn't have
5. **Perfection seeking** (90% is often better ROI than 98%)

### Iteration Strategy

1. **Test with same dataset** to compare versions fairly
2. **Track metrics** systematically (don't rely on gut feel)
3. **Focus on patterns** not individual failures
4. **Stop iterating** when improvements are <3 percentage points
5. **Version control prompts** to enable rollback

## Adapting This for Your Workflow

### Start with Version 3

Don't start from scratch! Begin with v3 structure and customize:

1. Update category definitions to match your standards
2. Add examples from your actual commits
3. Customize exclusions for your repository patterns
4. Test and measure
5. Iterate based on your specific issues

### Repository-Specific Variations

Different repositories may need different prompts:

**Frontend repository:**
- More emphasis on UI/UX improvements
- Exclude: styling-only changes, component refactors

**Backend API repository:**
- Separate category for breaking changes
- Emphasize: endpoint additions, performance
- Exclude: database migration details

**Documentation repository:**
- Simpler categorization (Content vs Structure vs Fixes)
- All commits are "user-facing"
- Focus on impact to readers

### Audience-Specific Variations

**Internal release notes:**
- Include infrastructure improvements
- More technical language
- Keep some "excluded" items

**External release notes:**
- Stricter exclusions
- User-benefit focused
- Customer-friendly language

## Try It Yourself

Use this prompt as your starting point:

1. Copy Version 4 to `prompts/categorization_prompt.txt`
2. Customize examples for your domain
3. Update exclusions for your repository
4. Test and measure accuracy
5. Iterate based on results

---

**Ready to use this?** [Go to Tutorial →](../tutorial/index.md){ .md-button .md-button--primary }
