# Step 2: Document Your Process

This is the **most important step** in the entire tutorial. Before automating anything, you need to clearly document your manual workflow.

!!! info "Time Estimate"
    30-45 minutes

!!! success "Key Principle"
    **"Before automating, write down your actual manual process—automation replicates your workflow."**
    
    If your manual process is poorly defined, your automation will be poorly defined too.

## Why This Matters

Your documented manual process becomes:

1. **The foundation for your automation prompt** - Each manual step maps to an automated step
2. **Your quality baseline** - How do you know if automation works? Compare to your manual standards
3. **Your training material** - For teaching the AI what good categorization looks like
4. **Your troubleshooting guide** - When automation fails, check which manual step is misaligned

## What You'll Accomplish

By the end of this step:

- ✅ Complete workflow documentation
- ✅ Clear categorization standards
- ✅ Defined exclusion rules
- ✅ Output format specification
- ✅ Ready-to-use automation prompt

## The Workflow Worksheet

Complete this worksheet by answering each question based on YOUR current manual process.

### Part 1: Current Manual Workflow

**What steps do you currently follow to create release notes?**

Write each step in order:

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

**Example:**

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

### Part 2: Categorization Standards

**How do you decide which category each change belongs to?**

!!! tip "Be Specific"
    Instead of "I know a bug fix when I see one," write: "Bug fixes contain words like 'fix', 'bug', 'issue', 'resolve' and describe correcting existing functionality."

Complete this table:

| Category | Definition | Keyword Indicators | Examples |
|----------|-----------|-------------------|----------|
| **New Features** | | | |
| **Enhancements** | | | |
| **Bug Fixes** | | | |
| **Documentation** | | | |
| **Other** | | | |

**Example:**

| Category | Definition | Keyword Indicators | Examples |
|----------|-----------|-------------------|----------|
| **New Features** | Wholly new capabilities that didn't exist before | "add", "new", "create", "introduce" | "Add user authentication", "New dashboard view" |
| **Enhancements** | Improvements to existing features | "improve", "update", "enhance", "optimize", "increase" | "Improve search performance", "Update API response format" |
| **Bug Fixes** | Corrections to existing functionality | "fix", "bug", "resolve", "issue", "correct" | "Fix memory leak", "Resolve login timeout" |
| **Documentation** | Content updates, guides, API docs | "docs", "documentation", "guide", "readme" | "Update API guide", "Fix typo in docs" |

### Part 3: Exclusion Rules

**What types of commits should NOT appear in release notes?**

Check all that apply and add specifics:

- [ ] Merge commits without meaningful changes
- [ ] Work-in-progress commits (WIP, temp, test)
- [ ] Internal tooling changes
- [ ] Code formatting/style changes
- [ ] Test file updates (unless new features)
- [ ] Dependency updates (unless user-facing)
- [ ] Other: _______________

**Write specific exclusion criteria:**

```markdown
## What to Exclude

1. Exclude commits containing: _______________
2. Exclude commits starting with: _______________
3. Exclude commits from these paths: _______________
4. Exclude commits by these authors: _______________
```

**Example:**

```markdown
## What to Exclude

1. Exclude commits containing: "WIP", "temp", "test only", "internal"
2. Exclude commits starting with: "Merge pull request", "chore:"
3. Exclude commits from these paths: /tests/, /internal-tools/
4. Exclude commits by these authors: automation-bot@company.com
```

### Part 4: Output Format

**What does your final release notes format look like?**

Provide a template:

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

**Example:**

```markdown
## My Release Notes Format

### Header Information
- Include: Date, period covered
- Format: "Release Notes - MM/DD/YYYY (covering commits since MM/DD/YYYY)"

### Category Order
1. 🎉 New Features (most exciting first)
2. ✨ Enhancements
3. 🐛 Bug Fixes
4. 📝 Documentation

### Entry Format
- Commit description format: "- Description ([commit-hash](link))"
- Link format: Full GitHub URL to commit
- Additional context: Add parenthetical notes for major changes

### Footer/Notes
- Include: "For questions, contact docs@company.com"
```

### Part 5: Audience Considerations

**Who reads your release notes?**

- [ ] Internal engineering team
- [ ] External customers
- [ ] Product managers
- [ ] Support team
- [ ] Sales/Marketing
- [ ] Other: _______________

**How should language be adjusted for this audience?**

```markdown
## Audience Guidance

Technical level: _______________
Tone: _______________
Avoid: _______________
Emphasize: _______________
```

**Example:**

```markdown
## Audience Guidance

Technical level: Mix of technical and non-technical readers
Tone: Professional but approachable
Avoid: Internal jargon, overly technical implementation details
Emphasize: User impact, benefits, links to documentation
```

## Completed Worksheet Example

See a [complete example worksheet](../../examples/manual-process-example.md) showing real documentation from a docs team.

## Converting to an Automation Prompt

Once you've completed the worksheet, you'll convert it into an automation prompt in [Step 5](step-5-iterate-prompts.md).

**The mapping:**

| Manual Step | Automation Step |
|-------------|----------------|
| Filter by date range | Script queries GitHub API |
| Review each commit | Script fetches commit data |
| Decide if user-facing | Exclusion rules in prompt |
| Categorize commits | AI analyzes with your standards |
| Format consistently | Template in prompt |
| Add context | Human review (stays manual) |

## What You've Learned

In this step, you:

- ✅ Documented your complete manual workflow
- ✅ Defined clear categorization standards
- ✅ Specified exclusion rules
- ✅ Created output format template
- ✅ Considered audience needs

## Next Step

With your process documented, you're ready to set up API access.

[Next: Step 3 - Configure APIs →](step-3-configure.md){ .md-button .md-button--primary }

---

!!! tip "Save Your Worksheet"
    Keep this documentation! You'll reference it when:
    
    - Writing your first prompt (Step 5)
    - Troubleshooting categorization errors
    - Training new team members
    - Building other automation projects
