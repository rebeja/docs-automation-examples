"""Tests for the README generator script."""

import sys
import os
import json
import pytest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '03-readme-generator'))

from readme_generator import (
    detect_language,
    detect_project_name,
    detect_license,
    parse_dependencies,
    build_context_summary,
    get_sample_repo_context,
    assemble_readme,
    ALL_SECTIONS,
)


# ─── Helpers ──────────────────────────────────────────────────────────────────

def _make_context(**overrides):
    base = {
        'name': 'myproject',
        'language': 'Python',
        'dependencies': ['click', 'requests'],
        'entry_points': ['main.py'],
        'license': 'MIT',
        'existing_readme': '',
        'file_tree': ['main.py', 'requirements.txt', 'LICENSE'],
        'key_files': {'main.py': '#!/usr/bin/env python3\nprint("hello")'},
    }
    base.update(overrides)
    return base


def _sample_sections():
    return {
        'description': '# myproject\n\nA great tool.',
        'installation': '## Installation\n\n```bash\npip install myproject\n```',
        'usage': '## Usage\n\n```bash\npython main.py\n```',
        'contributing': '## Contributing\n\nPRs welcome.',
    }


# ─── TestDetectLanguage ───────────────────────────────────────────────────────

class TestDetectLanguage:
    def test_detects_python(self):
        assert detect_language(['main.py', 'utils.py', 'README.md']) == 'Python'

    def test_detects_javascript(self):
        assert detect_language(['index.js', 'app.js', 'utils.js']) == 'JavaScript'

    def test_detects_typescript(self):
        assert detect_language(['index.ts', 'server.ts']) == 'TypeScript'

    def test_detects_go(self):
        assert detect_language(['main.go', 'handler.go']) == 'Go'

    def test_returns_most_common(self):
        # 3 Python files vs 1 JS file → Python wins
        assert detect_language(['a.py', 'b.py', 'c.py', 'index.js']) == 'Python'

    def test_unknown_extensions(self):
        assert detect_language(['README.md', 'Makefile', '.gitignore']) == 'Unknown'

    def test_empty_list(self):
        assert detect_language([]) == 'Unknown'


# ─── TestDetectProjectName ────────────────────────────────────────────────────

class TestDetectProjectName:
    def test_reads_package_json(self):
        contents = {'package.json': json.dumps({'name': 'my-awesome-app'})}
        assert detect_project_name(contents, 'fallback') == 'my-awesome-app'

    def test_reads_pyproject_toml(self):
        contents = {'pyproject.toml': '[tool.poetry]\nname = "my-lib"\nversion = "1.0"'}
        assert detect_project_name(contents, 'fallback') == 'my-lib'

    def test_reads_cargo_toml(self):
        contents = {'Cargo.toml': '[package]\nname = "my-crate"\nversion = "0.1.0"'}
        assert detect_project_name(contents, 'fallback') == 'my-crate'

    def test_falls_back_to_directory_name(self):
        assert detect_project_name({}, 'my-directory') == 'my-directory'

    def test_invalid_package_json_falls_back(self):
        contents = {'package.json': 'not valid json'}
        assert detect_project_name(contents, 'fallback') == 'fallback'


# ─── TestDetectLicense ────────────────────────────────────────────────────────

class TestDetectLicense:
    def test_detects_mit(self):
        assert detect_license({'LICENSE': 'MIT License\n\nCopyright...'}) == 'MIT'

    def test_detects_apache(self):
        assert detect_license({'LICENSE': 'Apache License\nVersion 2.0'}) == 'Apache 2.0'

    def test_detects_gpl(self):
        assert detect_license({'LICENSE': 'GNU General Public License'}) == 'GPL'

    def test_no_license_file(self):
        assert detect_license({}) == 'Not specified'

    def test_custom_license(self):
        assert detect_license({'LICENSE': 'Proprietary software. All rights reserved.'}) == 'Custom'


# ─── TestParseDependencies ────────────────────────────────────────────────────

class TestParseDependencies:
    def test_parses_requirements_txt(self):
        contents = {'requirements.txt': 'click>=8.0\nrequests==2.28\npyyaml\n# comment\n'}
        deps = parse_dependencies(contents)
        assert 'click' in deps
        assert 'requests' in deps
        assert 'pyyaml' in deps

    def test_skips_comments(self):
        contents = {'requirements.txt': '# this is a comment\nflask\n'}
        deps = parse_dependencies(contents)
        assert '# this is a comment' not in deps
        assert 'flask' in deps

    def test_parses_package_json(self):
        pkg = {'dependencies': {'express': '^4.0', 'lodash': '^4.0'}, 'devDependencies': {'jest': '^29'}}
        contents = {'package.json': json.dumps(pkg)}
        deps = parse_dependencies(contents)
        assert 'express' in deps
        assert 'lodash' in deps
        assert 'jest' in deps

    def test_empty_files(self):
        assert parse_dependencies({}) == []

    def test_caps_at_20(self):
        lines = '\n'.join([f'pkg{i}' for i in range(30)])
        contents = {'requirements.txt': lines}
        deps = parse_dependencies(contents)
        assert len(deps) <= 20


# ─── TestBuildContextSummary ──────────────────────────────────────────────────

class TestBuildContextSummary:
    def test_includes_project_name(self):
        summary = build_context_summary(_make_context(name='my-tool'))
        assert 'my-tool' in summary

    def test_includes_language(self):
        summary = build_context_summary(_make_context(language='Go'))
        assert 'Go' in summary

    def test_includes_dependencies(self):
        summary = build_context_summary(_make_context(dependencies=['flask', 'sqlalchemy']))
        assert 'flask' in summary

    def test_includes_file_tree(self):
        summary = build_context_summary(_make_context(file_tree=['main.py', 'README.md']))
        assert 'main.py' in summary

    def test_includes_key_file_content(self):
        summary = build_context_summary(_make_context(key_files={'app.py': 'print("hello")'}))
        assert 'print("hello")' in summary

    def test_returns_string(self):
        assert isinstance(build_context_summary(_make_context()), str)


# ─── TestSampleMode ───────────────────────────────────────────────────────────

class TestSampleMode:
    def test_returns_dict(self):
        context = get_sample_repo_context()
        assert isinstance(context, dict)

    def test_has_required_keys(self):
        required = {'name', 'language', 'dependencies', 'entry_points', 'license', 'file_tree', 'key_files'}
        context = get_sample_repo_context()
        assert required.issubset(context.keys())

    def test_name_is_string(self):
        assert isinstance(get_sample_repo_context()['name'], str)

    def test_dependencies_is_list(self):
        assert isinstance(get_sample_repo_context()['dependencies'], list)

    def test_file_tree_is_list(self):
        assert isinstance(get_sample_repo_context()['file_tree'], list)


# ─── TestReadmeAssembly ───────────────────────────────────────────────────────

class TestReadmeAssembly:
    def test_includes_all_sections(self):
        result = assemble_readme(_sample_sections(), _make_context())
        assert '# myproject' in result
        assert '## Installation' in result
        assert '## Usage' in result
        assert '## Contributing' in result

    def test_includes_disclaimer(self):
        result = assemble_readme(_sample_sections(), _make_context())
        assert 'AI assistance' in result

    def test_returns_string(self):
        assert isinstance(assemble_readme(_sample_sections(), _make_context()), str)

    def test_empty_sections_excluded(self):
        sections = {**_sample_sections(), 'contributing': ''}
        result = assemble_readme(sections, _make_context())
        # Contributing content should not appear
        assert 'PRs welcome' not in result

    def test_custom_template(self, tmp_path):
        template = tmp_path / 'custom.md.j2'
        template.write_text("PROJECT={{ project_name }}\nLANG={{ language }}")
        result = assemble_readme(_sample_sections(), _make_context(), template_path=str(template))
        assert 'PROJECT=myproject' in result
        assert 'LANG=Python' in result

    def test_missing_template_falls_back_to_default(self):
        result = assemble_readme(_sample_sections(), _make_context(), template_path='/nonexistent/template.j2')
        assert '# myproject' in result
