#!/usr/bin/env python3
"""
Update project status based on GitHub API.
Checks last commit dates and flags stale projects.
"""

import re
import requests
from pathlib import Path
from datetime import datetime, timedelta
import os

def get_last_commit(repo_url):
    """Get last commit date from GitHub API."""
    # Extract owner/repo from URL
    match = re.search(r"github\.com/([^/]+)/([^/]+)", repo_url)
    if not match:
        return None
    
    owner, repo = match.groups()
    repo = repo.replace(".git", "").rstrip("/")
    
    api_url = f"https://api.github.com/repos/{owner}/{repo}/commits?per_page=1"
    
    headers = {}
    if "GITHUB_TOKEN" in os.environ:
        headers["Authorization"] = f"token {os.environ['GITHUB_TOKEN']}"
    
    try:
        resp = requests.get(api_url, headers=headers, timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            if data:
                return data[0]["commit"]["committer"]["date"][:10]
    except Exception as e:
        print(f"Error checking {repo_url}: {e}")
    
    return None

def update_file_status(filepath):
    """Update status in a single markdown file."""
    content = Path(filepath).read_text()
    original = content
    
    # Find GitHub URL
    match = re.search(r"GitHub:\s*(https://github\.com/[^\s\n]+)", content)
    if not match:
        return False
    
    github_url = match.group(1)
    last_commit = get_last_commit(github_url)
    
    if not last_commit:
        return False
    
    # Determine status
    commit_date = datetime.strptime(last_commit, "%Y-%m-%d")
    days_since = (datetime.now() - commit_date).days
    
    if days_since < 180:
        new_status = f"✅ Active (last commit: {last_commit})"
    elif days_since < 365:
        new_status = f"⚠️ Maintenance mode (last commit: {last_commit})"
    else:
        new_status = f"❌ Stale (last commit: {last_commit})"
    
    # Update content
    content = re.sub(
        r"Status:\s*[✅⚠️❌]\s*[^\n]*",
        f"Status: {new_status}",
        content
    )
    
    # Update last verified date
    today = datetime.now().strftime("%Y-%m-%d")
    content = re.sub(
        r"Last Verified:\s*\d{4}-\d{2}-\d{2}",
        f"Last Verified: {today}",
        content
    )
    
    if content != original:
        Path(filepath).write_text(content)
        print(f"Updated: {filepath} -> {new_status}")
        return True
    
    return False

def main():
    updated = 0
    for md_file in Path("categories").rglob("*.md"):
        if update_file_status(md_file):
            updated += 1
    
    print(f"\nUpdated {updated} files")
    return 0

if __name__ == "__main__":
    exit(main())
