# Step 4: First run

Generate your first automated release notes with sample data, then with a real repository.

**Time estimate:** 20-30 minutes

## Complete these tasks

- Complete first successful run with sample data
- Generate release notes from real repository
- Review output quality
- Create list of improvements needed
- Build confidence to iterate

## Run with sample data

Start with built-in sample data to verify everything works without using API credits.

### 1. Navigate to project directory

```bash
cd 01-release-notes-automation
```

### 2. Run with sample flag

```bash
python generate_release_notes.py \
  --repo sample/repo \
  --since 2024-01-01 \
  --sample
```

The `--sample` flag uses built-in test commits instead of calling GitHub API.

### 3. Review output

The output shows:

```
Fetching commits from sample/repo since 2024-01-01...
Found 8 sample commits
Categorizing commits using AI...
Generating release notes...
Release notes written to release_notes.md
```

### 4. Open the generated file

```bash
cat release_notes.md
```

Example output:

```markdown
# Release Notes

**Date:** 2024-01-28
**Period:** Since 2024-01-01

## New Features

- Add user authentication feature ([abc123](https://github.com/sample/repo/commit/abc123))
- Create dashboard view for analytics ([xyz789](https://github.com/sample/repo/commit/xyz789))

## Enhancements

- Improve search performance by 50% ([def456](https://github.com/sample/repo/commit/def456))
- Update API response format ([mno345](https://github.com/sample/repo/commit/mno345))

## Bug Fixes

- Fix memory leak in parser ([ghi789](https://github.com/sample/repo/commit/ghi789))
- Resolve login timeout issue ([pqr678](https://github.com/sample/repo/commit/pqr678))

## Documentation

- Update API documentation with new endpoints ([jkl012](https://github.com/sample/repo/commit/jkl012))
```

If you see categorized release notes, the automation is working.

## Run with real repository

Try with an actual GitHub repository.

### 1. Choose a repository

Choose one option:

Use your own repository:
```bash
--repo your-username/your-repo
```

Use a public test repository:
```bash
--repo octocat/Hello-World
```

Use an Indeed public repository (if from Indeed):
```bash
--repo indeedeng/proctor
```

### 2. Determine date range

Choose a date range with meaningful commits:

```bash
# Last 30 days
--since $(date -d '30 days ago' +%Y-%m-%d)  # Linux/Mac

# Specific date
--since 2024-01-01

# With end date
--since 2024-01-01 --until 2024-01-31
```

### 3. Run the script

```bash
python generate_release_notes.py \
  --repo octocat/Hello-World \
  --since 2024-01-01
```

### 4. Monitor progress

The output shows:

```
Fetching commits from octocat/Hello-World since 2024-01-01...
Found 23 commits
Categorizing commits using AI...
Generating release notes...
Release notes written to release_notes.md
```

Typical timing: 10-30 seconds depending on commit count and AI provider.

### 5. Review the output

```bash
cat release_notes.md
```

Or open in your text editor:

```bash
code release_notes.md    # VS Code
cursor release_notes.md  # Cursor
```

## Evaluate quality

Review the output for quality and identify improvements.

### Check these items

#### Categorization accuracy

- Are features actually new features (not enhancements)?
- Are bug fixes correctly identified?
- Are enhancements truly improvements (not new features)?
- Is documentation correctly separated?

#### Exclusions

- Internal-only changes excluded
- WIP or temp commits filtered out
- Merge commits without substance removed
- Test-only changes excluded

#### Formatting

- Commit links working
- Format consistent
- Emoji icons displaying correctly
- Date or period information accurate

#### Completeness

- All user-facing changes included
- Major changes properly represented
- No important information missing

### Common issues

Issue 1: Enhancements categorized as features

```markdown
## New Features
- Improve search performance by 50%  [This is an enhancement]
```

Prompt needs clearer distinction between "new" and "improved".

Fix: Refine categorization standards (Step 5)

---

Issue 2: Internal changes included

```markdown
## Enhancements
- Update CI/CD pipeline configuration  [Internal only]
```

Exclusion rules not specific enough.

Fix: Add explicit exclusion patterns (Step 5)

---

Issue 3: Vague descriptions

```markdown
## Bug Fixes
- Fix bug  [Too vague]
```

Commit message was vague, AI has nothing to work with.

Fix: Cannot fix bad commit messages, but can add context in review

---

Issue 4: Missing context

```markdown
## New Features
- Add webhook support  [Needs context about what it enables]
```

Automation cannot infer business context.

Fix: Human adds "Add webhook support (enables real-time integrations)"

## Compare to your manual process

Reference your [documented manual process](step-2-document-process.md) from Step 2.

### Create a side-by-side comparison

Create a comparison table:

| Commit | Your Manual Category | AI Category | Match? | Notes |
|--------|---------------------|-------------|--------|-------|
| "Add user auth" | New Feature | New Feature | Yes | Correct |
| "Improve performance" | Enhancement | New Feature | No | AI needs clarity |
| "Update CI config" | (Excluded) | Enhancement | No | Missing exclusion rule |

### Calculate accuracy

```
Accuracy = Correct Categorizations / Total Commits × 100%
```

Example: 15 correct out of 20 commits = 75% accuracy

Targets:

- First run: 60-70% is normal
- After iteration: Aim for 85-95%
- Never perfect: 100% is unrealistic and unnecessary

## Create your improvement list

Create a prioritized list based on your review:

### High priority (breaks quality)

Issues that make the output unusable:

- Missing critical exclusion rules
- Major miscategorizations
- Including internal-only changes

### Medium priority (reduces quality)

Issues that require significant manual cleanup:

- Inconsistent categorization of similar commits
- Unclear boundary between features and enhancements
- Some internal changes leaking through

### Low priority (nice to have)

Minor issues that do not significantly impact workflow:

- Formatting preferences
- Wording tweaks
- Edge cases affecting less than 5% of commits

### Example improvement list

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

## Summary

You generated release notes with sample data, ran automation on a real repository, evaluated output quality systematically, created a prioritized improvement list, and compared AI output to manual standards.

## Next step

Iterate on your prompts to improve quality.

[Next: Step 5 - Iterate prompts](step-5-iterate-prompts.md)

---

Save your generated `release_notes.md` files (rename to `release_notes_v1.md`, etc.), improvement list, and accuracy calculations. You will reference these when refining prompts in Step 5.
