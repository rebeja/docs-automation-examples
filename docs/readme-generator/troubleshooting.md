# Troubleshooting

## Setup issues

### `ModuleNotFoundError: No module named 'anthropic'`

The required AI provider package is not installed.

```bash
pip install anthropic         # for Anthropic
pip install openai            # for OpenAI or Azure OpenAI
```

### `ModuleNotFoundError: No module named 'PyGithub'`

PyGithub is only needed for GitHub repo input. Install it if you're pointing `--input` at a GitHub repository:

```bash
pip install PyGithub
```

### `ModuleNotFoundError: No module named 'jinja2'`

```bash
pip install jinja2
```

---

## Configuration issues

### `Error: config.yaml not found`

The script looks for `config.yaml` at `../config.yaml` relative to the script location by default. Run from the `03-readme-generator/` directory, or pass the config path explicitly:

```bash
python readme_generator.py --input ./my-project --config /path/to/config.yaml
```

### `Error: 'ai_provider' not found in config`

Your `config.yaml` is missing required fields. At minimum, the file needs:

```yaml
ai_provider: anthropic
ai_api_key: your-key-here
model: claude-sonnet-4-6
```

Copy `config.example.yaml` from the project root and fill in your values.

### `AuthenticationError` or `401 Unauthorized`

Your API key is invalid or not set. Check:

1. `ai_api_key` in `config.yaml` matches the key from your provider's dashboard
2. No extra spaces or quotes around the key value
3. The key has not expired or been revoked

---

## GitHub input issues

### `GithubException: 401 Unauthorized` (GitHub)

Your GitHub token is missing or invalid. Add it to `config.yaml`:

```yaml
github_token: ghp_yourtoken
```

Tokens need `repo` scope to access private repositories. Public repos do not require a token.

### `GithubException: 404 Not Found` (GitHub)

The repository slug is incorrect, the repo is private and your token lacks access, or the repo does not exist.

Verify the slug format: `owner/repo` (no `https://`, no `.git`).

### Rate limit errors from GitHub

GitHub's unauthenticated API rate limit is 60 requests/hour. Add a GitHub token to increase this to 5,000 requests/hour:

```yaml
github_token: ghp_yourtoken
```

---

## Generation issues

### Output is generic or inaccurate

The AI generates content from the context it receives. If output is generic:

1. Run `--analyze` to see what context was extracted
2. Check whether your project name, language, and dependencies were detected correctly
3. Add a stub `README.md` to your project with a one-paragraph description
4. Add docstrings to entry point files

See [Step 2: Analyze your repo](tutorial/step-2-analyze-repo.md) for details.

### Generated install commands don't work

AI infers install commands from dependency files. Common problems:

- No recognized dependency file in the root directory (`requirements.txt`, `package.json`, `go.mod`, etc.)
- Dependency file is in a subdirectory (the script only looks one level deep for dependency files)
- Project requires a build step not reflected in the dependency file

Fix: Add the correct commands explicitly in `installation_prompt.txt`:

```
The correct install command is: make install
Prerequisites: Go 1.21 or later
```

### `KeyError: 'description_section'` during assembly

A section failed to generate but the template still expected it. This usually means the AI call for that section returned an error or empty response.

Check the terminal output for error messages during section generation, and verify your API key has sufficient quota.

### Output file is empty or truncated

Disk write error, or the script was interrupted. Run again — generation will start from scratch.

---

## Token and cost issues

### API quota exceeded

If you hit your API quota mid-generation, the script will error on the failing section. Generated sections before the error are not written to the output file.

Wait for your quota to reset, or use `--sections` to regenerate only the section that failed:

```bash
python readme_generator.py --input ./my-project --sections usage --output README.md
```

### Generation is slow

Each section is a separate API call. Four sections means four round trips. If latency is the issue:

- Use `--sections` to generate only the sections you need
- Run `--analyze` first to verify context quality before spending tokens on generation

---

## Template issues

### `TemplateNotFound` or `UndefinedError` in template

Your custom template references a variable that doesn't exist. Available variables are listed in the [configuration reference](reference/configuration.md#sections).

Check for typos in variable names: `{{ description_section }}` not `{{ description }}`.

### Template renders with empty sections

The section variable is empty, which means that section was not generated. Either:
- The section name was not in `--sections` (omitting `--sections` generates all four)
- The section generation failed silently

Run without `--sections` to generate all sections, or check terminal output for errors.
