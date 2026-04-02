# Prompt engineering reference

The README generator uses four prompt files to control what each section contains. Understanding the prompt structure lets you tailor output for your project's audience and style.

## Prompt file structure

Each prompt file follows the same pattern:

```
[Role statement]
[Task description]

Include:
- [List of what to generate]

Do NOT include:
- [List of exclusions]

[Formatting instructions]

Repository context:
{REPO_CONTEXT}
```

The `{REPO_CONTEXT}` placeholder is replaced at runtime with the analyzed repository summary. Everything else is your instruction to the AI.

## Default prompts

### `description_prompt.txt`

Generates the opening section: project name as H1, a 2-3 sentence description, and a 3-5 bullet feature list.

**Key instructions in the default prompt:**
- Professional, developer-friendly tone
- No badges, no installation steps
- Starts with `# {project name}`

**When to edit:** If the default output is too generic, add audience or tone instructions. For example:

```
Target audience: data engineers integrating this into Apache Airflow pipelines.
Tone: technical and precise. Assume familiarity with Python and SQL.
```

### `installation_prompt.txt`

Generates the `## Installation` section: prerequisites, install steps, and a quickstart command.

**Key instructions in the default prompt:**
- Uses detected dependency file to infer install commands
- Flags uncertainty rather than guessing silently
- Excludes full usage docs

**When to edit:** If your project has non-standard install steps, add them explicitly:

```
After cloning, users must also run: make init
The project requires PostgreSQL 14 or later. Include this as a prerequisite.
```

### `usage_prompt.txt`

Generates the `## Usage` section: 2-4 usage scenarios with code examples and expected output.

**Key instructions in the default prompt:**
- Bases examples on entry point files in context
- Handles CLIs, libraries, and web apps differently
- Adds verification comments when uncertain

**When to edit:** If you want specific examples or need to exclude certain features:

```
Focus on the --export and --filter flags. Skip the --debug flag (internal use only).
Show expected output for each command as a plain code block labeled "Output:".
```

### `contributing_prompt.txt`

Generates `## Contributing` and `## License` sections: contribution steps and license notice.

**Key instructions in the default prompt:**
- Uses detected LICENSE file for the license type
- Standard fork/PR contribution workflow
- Generic code of conduct reference

**When to edit:** If your project has specific contribution requirements:

```
Contributors must sign a CLA before their PR is accepted. Mention this prominently.
Do NOT include a code of conduct section — link to CONTRIBUTING.md instead.
```

## Common customization patterns

### Specify audience

Add to any prompt:

```
Target audience: [who they are, what they already know]
```

Examples:

```
Target audience: Hobbyist Python developers, not necessarily familiar with virtual environments.

Target audience: Senior DevOps engineers. Assume familiarity with Docker and Kubernetes.
```

### Adjust tone

```
Tone: casual and friendly. This is an open source weekend project.
Tone: formal and precise. Enterprise software for regulated industries.
Tone: concise. Minimize prose. Prefer bullet points and code over paragraphs.
```

### Control formatting

```
Format all shell commands with a leading $ prompt character.
Show expected output after each command, labeled "Output:", in a plain code block.
Use numbered lists for sequential steps, bullet lists for non-sequential items.
```

### Exclude content you'll write manually

```
Do NOT include environment variable documentation — I will add this manually.
Do NOT generate a roadmap or future features section.
Do NOT include Docker instructions — the project does not support Docker.
```

### Add missing context

If the script can't find certain details automatically, add them directly:

```
The project name is "flux-sync". The directory name will be different — ignore it.
This project requires Node.js 18 or later. Include this as a prerequisite.
The primary entry point is src/cli.ts, compiled to dist/cli.js. Show usage with node dist/cli.js.
```

## Iterating on prompts

The fastest iteration cycle:

1. Edit a prompt file
2. Regenerate only that section: `python readme_generator.py --input ./my-project --sections <name>`
3. Review the output
4. Repeat

Regenerating a single section takes seconds and uses minimal API tokens. Avoid regenerating all four sections during prompt iteration.

## What prompts cannot fix

Some output quality problems come from the repository context, not the prompt:

| Problem | Root cause | Fix |
|---|---|---|
| Generic descriptions | No docstrings, no stub README | Add a module-level docstring or stub README |
| Wrong install commands | No recognized dependency file | Add `requirements.txt` / `package.json` to repo root |
| Missing entry point examples | No standard entry point filename | Add a module-level docstring to your main file |
| Hallucinated function names | Entry point file too large, key code truncated | Move key functions to the top of the file |

If improving prompts doesn't help, run `--analyze` and check whether the context summary actually contains the information you want the AI to use.
