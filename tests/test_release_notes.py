"""Tests for the release notes generation script."""

import sys
import os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '01-release-notes-automation'))

from generate_release_notes import (
    get_sample_commits,
    generate_release_notes,
    fetch_commits,
    parse_conventional_commit,
    match_keyword_rules,
    parse_ai_categories,
    categorize_commits_hybrid,
    CATEGORY_ORDER,
)


# ─── Helpers ──────────────────────────────────────────────────────────────────

def _make_commit(sha, message):
    return {"sha": sha, "message": message, "author": "dev", "date": "2024-01-01", "url": f"http://example.com/{sha}"}


def _sample_categories():
    return [
        {"name": "New Features", "commits": [_make_commit("abc123", "Add login page")]},
        {"name": "Bug Fixes", "commits": [_make_commit("def456", "Fix crash on startup")]},
        {"name": "Enhancements", "commits": []},
        {"name": "Documentation", "commits": []},
    ]


# ─── TestGetSampleCommits ─────────────────────────────────────────────────────

class TestGetSampleCommits:
    def test_returns_list(self):
        commits = get_sample_commits()
        assert isinstance(commits, list)

    def test_returns_commits(self):
        commits = get_sample_commits()
        assert len(commits) > 0

    def test_commit_has_required_keys(self):
        required_keys = {'sha', 'message', 'author', 'date', 'url'}
        for commit in get_sample_commits():
            assert required_keys.issubset(commit.keys()), f"Commit missing keys: {commit}"

    def test_commit_values_are_strings(self):
        for commit in get_sample_commits():
            for key in ('sha', 'message', 'author', 'date', 'url'):
                assert isinstance(commit[key], str), f"commit['{key}'] should be a string"

    def test_commit_dates_are_formatted(self):
        for commit in get_sample_commits():
            assert len(commit['date']) == 10, f"Expected YYYY-MM-DD, got: {commit['date']}"
            assert commit['date'][4] == '-'
            assert commit['date'][7] == '-'


# ─── TestGenerateReleaseNotes ─────────────────────────────────────────────────

class TestGenerateReleaseNotes:
    def test_includes_header(self):
        result = generate_release_notes(_sample_categories(), "2024-01-01", "owner/repo")
        assert "# Release Notes" in result

    def test_includes_repo_name(self):
        result = generate_release_notes(_sample_categories(), "2024-01-01", "owner/repo")
        assert "owner/repo" in result

    def test_includes_since_date(self):
        result = generate_release_notes(_sample_categories(), "2024-01-01", "owner/repo")
        assert "2024-01-01" in result

    def test_includes_commit_messages(self):
        result = generate_release_notes(_sample_categories(), "2024-01-01", "owner/repo")
        assert "Add login page" in result
        assert "Fix crash on startup" in result

    def test_includes_review_disclaimer(self):
        result = generate_release_notes(_sample_categories(), "2024-01-01", "owner/repo")
        assert "review" in result.lower()

    def test_returns_string(self):
        result = generate_release_notes(_sample_categories(), "2024-01-01", "owner/repo")
        assert isinstance(result, str)

    def test_empty_categories(self):
        empty = [{"name": name, "commits": []} for name in CATEGORY_ORDER]
        result = generate_release_notes(empty, "2024-01-01", "owner/repo")
        assert "# Release Notes" in result
        assert isinstance(result, str)

    def test_skips_empty_category_sections(self):
        result = generate_release_notes(_sample_categories(), "2024-01-01", "owner/repo")
        # Enhancements and Documentation have no commits, should not appear as headers
        assert "## Enhancements" not in result
        assert "## Documentation" not in result


# ─── TestFetchCommitsWithSampleData ───────────────────────────────────────────

class TestFetchCommitsWithSampleData:
    def test_returns_sample_when_flag_set(self):
        commits = fetch_commits("any/repo", "2024-01-01", config={}, use_sample=True)
        assert commits == get_sample_commits()

    def test_sample_commit_count_matches(self):
        commits = fetch_commits("any/repo", "2024-01-01", config={}, use_sample=True)
        assert len(commits) == len(get_sample_commits())

    def test_sample_ignores_repo_argument(self):
        commits_a = fetch_commits("owner/repo-a", "2024-01-01", config={}, use_sample=True)
        commits_b = fetch_commits("owner/repo-b", "2024-01-01", config={}, use_sample=True)
        assert commits_a == commits_b


# ─── TestHybridCategorization ─────────────────────────────────────────────────

class TestParseConventionalCommit:
    def test_feat_prefix(self):
        assert parse_conventional_commit("feat: add login") == "New Features"

    def test_feature_prefix(self):
        assert parse_conventional_commit("feature: new dashboard") == "New Features"

    def test_fix_prefix(self):
        assert parse_conventional_commit("fix: resolve timeout") == "Bug Fixes"

    def test_docs_prefix(self):
        assert parse_conventional_commit("docs: update readme") == "Documentation"

    def test_chore_prefix(self):
        assert parse_conventional_commit("chore: update deps") == "Enhancements"

    def test_scoped_commit(self):
        assert parse_conventional_commit("fix(auth): token expiry") == "Bug Fixes"

    def test_breaking_change_marker(self):
        assert parse_conventional_commit("feat!: drop Python 3.8") == "New Features"

    def test_scoped_breaking_change(self):
        assert parse_conventional_commit("refactor(api)!: rename endpoints") == "Enhancements"

    def test_unrecognized_prefix(self):
        assert parse_conventional_commit("wip: not done yet") is None

    def test_no_prefix(self):
        assert parse_conventional_commit("Add user authentication") is None

    def test_empty_message(self):
        assert parse_conventional_commit("") is None


class TestMatchKeywordRules:
    RULES = [
        {"keywords": ["auth", "token", "oauth"], "category": "Security"},
        {"keywords": ["perf", "latency", "cache"], "category": "Performance"},
    ]

    def test_matches_keyword(self):
        assert match_keyword_rules("add oauth support", self.RULES) == "Security"

    def test_case_insensitive(self):
        assert match_keyword_rules("Improve CACHE performance", self.RULES) == "Performance"

    def test_first_rule_wins(self):
        # "auth" matches Security before Performance keywords
        assert match_keyword_rules("auth cache fix", self.RULES) == "Security"

    def test_no_match_returns_none(self):
        assert match_keyword_rules("fix typo in readme", self.RULES) is None

    def test_empty_rules(self):
        assert match_keyword_rules("auth fix", []) is None


class TestParseAiCategories:
    def test_parses_standard_response(self):
        response = (
            "## New Features\n"
            "- Add login page ([abc123](http://example.com))\n"
            "## Bug Fixes\n"
            "- Fix crash ([def456](http://example.com))\n"
        )
        result = parse_ai_categories(response)
        assert "New Features" in result
        assert "Bug Fixes" in result
        assert len(result["New Features"]) == 1
        assert len(result["Bug Fixes"]) == 1

    def test_empty_category(self):
        response = "## New Features\n## Bug Fixes\n- Fix crash\n"
        result = parse_ai_categories(response)
        assert result["New Features"] == []
        assert len(result["Bug Fixes"]) == 1

    def test_empty_response(self):
        assert parse_ai_categories("") == {}


class TestCategorizeCommitsHybrid:
    def test_conventional_commits_require_no_ai(self):
        commits = [
            _make_commit("a1", "feat: add login"),
            _make_commit("b2", "fix: resolve crash"),
            _make_commit("c3", "docs: update readme"),
        ]
        # No prompt_path needed when all commits match rules — pass a dummy path
        result = categorize_commits_hybrid(commits, config={}, prompt_path="nonexistent.txt")
        features = next(c for c in result if c["name"] == "New Features")
        fixes = next(c for c in result if c["name"] == "Bug Fixes")
        docs = next(c for c in result if c["name"] == "Documentation")
        assert len(features["commits"]) == 1
        assert features["commits"][0]["sha"] == "a1"
        assert len(fixes["commits"]) == 1
        assert len(docs["commits"]) == 1

    def test_keyword_rules_applied_before_ai(self, tmp_path):
        # Write a rules file so categorize_commits_hybrid can load it
        rules_file = tmp_path / "rules.yaml"
        rules_file.write_text("rules:\n  - keywords: [cache]\n    category: Performance\n")
        commits = [_make_commit("x1", "improve cache hit rate")]
        result = categorize_commits_hybrid(
            commits, config={}, prompt_path="nonexistent.txt",
            rules_path=str(rules_file)
        )
        # Commit matched by keyword rule — AI stage never reached (no prompt file needed)
        perf = next((c for c in result if c["name"] == "Performance"), None)
        assert perf is not None
        assert len(perf["commits"]) == 1
        assert perf["commits"][0]["sha"] == "x1"

    def test_result_contains_all_standard_categories(self):
        commits = [_make_commit("a1", "feat: add feature")]
        result = categorize_commits_hybrid(commits, config={}, prompt_path="nonexistent.txt")
        names = [c["name"] for c in result]
        for expected in CATEGORY_ORDER:
            assert expected in names

    def test_standard_categories_appear_first(self):
        commits = [_make_commit("a1", "feat: add feature")]
        result = categorize_commits_hybrid(commits, config={}, prompt_path="nonexistent.txt")
        first_four = [c["name"] for c in result[:4]]
        assert first_four == CATEGORY_ORDER

    def test_empty_commits_returns_empty_categories(self):
        result = categorize_commits_hybrid([], config={}, prompt_path="nonexistent.txt")
        assert all(len(c["commits"]) == 0 for c in result)


# ─── TestTemplateRendering ────────────────────────────────────────────────────

class TestTemplateRendering:
    def test_default_template_includes_header(self):
        result = generate_release_notes(_sample_categories(), "2024-01-01", "owner/repo")
        assert "# Release Notes" in result

    def test_default_template_includes_category_names(self):
        result = generate_release_notes(_sample_categories(), "2024-01-01", "owner/repo")
        assert "New Features" in result
        assert "Bug Fixes" in result

    def test_template_variables_rendered(self):
        result = generate_release_notes(
            _sample_categories(), "2024-01-01", "myorg/myrepo",
            config={"ai_provider": "anthropic", "vcs_provider": "github"}
        )
        assert "myorg/myrepo" in result
        assert "2024-01-01" in result

    def test_custom_template_file(self, tmp_path):
        template_file = tmp_path / "custom.md.j2"
        template_file.write_text("REPO={{ repo }} DATE={{ date }} SINCE={{ since_date }}")
        result = generate_release_notes(
            _sample_categories(), "2024-01-01", "owner/repo",
            template_path=str(template_file)
        )
        assert "REPO=owner/repo" in result
        assert "SINCE=2024-01-01" in result

    def test_missing_custom_template_falls_back_to_default(self):
        result = generate_release_notes(
            _sample_categories(), "2024-01-01", "owner/repo",
            template_path="/nonexistent/template.j2"
        )
        assert "# Release Notes" in result


# ─── TestBatchProcessing ──────────────────────────────────────────────────────

class TestBatchProcessing:
    def test_run_batch_writes_separate_files(self, tmp_path, monkeypatch):
        from generate_release_notes import run_batch

        # Monkeypatch to avoid real VCS/AI calls
        monkeypatch.setattr(
            "generate_release_notes.get_vcs_provider",
            lambda config: type("P", (), {"fetch_commits": lambda self, *a, **kw: get_sample_commits()})()
        )
        monkeypatch.setattr(
            "generate_release_notes.categorize_commits_hybrid",
            lambda commits, config, prompt_path, rules_path: _sample_categories()
        )
        monkeypatch.chdir(tmp_path)

        class Args:
            since = "2024-01-01"
            sample = False
            prompt = "prompts/categorization_prompt.txt"
            rules = None
            template = None
            output = "combined.md"
            batch_output = "separate"

        run_batch(["owner/repo-a", "owner/repo-b"], Args(), config={})

        assert (tmp_path / "release-notes-owner-repo-a.md").exists()
        assert (tmp_path / "release-notes-owner-repo-b.md").exists()

    def test_run_batch_writes_combined_file(self, tmp_path, monkeypatch):
        from generate_release_notes import run_batch

        monkeypatch.setattr(
            "generate_release_notes.get_vcs_provider",
            lambda config: type("P", (), {"fetch_commits": lambda self, *a, **kw: get_sample_commits()})()
        )
        monkeypatch.setattr(
            "generate_release_notes.categorize_commits_hybrid",
            lambda commits, config, prompt_path, rules_path: _sample_categories()
        )
        monkeypatch.chdir(tmp_path)

        class Args:
            since = "2024-01-01"
            sample = False
            prompt = "prompts/categorization_prompt.txt"
            rules = None
            template = None
            output = "combined.md"
            batch_output = "combined"

        run_batch(["owner/repo-a", "owner/repo-b"], Args(), config={})

        combined = tmp_path / "combined.md"
        assert combined.exists()
        content = combined.read_text()
        assert "owner/repo-a" in content
        assert "owner/repo-b" in content
