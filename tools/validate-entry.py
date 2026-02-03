#!/usr/bin/env python3
"""
Validate a project entry markdown file.
Checks for required fields, valid URLs, and proper formatting.
"""

import sys
import re
import requests
from pathlib import Path
from datetime import datetime

def validate_file(filepath):
    """Validate a single markdown file."""
    content = Path(filepath).read_text()
    errors = []
    warnings = []
    
    # Required sections
    required_sections = [
        ("Status:", r"Status:\s*[✅⚠️❌]\s*Active|Status:\s*[✅⚠️❌]\s*Inactive|Status:\s*[✅⚠️❌]\s*Archived"),
        ("Skill Level:", r"Skill Level:\s*(Beginner|Intermediate|Advanced)"),
        ("True Cost:", r"True Cost:"),
        ("What It Does:", r"What It Does:"),
        ("GitHub:", r"GitHub:\s*https://github\.com/"),
    ]
    
    for name, pattern in required_sections:
        if not re.search(pattern, content, re.IGNORECASE):
            errors.append(f"Missing or invalid: {name}")
    
    # Date format check
    date_pattern = r"\d{4}-\d{2}-\d{2}"
    dates = re.findall(date_pattern, content)
    for date_str in dates:
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            errors.append(f"Invalid date format: {date_str}")
    
    # URL validation (sample, not all)
    urls = re.findall(r'https?://[^\s\)]+', content)
    for url in urls[:3]:  # Check first 3 URLs only
        try:
            resp = requests.head(url, timeout=5, allow_redirects=True)
            if resp.status_code >= 400:
                warnings.append(f"URL may be broken ({resp.status_code}): {url}")
        except Exception as e:
            warnings.append(f"Could not check URL: {url}")
    
    # Print results
    print(f"\nValidating: {filepath}")
    print("=" * 50)
    
    if errors:
        print("\n❌ ERRORS:")
        for e in errors:
            print(f"  - {e}")
    
    if warnings:
        print("\n⚠️  WARNINGS:")
        for w in warnings:
            print(f"  - {w}")
    
    if not errors and not warnings:
        print("✅ All checks passed!")
        return 0
    elif not errors:
        print("\n✅ Validation passed with warnings")
        return 0
    else:
        print(f"\n❌ Validation failed with {len(errors)} errors")
        return 1

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validate-entry.py <path-to-md-file>")
        sys.exit(1)
    
    sys.exit(validate_file(sys.argv[1]))
