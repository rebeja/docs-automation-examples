# API Integration Reference

How the release notes automation integrates with GitHub and AI provider APIs.

## Overview

The automation connects to two types of APIs:

1. **GitHub API** - Fetches commit data
2. **AI Provider API** - Categorizes commits

Both use standard REST/HTTP patterns with authentication tokens.

## GitHub API Integration

### Authentication

Uses personal access tokens (PAT):

```yaml
# config.yaml
github_token: "ghp_xxxxxxxxxxxx"
```

### API Endpoints Used

**Get Repository:**
```
GET /repos/:owner/:repo
```

**Get Commits:**
```
GET /repos/:owner/:repo/commits?since=YYYY-MM-DD
```

### Code Example

```python
from github import Github

# Initialize client
g = Github(config['github_token'])

# Get repository
repo = g.get_repo('owner/repo')

# Fetch commits since date
since = datetime.strptime('2024-01-01', '%Y-%m-%d')
commits = repo.get_commits(since=since)

# Process commits
for commit in commits:
    print(f"{commit.sha}: {commit.commit.message}")
```

### Rate Limits

- **Authenticated:** 5,000 requests/hour
- **Unauthenticated:** 60 requests/hour

**Checking limits:**
```python
rate_limit = g.get_rate_limit()
print(f"Remaining: {rate_limit.core.remaining}")
print(f"Resets at: {rate_limit.core.reset}")
```

### Error Handling

**Common errors:**

| Status Code | Meaning | Solution |
|-------------|---------|----------|
| 401 | Bad credentials | Check token is valid |
| 403 | Rate limit or permissions | Wait or check scopes |
| 404 | Repository not found | Verify repo name and access |

## AI Provider Integration

### Anthropic (Claude)

**Authentication:**
```yaml
ai_provider: "anthropic"
ai_api_key: "sk-ant-xxxxx"
model: "claude-3-sonnet-20240229"
```

**API Call:**
```python
import anthropic

client = anthropic.Anthropic(api_key=config['ai_api_key'])

message = client.messages.create(
    model=config['model'],
    max_tokens=3000,
    temperature=0.3,
    messages=[{
        "role": "user",
        "content": prompt
    }]
)

response_text = message.content[0].text
```

**Pricing:**
- Claude 3 Sonnet: ~$0.015-0.02 per release notes generation
- Claude 3 Opus: ~$0.03-0.05 per generation

### OpenAI (GPT)

**Authentication:**
```yaml
ai_provider: "openai"
ai_api_key: "sk-xxxxx"
model: "gpt-4"
```

**API Call:**
```python
import openai

client = openai.OpenAI(api_key=config['ai_api_key'])

response = client.chat.completions.create(
    model=config['model'],
    messages=[{
        "role": "user",
        "content": prompt
    }],
    max_tokens=3000,
    temperature=0.3
)

response_text = response.choices[0].message.content
```

**Pricing:**
- GPT-4: ~$0.02-0.03 per generation
- GPT-3.5-turbo: ~$0.005-0.01 per generation

## Data Flow

```
1. Load Configuration
   ↓
2. Authenticate with GitHub
   ↓
3. Fetch Commits (GitHub API)
   ↓
4. Format for AI (prompt template)
   ↓
5. Categorize (AI Provider API)
   ↓
6. Format Output (Markdown)
   ↓
7. Save to File
```

## Configuration Management

### Environment Variables

For production, use environment variables:

```bash
export GITHUB_TOKEN="ghp_xxxxx"
export AI_API_KEY="sk-ant-xxxxx"
export AI_PROVIDER="anthropic"
export AI_MODEL="claude-3-sonnet-20240229"
```

### Config File Priority

1. Command line arguments (highest)
2. Environment variables
3. `config.yaml` file (lowest)

### Security

**DO ✅:**
- Use environment variables in CI/CD
- Rotate tokens every 90 days
- Use minimal GitHub token scopes
- Store tokens in password manager

**DON'T ❌:**
- Commit config.yaml with real keys
- Share tokens in Slack/email
- Use production keys for testing
- Log API keys in error messages

## Error Handling

### GitHub API Errors

```python
from github import GithubException

try:
    commits = fetch_commits(repo, since_date, config)
except GithubException as e:
    if e.status == 401:
        print("Invalid GitHub token")
    elif e.status == 404:
        print("Repository not found")
    elif e.status == 403:
        print("Rate limit exceeded")
```

### AI API Errors

```python
try:
    response = categorize_commits(commits, config)
except anthropic.APIError as e:
    print(f"AI API error: {e}")
except anthropic.RateLimitError as e:
    print("Rate limit exceeded, wait and retry")
```

## Performance Optimization

### Reduce API Calls

**GitHub:**
- Fetch commits in batches
- Cache results locally
- Use specific date ranges

**AI Provider:**
- Batch commits in single request (up to token limit)
- Cache categorization results
- Don't re-process unchanged commits

### Retry Strategy

```python
import time
from tenacity import retry, stop_after_attempt, wait_exponential

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=10)
)
def fetch_with_retry(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
```

## Alternative Platforms

### GitLab

```python
import gitlab

gl = gitlab.Gitlab('https://gitlab.com', private_token=token)
project = gl.projects.get('owner/repo')
commits = project.commits.list(since='2024-01-01')
```

### Bitbucket

```python
import requests

url = f"https://api.bitbucket.org/2.0/repositories/{owner}/{repo}/commits"
headers = {"Authorization": f"Bearer {token}"}
response = requests.get(url, headers=headers)
commits = response.json()['values']
```

## Monitoring and Logging

### Track API Usage

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info(f"Fetching commits from {repo} since {since_date}")
logger.info(f"Found {len(commits)} commits")
logger.info(f"AI categorization complete, cost: ${estimated_cost}")
```

### Cost Tracking

```python
def estimate_cost(commit_count, provider, model):
    # Rough estimates per 1000 tokens
    costs = {
        'anthropic': {'sonnet': 0.003, 'opus': 0.015},
        'openai': {'gpt-4': 0.03, 'gpt-3.5-turbo': 0.001}
    }
    
    # Estimate tokens (commits + prompt)
    estimated_tokens = commit_count * 50 + 1000
    
    return (estimated_tokens / 1000) * costs[provider][model]
```

## Testing

### Mock API Responses

```python
from unittest.mock import Mock, patch

@patch('github.Github')
def test_fetch_commits(mock_github):
    # Mock GitHub API
    mock_repo = Mock()
    mock_repo.get_commits.return_value = [
        Mock(sha='abc123', commit=Mock(message='Test commit'))
    ]
    mock_github.return_value.get_repo.return_value = mock_repo
    
    # Test function
    commits = fetch_commits('owner/repo', '2024-01-01', config)
    assert len(commits) == 1
```

## Troubleshooting

### Connection Issues

```bash
# Test GitHub API access
curl -H "Authorization: token YOUR_TOKEN" \
  https://api.github.com/user

# Test Anthropic API
curl https://api.anthropic.com/v1/messages \
  -H "x-api-key: YOUR_KEY" \
  -H "anthropic-version: 2023-06-01"
```

### Debug Mode

```python
# Enable verbose output
import http.client
http.client.HTTPConnection.debuglevel = 1
```

---

**Related:**
- [Configuration Reference](configuration.md)
- [Troubleshooting Guide](../troubleshooting.md)
- [FAQ](../faq.md)
