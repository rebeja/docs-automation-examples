# FAQ

## General

### What AI providers does the README generator support?

Anthropic (Claude), OpenAI (GPT-4 and later), and Azure OpenAI. Configure your provider in `config.yaml` — see the [configuration reference](reference/configuration.md).

### Does it work without a GitHub token?

Yes, for local directories. Point `--input` at a local path and no GitHub token is needed.

For GitHub repository input, public repos work without a token but are subject to rate limits (60 requests/hour). Private repos require a token with `repo` scope.

### Can I use it with GitLab or Bitbucket repos?

Not directly. The script supports local directories and GitHub repos. For GitLab or Bitbucket, clone the repository locally first:

```bash
git clone https://gitlab.com/your/repo.git
python readme_generator.py --input ./repo --output README.md
```

### How much does each generation cost?

Cost depends on your AI provider, model, and the size of the repository context. For a typical small-to-medium project using Claude Sonnet:

- Each section is one API call
- Total context per call is roughly 2,000–4,000 tokens of repo content plus the prompt
- Four sections total

Run `--analyze` first to see how much context is extracted — this call has no AI cost.

### Can I run it on multiple repos at once?

No. The script processes one repository per run. For multiple repos, run it in a shell loop:

```bash
for dir in ./project-a ./project-b ./project-c; do
  python readme_generator.py --input "$dir" --output "$dir/README.md"
done
```

---

## Output quality

### The generated README looks generic. How do I improve it?

The most common cause is thin repository context. Steps to improve it:

1. Run `--analyze` and review the context summary
2. Add a stub `README.md` to the project root with a short description
3. Add module-level docstrings to entry point files
4. Edit the prompt files to add audience, tone, or content requirements

See [Step 4: Refine and customize](tutorial/step-4-refine.md) for techniques.

### The AI invented features or commands that don't exist. What happened?

This is hallucination — the AI generated plausible-sounding content not supported by the actual code. It happens most often in the usage section when entry point files are large, deeply nested, or use unconventional names.

Mitigations:
- Move key functions and their docstrings to the top of entry point files
- Add explicit examples in `usage_prompt.txt`: "Show only the `--export` and `--filter` flags"
- Always test generated examples before publishing

### Can the generator update an existing README instead of writing a new one?

The generator writes complete sections from scratch. It does read your existing README as additional context if one is present — but it does not perform a diff or merge.

For updating an existing README, use `--sections` to regenerate only specific sections:

```bash
python readme_generator.py --input ./my-project --sections installation --output README.md
```

Then manually integrate the new section into your existing file.

### The description section is accurate but the installation section is wrong. Can I keep one and regenerate the other?

Yes. Use `--sections` to regenerate individual sections without overwriting others. Note that the output file is fully rewritten each run, so the simplest approach is:

1. Manually copy the good sections to a draft file
2. Regenerate the problem section to a separate output file: `--output tmp.md`
3. Replace the bad section in your draft with the new output

---

## Configuration

### Can I change the output language?

The prompts control output language. Add a language instruction to any prompt file:

```
Write all output in French.
```

For a non-English README, add this instruction to all four prompts.

### Can I add more sections beyond the default four?

Not through the existing `--sections` flag, which only accepts `description`, `installation`, `usage`, and `contributing`. To add a custom section:

1. Create a new prompt file (e.g., `prompts/api_reference_prompt.txt`)
2. Add the `{REPO_CONTEXT}` placeholder
3. Call `generate_section()` manually in a script that wraps `readme_generator.py`, or add it to `readme_generator.py` directly

### Where is the output template?

At `templates/readme_template.md.j2`. Copy it and pass your copy via `--template` to customize the section order or add static content like a badges line. See [Step 4: Refine and customize](tutorial/step-4-refine.md#use-a-custom-template).

---

## Using with CI

### Can I run this in a GitHub Action?

Yes. The script reads API keys from environment variables:

```yaml
- name: Generate README
  env:
    AI_PROVIDER: anthropic
    AI_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
    AI_MODEL: claude-sonnet-4-6
  run: python 03-readme-generator/readme_generator.py --input . --output README.md
```

The generated README can then be committed back to the repository with a subsequent step.

### Should I auto-commit generated READMEs?

Only if you have a review step. Automatically committing unreviewed AI output risks publishing hallucinated content. A safer pattern: open a pull request with the generated output so a human reviews before merge.
