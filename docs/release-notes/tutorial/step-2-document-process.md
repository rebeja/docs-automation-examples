# Step 2: Document your process

This is the most important step in the tutorial. Document your manual workflow before automating anything.

**Time estimate:** 30-45 minutes

**Key principle:** Automation replicates your workflow. Poorly defined manual processes create poorly defined automation.

## Why documentation matters

Your documented manual process becomes:

1. **Foundation for automation prompt** - Each manual step maps to an automated step
2. **Quality baseline** - Compare automation output to your manual standards
3. **Training material** - Teach the AI what good categorization looks like
4. **Troubleshooting guide** - Check which manual step is misaligned when automation fails

## Complete these tasks

- Document complete workflow
- Define clear categorization standards
- Specify exclusion rules
- Create output format specification
- Prepare automation prompt

## Workflow worksheet

Answer each question based on your current manual process.

### Part 1: Current manual workflow

List each step you follow to create release notes:

```markdown
## My Manual Release Notes Process

1. Step: _______________________________________________
   Time: _____ minutes
   Tools used: _______________

2. Step: _______________________________________________
   Time: _____ minutes
   Tools used: _______________

3. Step: _______________________________________________
   Time: _____ minutes
   Tools used: _______________

(Continue for all steps...)

**Total time per release:** _____ hours/minutes
```

Example:

```markdown
## My Manual Release Notes Process

1. Step: Open GitHub and navigate to repository
   Time: 2 minutes
   Tools used: GitHub web interface

2. Step: Navigate to "Commits" and filter by date range
   Time: 5 minutes
   Tools used: GitHub filters

3. Step: Review each commit message
   Time: 30-45 minutes (for 50+ commits)
   Tools used: Read commit messages, click through to see changes

4. Step: Copy relevant commits to a draft document
   Time: 15 minutes
   Tools used: Google Doc or Markdown file

5. Step: Categorize each commit as Feature/Enhancement/Bug Fix/Docs
   Time: 20 minutes
   Tools used: Manual judgment

6. Step: Format consistently with headings and links
   Time: 10 minutes
   Tools used: Markdown formatting

7. Step: Add context and clean up language
   Time: 15 minutes
   Tools used: Editing skills

**Total time per release:** 1.5-2 hours
```

### Part 2: Categorization standards

Define how you decide which category each change belongs to. Be specific with keywords and indicators, not vague descriptions like "I know a bug fix when I see one."

Complete this table:

| Category | Definition | Keyword Indicators | Examples |
|----------|-----------|-------------------|----------|
| **New Features** | | | |
| **Enhancements** | | | |
| **Bug Fixes** | | | |
| **Documentation** | | | |
| **Other** | | | |

Example:

| Category | Definition | Keyword Indicators | Examples |
|----------|-----------|-------------------|----------|
| **New Features** | Capabilities that didn't exist before | "add", "new", "create", "introduce" | "Add user authentication", "New dashboard view" |
| **Enhancements** | Improvements to existing features | "improve", "update", "enhance", "optimize", "increase" | "Improve search performance", "Update API response format" |
| **Bug Fixes** | Corrections to existing functionality | "fix", "bug", "resolve", "issue", "correct" | "Fix memory leak", "Resolve login timeout" |
| **Documentation** | Content updates, guides, API docs | "docs", "documentation", "guide", "readme" | "Update API guide", "Fix typo in docs" |

### Part 3: Exclusion rules

Define which commits should not appear in release notes:

- Merge commits without meaningful changes
- Work-in-progress commits (WIP, temp, test)
- Internal tooling changes
- Code formatting or style changes
- Test file updates (unless new features)
- Dependency updates (unless user-facing)
- Other: _______________

Write specific exclusion criteria:

```markdown
## What to Exclude

1. Exclude commits containing: _______________
2. Exclude commits starting with: _______________
3. Exclude commits from these paths: _______________
4. Exclude commits by these authors: _______________
```

Example:

```markdown
## What to Exclude

1. Exclude commits containing: "WIP", "temp", "test only", "internal"
2. Exclude commits starting with: "Merge pull request", "chore:"
3. Exclude commits from these paths: /tests/, /internal-tools/
4. Exclude commits by these authors: automation-bot@company.com
```

### Part 4: Output format

Define your final release notes format:

```markdown
## My Release Notes Format

### Header Information
- Include: _______________
- Format: _______________

### Category Order
1. _______________
2. _______________
3. _______________
4. _______________

### Entry Format
- Commit description format: _______________
- Link format: _______________
- Additional context: _______________

### Footer/Notes
- Include: _______________
```

Example:

```markdown
## My Release Notes Format

### Header Information
- Include: Date, period covered
- Format: "Release Notes - MM/DD/YYYY (covering commits since MM/DD/YYYY)"

### Category Order
1. New Features (most exciting first)
2. Enhancements
3. Bug Fixes
4. Documentation

### Entry Format
- Commit description format: "- Description ([commit-hash](link))"
- Link format: Full GitHub URL to commit
- Additional context: Add parenthetical notes for major changes

### Footer/Notes
- Include: "For questions, contact docs@company.com"
```

### Part 5: Audience considerations

Identify who reads your release notes:

- Internal engineering team
- External customers
- Product managers
- Support team
- Sales or Marketing
- Other: _______________

Define language adjustments for this audience:

```markdown
## Audience Guidance

Technical level: _______________
Tone: _______________
Avoid: _______________
Emphasize: _______________
```

Example:

```markdown
## Audience Guidance

Technical level: Mix of technical and non-technical readers
Tone: Professional but approachable
Avoid: Internal jargon, overly technical implementation details
Emphasize: User impact, benefits, links to documentation
```

## Completed worksheet example

Review a [complete example worksheet](../../examples/manual-process-example.md) showing real documentation from a docs team.

## Convert to automation prompt

After completing the worksheet, convert it into an automation prompt in [Step 5](step-5-iterate-prompts.md).

Manual steps map to automation steps:

| Manual Step | Automation Step |
|-------------|----------------|
| Filter by date range | Script queries GitHub API |
| Review each commit | Script fetches commit data |
| Decide if user-facing | Exclusion rules in prompt |
| Categorize commits | AI analyzes with your standards |
| Format consistently | Template in prompt |
| Add context | Human review (stays manual) |

## Summary

You documented your complete manual workflow, defined clear categorization standards, specified exclusion rules, created output format template, and considered audience needs.

## Next step

Set up API access with your process documented.

[Next: Step 3 - Configure APIs](step-3-configure.md)

---

Keep this documentation. Reference it when writing your first prompt (Step 5), troubleshooting categorization errors, training new team members, and building other automation projects.
