# Configuration reference

## CLI arguments

| Argument | Default | Description |
|---|---|---|
| `--input` | — | Local directory path or `owner/repo` GitHub slug |
| `--output` | `README.md` | Output file path |
| `--config` | `../config.yaml` | Path to config YAML file |
| `--prompts` | `prompts` | Directory containing prompt template files |
| `--template` | Built-in default | Custom Jinja2 template file (`.j2`) |
| `--sections` | All sections | Comma-separated list of sections to generate |
| `--analyze` | `false` | Print repo context only, skip generation |
| `--sample` | `false` | Use built-in sample project, no API calls |

## config.yaml fields

The script reads the shared `config.yaml` at the project root. Fields used by the README generator:

| Field | Required | Description |
|---|---|---|
| `ai_provider` | Yes | `anthropic`, `openai`, or `azure_openai` |
| `ai_api_key` | Yes | API key for the chosen provider |
| `model` | Yes | Model name or deployment name |
| `github_token` | GitHub repos only | Personal access token with `repo` scope |
| `azure_endpoint` | Azure only | Azure OpenAI resource endpoint |
| `azure_api_version` | Azure only | API version string (default: `2024-02-01`) |
| `readme_max_file_lines` | No | Max lines read per file (default: `200`) |

## Environment variable overrides

| Variable | Config field |
|---|---|
| `AI_PROVIDER` | `ai_provider` |
| `AI_API_KEY` | `ai_api_key` |
| `AI_MODEL` | `model` |
| `GITHUB_TOKEN` | `github_token` |

## Sections

Available section names for `--sections`:

| Name | Heading generated | Prompt file |
|---|---|---|
| `description` | `# {project name}` | `prompts/description_prompt.txt` |
| `installation` | `## Installation` | `prompts/installation_prompt.txt` |
| `usage` | `## Usage` | `prompts/usage_prompt.txt` |
| `contributing` | `## Contributing` and `## License` | `prompts/contributing_prompt.txt` |
