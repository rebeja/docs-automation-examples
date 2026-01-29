# Step 4: First Run

Time to generate your first automated release notes! In this step, you'll run the script with sample data, then with a real repository, and learn how to evaluate the results.

!!! info "Time Estimate"
    20-30 minutes

## What You'll Accomplish

By the end of this step:

- ✅ First successful run with sample data
- ✅ Release notes generated from real repository
- ✅ Understanding of what to review
- ✅ List of improvements needed
- ✅ Confidence to iterate

## Running with Sample Data

Start with built-in sample data to verify everything works without using API credits.

### 1. Navigate to Project Directory

```bash
cd 01-release-notes-automation
```

### 2. Run with Sample Flag

```bash
python generate_release_notes.py \
  --repo sample/repo \
  --since 2024-01-01 \
  --sample
```

The `--sample` flag uses built-in test commits instead of calling GitHub API.

### 3. Review Output

You should see:

```
Fetching commits from sample/repo since 2024-01-01...
Found 8 sample commits
Categorizing commits using AI...
Generating release notes...
Release notes written to release_notes.md
```

### 4. Open the Generated File

```bash
cat release_notes.md
```

**Example output:**

```markdown
# Release Notes

**Date:** 2024-01-28
**Period:** Since 2024-01-01

## 🎉 New Features

- Add user authentication feature ([abc123](https://github.com/sample/repo/commit/abc123))
- Create dashboard view for analytics ([xyz789](https://github.com/sample/repo/commit/xyz789))

## ✨ Enhancements

- Improve search performance by 50% ([def456](https://github.com/sample/repo/commit/def456))
- Update API response format ([mno345](https://github.com/sample/repo/commit/mno345))

## 🐛 Bug Fixes

- Fix memory leak in parser ([ghi789](https://github.com/sample/repo/commit/ghi789))
- Resolve login timeout issue ([pqr678](https://github.com/sample/repo/commit/pqr678))

## 📝 Documentation

- Update API documentation with new endpoints ([jkl012](https://github.com/sample/repo/commit/jkl012))
```

!!! success "Success!"
    If you see categorized release notes, the automation is working! 🎉

## Running with Real Repository

Now try with an actual GitHub repository.

### 1. Choose a Repository

Options:

**Option A: Use your own repository**
```bash
--repo your-username/your-repo
```

**Option B: Use a public test repository**
```bash
--repo octocat/Hello-World
```

**Option C: Use an Indeed public repository** (if from Indeed)
```bash
--repo indeedeng/proctor
```

### 2. Determine Date Range

Pick a date range with meaningful commits:

```bash
# Last 30 days
--since $(date -d '30 days ago' +%Y-%m-%d)  # Linux/Mac

# Specific date
--since 2024-01-01

# With end date
--since 2024-01-01 --until 2024-01-31
```

### 3. Run the Script

```bash
python generate_release_notes.py \
  --repo octocat/Hello-World \
  --since 2024-01-01
```

### 4. Monitor Progress

You'll see:

```
Fetching commits from octocat/Hello-World since 2024-01-01...
Found 23 commits
Categorizing commits using AI...
Generating release notes...
Release notes written to release_notes.md
```

**Timing:** Typically 10-30 seconds depending on commit count and AI provider.

### 5. Review the Output

```bash
cat release_notes.md
```

Or open in your text editor:

```bash
code release_notes.md    # VS Code
cursor release_notes.md  # Cursor
```

## Evaluating Quality

Now comes the important part: reviewing the output for quality and identifying improvements.

### What to Check

Use this checklist:

#### ✅ Categorization Accuracy

- [ ] Are features actually new features (not enhancements)?
- [ ] Are bug fixes correctly identified?
- [ ] Are enhancements truly improvements (not new features)?
- [ ] Is documentation correctly separated?

#### ✅ Exclusions

- [ ] Were internal-only changes excluded?
- [ ] Were WIP/temp commits filtered out?
- [ ] Were merge commits without substance removed?
- [ ] Were test-only changes excluded?

#### ✅ Formatting

- [ ] Are commit links working?
- [ ] Is the format consistent?
- [ ] Are emoji icons displaying correctly?
- [ ] Is the date/period information accurate?

#### ✅ Completeness

- [ ] Are all user-facing changes included?
- [ ] Are major changes properly represented?
- [ ] Is anything important missing?

### Common Issues

**Issue 1: Enhancements Categorized as Features**

```markdown
## 🎉 New Features
- Improve search performance by 50%  ❌ This is an enhancement!
```

**Why:** Prompt needs clearer distinction between "new" and "improved"

**Fix:** Refine categorization standards (Step 5)

---

**Issue 2: Internal Changes Included**

```markdown
## ✨ Enhancements
- Update CI/CD pipeline configuration  ❌ Internal only!
```

**Why:** Exclusion rules not specific enough

**Fix:** Add explicit exclusion patterns (Step 5)

---

**Issue 3: Vague Descriptions**

```markdown
## 🐛 Bug Fixes
- Fix bug  ❌ Too vague!
```

**Why:** Commit message was vague, AI has nothing to work with

**Fix:** Can't fix bad commit messages, but can add context in review

---

**Issue 4: Missing Context**

```markdown
## 🎉 New Features
- Add webhook support  ℹ️ Needs context about what it enables
```

**Why:** Automation can't infer business context

**Fix:** Human adds: "Add webhook support (enables real-time integrations)"

## Comparing to Your Manual Process

Pull out your [documented manual process](step-2-document-process.md) from Step 2.

### Side-by-Side Comparison

Create a comparison table:

| Commit | Your Manual Category | AI Category | Match? | Notes |
|--------|---------------------|-------------|--------|-------|
| "Add user auth" | New Feature | New Feature | ✅ | Correct |
| "Improve performance" | Enhancement | New Feature | ❌ | AI needs clarity |
| "Update CI config" | (Excluded) | Enhancement | ❌ | Missing exclusion rule |

### Calculate Accuracy

```
Accuracy = Correct Categorizations / Total Commits × 100%
```

**Example:** 15 correct out of 20 commits = 75% accuracy

**Targets:**

- **First run:** 60-70% is normal
- **After iteration:** Aim for 85-95%
- **Never perfect:** 100% is unrealistic (and unnecessary!)

## Creating Your Improvement List

Based on your review, create a prioritized list:

### High Priority (Breaks Quality)

Things that make the output unusable:

- Missing critical exclusion rules
- Major miscategorizations
- Including internal-only changes

### Medium Priority (Reduces Quality)

Things that require significant manual cleanup:

- Inconsistent categorization of similar commits
- Unclear boundary between features and enhancements
- Some internal changes leaking through

### Low Priority (Nice to Have)

Minor issues that don't significantly impact workflow:

- Formatting preferences
- Wording tweaks
- Edge cases affecting <5% of commits

### Example Improvement List

```markdown
## Improvements Needed

### High Priority
1. Exclude commits containing "internal", "ci:", "test:"
2. Clarify feature vs enhancement distinction
3. Filter out merge commits

### Medium Priority
1. Add examples of each category to prompt
2. Specify that "improve/optimize" = enhancement
3. Better handling of documentation updates

### Low Priority
1. Adjust emoji icons
2. Include commit author names
3. Add links to pull requests (not just commits)
```

## What You've Learned

In this step, you:

- ✅ Generated release notes with sample data
- ✅ Ran automation on a real repository
- ✅ Evaluated output quality systematically
- ✅ Created prioritized improvement list
- ✅ Compared AI output to manual standards

## Next Step

Now you're ready for the most rewarding part: iterating on your prompts to dramatically improve quality.

[Next: Step 5 - Iterate Prompts →](step-5-iterate-prompts.md){ .md-button .md-button--primary }

---

!!! tip "Keep Your Notes"
    Save your:
    - Generated `release_notes.md` files (rename to `release_notes_v1.md`, etc.)
    - Improvement list
    - Accuracy calculations
    
    You'll reference these when refining prompts in Step 5.
