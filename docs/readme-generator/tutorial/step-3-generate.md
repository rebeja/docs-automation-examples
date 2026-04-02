# Step 3: Generate your README

Run the full generator and review what each section produces.

## Generate all sections

=== "Sample project"

    ```bash
    python readme_generator.py --sample --output README_sample.md
    ```

=== "Local directory"

    ```bash
    python readme_generator.py --input /path/to/your/project --output README.md
    ```

=== "GitHub repo"

    ```bash
    python readme_generator.py --input owner/repo --output README.md
    ```

The script generates each section in order, prints progress, and writes the assembled README to the output file.

Expected output:

```
📄 README Generator
==================================================

🔍 Analyzing ./my-project...
✓ Project: my-project
✓ Language: Python
✓ License: MIT
✓ Dependencies: click, requests (+2 more)

✍️  Generating description section...
✓ Description section complete

✍️  Generating installation section...
✓ Installation section complete

✍️  Generating usage section...
✓ Usage section complete

✍️  Generating contributing section...
✓ Contributing section complete

📝 Assembling README...
✓ README written to README.md

✅ Done! Review the output before publishing.
```

## Generate specific sections only

Use `--sections` to regenerate just one or two sections instead of all four:

```bash
# Regenerate only the usage section
python readme_generator.py --input ./my-project --sections usage --output README.md

# Regenerate description and installation
python readme_generator.py --input ./my-project --sections description,installation --output README.md
```

This is useful when you want to keep sections you've already edited and only refresh specific ones.

## Review each section

Open the generated README and evaluate each section critically.

### Description section

AI is generally good at this. Check:

- [ ] Does it accurately describe what the project does?
- [ ] Is the feature list realistic (not invented)?
- [ ] Is the tone appropriate for your audience?

### Installation section

AI infers install commands from dependency files. Verify:

- [ ] Are the prerequisite versions correct?
- [ ] Does `pip install -r requirements.txt` (or equivalent) actually work?
- [ ] Is the quickstart example syntactically correct?

!!! warning "Always test installation steps"
    AI generates plausible-looking commands based on patterns, but it cannot run them. Every installation step must be tested manually before publishing.

### Usage section

AI generates examples based on your entry point files. Verify:

- [ ] Do the example commands actually work?
- [ ] Are function signatures and argument names accurate?
- [ ] Is expected output shown correctly?

### Contributing section

This section is largely boilerplate and is usually safe as-is. Check:

- [ ] Is the license type correct?
- [ ] Are the contribution steps appropriate for your project?

## What to keep, what to rewrite

| AI generates well | Write yourself |
|---|---|
| Project descriptions | Specific version requirements |
| Feature bullet lists | Accurate code output/screenshots |
| Boilerplate contributing text | Security or authentication notes |
| License notices | Roadmap or known limitations |
| General install patterns | Environment-specific instructions |

---

Next step: [Refine and customize →](step-4-refine.md)
