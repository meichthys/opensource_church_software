#!/usr/bin/env python3
"""
Check all URLs in the repository for broken links.
Generates a report of 404s, timeouts, and redirects.
"""

import re
import requests
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

EXCLUDE_PATTERNS = [
    r"localhost",
    r"127\.0\.0\.1",
    r"example\.com",
    r"your-domain\.com",
]

def should_check(url):
    """Check if URL should be validated."""
    for pattern in EXCLUDE_PATTERNS:
        if re.search(pattern, url):
            return False
    return True

def check_url(url):
    """Check a single URL."""
    try:
        resp = requests.head(url, timeout=10, allow_redirects=True)
        return {
            "url": url,
            "status": resp.status_code,
            "ok": resp.status_code < 400,
            "redirect": resp.history != []
        }
    except requests.exceptions.Timeout:
        return {"url": url, "status": "TIMEOUT", "ok": False, "redirect": False}
    except Exception as e:
        return {"url": url, "status": f"ERROR: {str(e)[:50]}", "ok": False, "redirect": False}

def find_all_urls():
    """Find all URLs in markdown files."""
    urls = set()
    for md_file in Path(".").rglob("*.md"):
        if ".git" in str(md_file):
            continue
        content = md_file.read_text()
        found = re.findall(r'https?://[^\s\)\]\>\"\']+', content)
        for url in found:
            if should_check(url):
                urls.add((str(md_file), url))
    return urls

def main():
    print("Checking links...")
    urls = find_all_urls()
    print(f"Found {len(urls)} unique URLs to check\n")
    
    broken = []
    redirects = []
    
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(check_url, url): (file, url) for file, url in urls}
        
        for future in as_completed(futures):
            file, url = futures[future]
            result = future.result()
            
            if not result["ok"]:
                broken.append({**result, "file": file})
                print(f"❌ {result['status']} | {url[:60]}...")
            elif result["redirect"]:
                redirects.append({**result, "file": file})
                print(f"↪️  Redirect | {url[:60]}...")
            else:
                print(f"✅ {result['status']} | {url[:60]}...")
    
    # Generate report
    report = f"""# Link Check Report
Generated: {datetime.now().isoformat()}

## Summary
- Total URLs checked: {len(urls)}
- Broken: {len(broken)}
- Redirects: {len(redirects)}

"""
    
    if broken:
        report += "## Broken Links\n\n"
        for item in broken:
            report += f"- [{item['file']}]({item['file']}): {item['url']}\n"
            report += f"  - Status: {item['status']}\n\n"
    
    if redirects:
        report += "## Redirects (review recommended)\n\n"
        for item in redirects:
            report += f"- [{item['file']}]({item['file']}): {item['url']}\n"
            report += f"  - Status: {item['status']}\n\n"
    
    Path("link-check-report.md").write_text(report)
    print(f"\nReport saved to link-check-report.md")
    
    return 1 if broken else 0

if __name__ == "__main__":
    exit(main())
