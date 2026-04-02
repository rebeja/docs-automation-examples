# Step 2: Analyze your repo

Before generating any content, understand what context the script extracts — and why it matters.

## What the analyzer does

The script scans your repository and builds a context summary that gets passed to the AI. It collects:

| Field | Source | Used for |
|-------|--------|----------|
| Project name | `package.json`, `pyproject.toml`, `Cargo.toml`, directory name | README title |
| Primary language | File extension counts | Install command format |
| Dependencies | `requirements.txt`, `package.json`, `go.mod`, etc. | Installation section |
| Entry points | `main.py`, `index.js`, `app.go`, etc. | Usage examples |
| License | `LICENSE` file contents | Contributing section |
| Key files | Up to 5 source files, truncated at 200 lines | All sections |

## Run the analysis

=== "Sample project"

    ```bash
    python readme_generator.py --sample --analyze
    ```

=== "Local directory"

    ```bash
    python readme_generator.py --input /path/to/your/project --analyze
    ```

=== "GitHub repo"

    ```bash
    python readme_generator.py --input owner/repo --analyze
    ```

The `--analyze` flag prints the full context summary without calling the AI or generating a README.

## Review the output

Look for:

**Is the project name correct?**
If not, the script couldn't find a config file to read it from. It falls back to the directory name. You can rename the output file later, or add a `name` field to your `package.json` / `pyproject.toml`.

**Is the right language detected?**
Language is detected from the most common file extension. If a repo has more test files than source files in a secondary language, the detection may be off. This is used as a hint to the AI — it will not cause incorrect output, but may affect command formatting.

**Are dependencies listed?**
Missing dependencies usually means the script did not find a recognized dependency file. Check that your `requirements.txt`, `package.json`, or equivalent is in the root directory.

**Are entry points found?**
Entry points with recognized names (`main.py`, `index.js`, etc.) are read and included as code context. If your entry point has a custom name, the AI will still work — it will use other files for context.

## Why context quality matters

The AI generates content based entirely on what you provide. A richer context leads to more accurate output:

| Less context | More context |
|---|---|
| Generic install instructions | Commands specific to your stack |
| Placeholder usage examples | Examples based on your actual functions |
| Boilerplate descriptions | Accurate feature lists |

If the analysis output looks thin, add a brief `README.md` stub with even a few sentences — the script reads existing README content and passes it as additional context.

---

Next step: [Generate your README →](step-3-generate.md)
