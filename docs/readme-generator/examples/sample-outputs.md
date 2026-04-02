# Sample outputs

These examples show what the README generator produces from the built-in sample project (`--sample`), followed by an edited version that a technical writer would publish.

The sample project is a Python CLI task manager called **TaskFlow** (`examples/sample_project/`).

---

## Generated output (unedited)

This is the raw output from:

```bash
python readme_generator.py --sample --output README_sample.md
```

---

```markdown
# TaskFlow

A command-line task management tool for developers who prefer to stay in the terminal.
TaskFlow helps you create, prioritize, and track tasks without leaving your workflow.

Key features:
- Add and list tasks from the command line
- Set priority levels (low, medium, high)
- Mark tasks as complete
- Persistent JSON storage — tasks survive between sessions

## Installation

**Prerequisites:** Python 3.8 or later

Clone the repository and install dependencies:

\```bash
git clone https://github.com/example/taskflow.git
cd taskflow
pip install -r requirements.txt
\```

**Quickstart:**

\```bash
python main.py add "Write project documentation" --priority high
python main.py list
\```

## Usage

### Add a task

\```bash
python main.py add "Task description" --priority medium
\```

Options for `--priority`: `low`, `medium`, `high` (default: `medium`)

### List tasks

\```bash
python main.py list
\```

Output:

\```
ID  Priority  Status    Task
1   high      pending   Write project documentation
2   medium    pending   Review pull requests
\```

### Complete a task

\```bash
python main.py complete 1
\```

### Remove a task

\```bash
python main.py remove 2
\```

## Contributing

Contributions are welcome. To contribute:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-change`
3. Make your changes and add tests
4. Submit a pull request

Please follow the existing code style and include tests for new features.

## License

MIT License. See [LICENSE](LICENSE) for details.
```

---

## Edited version (ready to publish)

A technical writer reviewed the generated output, tested the commands, and made the following changes:

- Corrected the install command (the sample project has no `git clone` source — updated to reflect a local workflow)
- Verified all `main.py` commands work as documented
- Added a note about where tasks are stored
- Removed the generic contributing text (not needed for a sample project)

```markdown
# TaskFlow

A command-line task management tool for developers who prefer to stay in the terminal.
TaskFlow helps you create, prioritize, and track tasks without leaving your workflow.

Key features:
- Add and list tasks from the command line
- Set priority levels (low, medium, high)
- Mark tasks as complete
- Persistent JSON storage — tasks survive between sessions

## Installation

**Prerequisites:** Python 3.8 or later

Install dependencies:

\```bash
pip install -r requirements.txt
\```

**Quickstart:**

\```bash
python main.py add "Write project documentation" --priority high
python main.py list
\```

## Usage

### Add a task

\```bash
python main.py add "Task description" --priority medium
\```

`--priority` accepts `low`, `medium`, or `high`. Default: `medium`.

### List tasks

\```bash
python main.py list
\```

Output:

\```
ID  Priority  Status    Task
1   high      pending   Write project documentation
2   medium    pending   Review pull requests
\```

### Complete a task

\```bash
python main.py complete 1
\```

Marks task 1 as done. Completed tasks remain in the list until removed.

### Remove a task

\```bash
python main.py remove 2
\```

Tasks are stored in `tasks.json` in the project root directory.

## License

MIT License. See [LICENSE](LICENSE) for details.
```

---

## What changed and why

| Change | Reason |
|---|---|
| Removed `git clone` from install | Sample project has no remote URL — tested the actual steps instead |
| Added `tasks.json` storage note | AI had no way to know this detail; found it by reading `main.py` |
| Removed generic contributing section | Not relevant for a sample/demo project |
| Added "completed tasks remain in list" note | Discovered while testing — useful behavior, not obvious from output |

The generated draft was a good starting point. The edits took about five minutes and required running the commands once to verify them.

---

## Generating this output yourself

```bash
# Generate the sample README
python readme_generator.py --sample --output README_sample.md

# View the output
cat README_sample.md
```

The sample project files are in `examples/sample_project/`. You can edit them to experiment with how different code structures affect the generated output.
