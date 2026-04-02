# Step 1: Setup environment

Install dependencies and choose your starting point.

## Prerequisites check

```bash
python3 --version  # Should be 3.8 or higher
git --version      # Any recent version
```

## Choose your path

**Path A: Use the sample project** (Recommended for first-time users)

- No GitHub token or local repo required for steps 1–2
- Uses a built-in Python CLI project called TaskFlow
- Run with `--sample` flag

**Path B: Use your own repository**

- Works with any local directory or GitHub repo
- Requires an AI provider API key
- Results are immediately useful

## Install dependencies

From the `03-readme-generator/` directory:

```bash
pip install --upgrade pip
pip install anthropic pyyaml jinja2
# or for OpenAI:
pip install openai pyyaml jinja2
# for GitHub repos, also add:
pip install PyGithub
```

## Configure AI access

The script reads from the shared `config.yaml` at the root of the repository. If you completed either of the other projects, your config is already set up.

If not, copy the example:

```bash
# From the repo root
cp config.example.yaml config.yaml
```

Open `config.yaml` and set:

```yaml
ai_provider: "anthropic"      # or "openai"
ai_api_key: "sk-ant-..."      # your API key
model: "claude-sonnet-4-6"    # or your preferred model
```

!!! note "Path A users"
    Skip AI configuration for now — `--sample` mode runs without API calls.
    You will need it for Step 3 when you generate actual content.

## Verify your setup

```bash
cd 03-readme-generator
python readme_generator.py --sample --analyze
```

Expected output:

```
📄 README Generator
==================================================

🔍 Analyzing sample project...
✓ Project: taskflow
✓ Language: Python
✓ License: MIT
✓ Dependencies: click, pyyaml, rich
✓ Entry points: main.py

📋 Full repo context:
...
```

If you see this output, you are ready to continue.

---

Next step: [Analyze your repo →](step-2-analyze-repo.md)
