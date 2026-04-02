# Step 4: Refine and customize

Improve output quality by editing prompts, adjusting context, and using custom templates.

## Edit the prompts

Each section has its own prompt file in `prompts/`. These are plain text files you can edit directly.

```
prompts/
├── description_prompt.txt
├── installation_prompt.txt
├── usage_prompt.txt
└── contributing_prompt.txt
```

Open any prompt to see its structure — each has a `{REPO_CONTEXT}` placeholder where the script injects repository information, plus instructions that shape the AI's output.

### Prompt editing techniques

**Specify your audience:**

```
# Add to description_prompt.txt
Target audience: Backend developers integrating this library into existing Python applications.
```

**Add formatting requirements:**

```
# Add to usage_prompt.txt
Format all commands as: $ command (with dollar sign prompt)
Show expected output after each command as a plain code block (no language hint).
```

**Exclude content you'll write manually:**

```
# Add to contributing_prompt.txt
Do NOT include a code of conduct section — I will write this separately.
Do NOT include issue templates — link to CONTRIBUTING.md instead.
```

**Tune the tone:**

```
# Add to description_prompt.txt
Tone: casual and friendly. This is an open source side project, not enterprise software.
```

After editing a prompt, regenerate only that section:

```bash
python readme_generator.py --input ./my-project --sections description --output README.md
```

## Improve context quality

The AI output is only as good as the context it receives. Two ways to improve it:

**Add a stub README**: Create a brief `README.md` in your project with a one-paragraph description. The script reads it and passes it as additional context.

```markdown
# my-project

A CLI tool for converting Markdown files to PDF with custom styling.
Built for technical writers who work in docs-as-code workflows.
```

**Add docstrings to entry points**: If your main entry file has no comments or docstrings, add a module-level docstring before running the generator.

```python
"""
my-project: Convert Markdown files to styled PDF.
Supports custom CSS, MkDocs theme compatibility, and batch processing.
"""
```

## Use a custom template

The default template assembles sections in a fixed order. For a different layout, copy and modify the default template:

```bash
cp templates/readme_template.md.j2 templates/my-template.md.j2
```

Edit `templates/my-template.md.j2`. Available variables:

| Variable | Content |
|---|---|
| `{{ description_section }}` | Full description section markdown |
| `{{ installation_section }}` | Full installation section markdown |
| `{{ usage_section }}` | Full usage section markdown |
| `{{ contributing_section }}` | Full contributing section markdown |
| `{{ project_name }}` | Project name string |
| `{{ language }}` | Primary language string |
| `{{ license }}` | License type string |
| `{{ date }}` | Generation date (YYYY-MM-DD) |

Example custom template adding a badges line:

```jinja2
{{ description_section }}

![License](https://img.shields.io/badge/license-{{ license }}-blue)
![Language](https://img.shields.io/badge/language-{{ language }}-green)

{{ installation_section }}

{{ usage_section }}

{{ contributing_section }}
```

Run with your template:

```bash
python readme_generator.py --input ./my-project --template templates/my-template.md.j2
```

## Iteration workflow

A productive iteration cycle:

1. Edit one prompt file
2. Regenerate that section: `--sections <name>`
3. Review the output
4. Repeat until satisfied
5. Move to the next section

Avoid regenerating all sections at once during iteration — it's slower and costs more API tokens.

---

Next step: [Best practices →](step-5-best-practices.md)
