# Changelog

All notable changes to the Documentation Automation Examples project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Changelog page added to the doc site (`docs/changelog.md`); uses the snippets extension to render `CHANGELOG.md` directly so content stays in one place
- **Project 03: README Generator** (`03-readme-generator/`) — new automation project that analyzes a local directory or GitHub repository and generates a complete README section by section using AI
  - `readme_generator.py`: main script with repo analysis (language detection, dependency parsing, entry point detection, license detection), section-by-section AI generation, and Jinja2 assembly
  - `prompts/`: four prompt files for description, installation, usage, and contributing sections; each accepts `{REPO_CONTEXT}` placeholder
  - `examples/sample_project/`: built-in TaskFlow CLI app for `--sample` mode (no API key needed for testing)
  - `templates/readme_template.md.j2`: default Jinja2 output template
  - CLI flags: `--input`, `--output`, `--config`, `--prompts`, `--template`, `--sections`, `--analyze`, `--sample`
  - `tests/test_readme_generator.py`: 39 tests covering language detection, project name detection, license detection, dependency parsing, context summary building, sample mode, and README assembly
  - Full tutorial (5 steps), reference docs (configuration, prompt engineering), sample outputs, troubleshooting, and FAQ added to the doc site under `docs/readme-generator/`
  - `config.example.yaml`: added `readme_max_file_lines` and `readme_sections` fields
  - `mkdocs.yml`: README Generator nav section added after Doc Site Portfolio

### Changed
- Tutorial steps 1, 3, 4, and 5 updated to add **Path C: Use Claude Code CLI** as a third AI workflow option alongside the existing script-based paths
  - Step 1: Added Path C to "Choose your path", added a "which path is right for you?" guidance paragraph, added full Path C setup section (install, authenticate, verify), added skip note in "Configure AI access" for Path C users, and added jump-ahead links on all three path names
  - Step 3: Added "Option C" blocks for generating nav structure, homepage, and about page via Claude Code CLI
  - Step 4: Added "Option C" block for generating project pages, plus a callout explaining how Path C users can direct Claude to write output to a file
  - Step 5: Added "Option C" block for content refinement, plus a callout explaining how to reference file paths in prompts

## [1.1.0] - 2026-04-02

### Added

**Release notes automation (01-release-notes-automation)**

- GitLab integration via `python-gitlab` — `GitLabProvider` class with support for self-hosted instances via `gitlab_url` config
- Bitbucket integration via `atlassian-python-api` — `BitbucketProvider` class with app password authentication
- Azure OpenAI provider — `AzureOpenAIProvider` class using the existing `openai` library's `AzureOpenAI` client; requires `azure_endpoint` and `azure_api_version` config fields
- Hybrid categorization pipeline — three-stage strategy: conventional commit prefix parsing → keyword rules → AI fallback; AI only processes commits not matched by earlier stages
- `categorization_rules.example.yaml` — example keyword rules file with pre-built rule sets for Security, Performance, Database, Infrastructure, and Dependencies categories
- Batch processing — `--repos` CLI argument and `batch_repos` config field; `--batch-output` controls separate files per repo or a single combined report
- Custom Jinja2 output templates — `--template` CLI argument accepts any `.j2` file; `templates/default.md.j2` ships as the built-in default and preserves existing output format
- `vcs_provider` config field and `VCS_PROVIDER` environment variable for selecting GitHub, GitLab, or Bitbucket

### Changed

- `generate_release_notes()` signature updated: now accepts categorized commit data (`List[Dict]`) instead of a raw AI response string, enabling template rendering
- `load_config()` no longer requires `github_token` as a universal required field; VCS token validation moved to each provider class to support multiple VCS sources
- `config.example.yaml` updated with sections for all new providers and batch processing options; model recommendation updated to `claude-sonnet-4-6`
- `conftest.py` updated with stubs for `gitlab` and `atlassian` so tests run without those packages installed
- Test suite expanded from 13 to 47 tests, adding `TestParseConventionalCommit`, `TestMatchKeywordRules`, `TestParseAiCategories`, `TestCategorizeCommitsHybrid`, `TestTemplateRendering`, and `TestBatchProcessing`

## [1.0.0] - 2026-04-02

### Added

**Doc site portfolio project (02-doc-site-portfolio)**
- Implemented `generate_content.py` — generates About, Home, project, and site structure pages from a writer profile using Anthropic or OpenAI
- Implemented `improve_content.py` — refines existing Markdown content for clarity, tone, or consistency using AI
- Added `profile.example.yaml` — template writers copy and fill in to drive both content generation scripts
- Wrote all three prompt templates: `about_page_prompt.txt`, `project_page_prompt.txt`, `site_structure_prompt.txt` (previously placeholders)
- Both scripts support `--sample` mode for full testing without API calls

**Tests**
- Added `tests/` directory with pytest test suite (39 tests)
- `tests/test_release_notes.py` — covers sample data, release notes formatting, and fetch with sample flag
- `tests/test_generate_content.py` — covers profile loading, profile/project formatting, and output wrapping
- `tests/conftest.py` — stubs optional dependencies so tests run without installing `anthropic`, `openai`, or `PyGithub`

**Release notes automation project (01-release-notes-automation)**
- Initial project setup with working release notes generation script
- GitHub API integration using PyGithub
- Support for Anthropic Claude and OpenAI GPT providers
- Sample data mode for testing without API calls
- Prompt engineering examples showing evolution from 65% to 91% accuracy
- Workflow worksheet for documenting manual processes
- Configuration management with YAML and environment variable overrides
- Comprehensive MkDocs documentation site
- Troubleshooting guide with 40+ common issues
- Comprehensive FAQ with 50+ questions
- Contributing guidelines and Code of Conduct

### Changed
- Doc site portfolio tutorial steps 1–5 updated to reference the new scripts alongside the existing manual prompting approach
- Tutorial step 1 corrected: AI setup now uses `config.yaml` (matching the actual scripts) instead of a `.env` file with wrong variable names
- Tutorial step 2 now includes a profile setup section for `profile.yaml`

### Documentation
- Complete tutorial covering setup through iteration (release notes)
- Doc site tutorial steps 1–6 covering setup through deployment
- Reference documentation for API integration, prompt engineering, site structure, theme customization, content types, and AI collaboration
- Sample outputs demonstrating categorization quality
- Getting started guide for first-time users
- Portfolio examples with five profile patterns

---

## Release Note Categories

This changelog uses the following categories:

- **Added** - New features or functionality
- **Changed** - Changes to existing functionality
- **Deprecated** - Features that will be removed in future versions
- **Removed** - Features that have been removed
- **Fixed** - Bug fixes
- **Security** - Security vulnerability fixes
- **Documentation** - Documentation improvements

---

## Future Releases (Planned)

### Version 1.2.0 (Planned)
- Web-based configuration UI
- Scheduled automation support
- Integration with CI/CD pipelines
- Multiple output format support (JSON, HTML)
- Internationalization (i18n) support

---

## Versioning Strategy

This project follows [Semantic Versioning](https://semver.org/):

- **MAJOR** version (X.0.0): Incompatible API changes or major rewrites
- **MINOR** version (1.X.0): New features, backward-compatible
- **PATCH** version (1.0.X): Bug fixes, backward-compatible

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to contribute changes to this project.

## Questions?

- **Changelog questions**: [Open an issue](https://github.com/rebeja/docs-automation-examples/issues)
- **Feature requests**: [Open a discussion](https://github.com/rebeja/docs-automation-examples/discussions)
