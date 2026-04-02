"""
Pytest configuration and shared fixtures.

Provides stub modules for optional third-party dependencies so the scripts
can be imported during testing without those packages being installed.
Only pure-Python functions are tested here; any tests that require real
API calls are integration tests and are not included.
"""

import sys
from unittest.mock import MagicMock


def _stub_if_missing(module_name: str, stub=None):
    """Register a stub module only if the real package is not installed."""
    if module_name not in sys.modules:
        sys.modules[module_name] = stub or MagicMock()


# --- PyGithub ---
github_stub = MagicMock()
github_stub.GithubException = type(
    'GithubException', (Exception,), {'data': {}, 'status': 0}
)
_stub_if_missing('github', github_stub)

# --- Anthropic ---
_stub_if_missing('anthropic')

# --- OpenAI ---
_stub_if_missing('openai')

# --- python-gitlab ---
_stub_if_missing('gitlab')

# --- atlassian-python-api ---
_stub_if_missing('atlassian')
