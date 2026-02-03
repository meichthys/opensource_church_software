# Contributing to Church Tech Stack

Thank you for helping maintain this resource for churches!

## What Belongs Here?

**✅ YES:**
- Open-source church software (OSI-approved license)
- Free tiers of open-core products with generous limits
- Tools actively maintained (commit within last 12 months)
- Self-hostable alternatives to commercial church software

**❌ NO:**
- Proprietary software (even if "free")
- Abandoned projects (no commits in 2+ years)
- Affiliate links or sponsored placements
- Tools without clear church use case

## How to Add a Project

### 1. Check It Doesn't Exist
Search existing categories first.

### 2. Verify Requirements
Before submitting, confirm:
- [ ] Open source license (MIT, GPL, Apache, etc.)
- [ ] Last commit within 12 months
- [ ] Basic documentation exists
- [ ] You've personally tested it OR found 3+ church references

### 3. Use the Template

Copy `template.md` from the root and fill in all sections:

```bash
cp template.md categories/[category-name]/[tool-name].md
```

Required fields:
- Status (with date)
- Skill level
- True cost breakdown
- What it does (one sentence)
- Why churches use it (3 bullets)
- Installation options
- Links (website, GitHub, demo, docs)

### 4. Test Your Entry

Run the validation script:

```bash
python tools/validate-entry.py categories/[category-name]/[tool-name].md
```

This checks:
- All required fields present
- URLs are valid
- Date format correct
- No broken markdown

### 5. Submit PR

Use the "New Project" issue template first if you want feedback before writing.

## How to Update a Project

If you notice outdated info:

1. Edit the relevant `.md` file
2. Update the `Last Verified` date
3. Run validation script
4. Submit PR with "Update:" prefix

## How to Remove a Project

Projects are removed when:
- No commits in 24+ months
- Repository archived/deleted
- License changed to proprietary
- Security vulnerabilities unpatched

Use the "Remove Project" issue template with reasoning.

## Decision Trees

### Should this go in "categories" or "stacks"?

**Categories** = Individual tools by function
**Stacks** = Pre-built combinations for specific church profiles

### How do you determine "Skill Level"?

| Level | Can they... |
|-------|-------------|
| Beginner | Use WordPress admin panel |
| Intermediate | Edit config files, use command line |
| Advanced | Set up Docker, manage Linux server |

### What's "True Cost"?

Include ALL costs:
- Software licensing: $0
- Hosting: $X/month
- Domain: $X/year
- Setup time: X hours
- Maintenance: X hours/month

## Code Contributions

### Adding Deployment Scripts

1. Place in `deployments/[type]/[tool-name]/`
2. Include README with prerequisites
3. Test on fresh VPS/container
4. Document tested versions

### Improving Automation

The `tools/` directory uses Python 3.8+:

```bash
cd tools
pip install -r requirements.txt
python check-links.py  # Run manually
```

GitHub Actions run these automatically.

## Style Guide

### Writing
- Use second person ("you can...")
- Be concise — pastors are busy
- Link to official docs, don't duplicate
- Use emojis sparingly

### Formatting
- YAML frontmatter for metadata
- Markdown tables for comparisons
- Code blocks for commands
- Screenshots in `assets/` with descriptive names

## Community

- Discussions: Use GitHub Discussions for Q&A
- Issues: Bug reports, updates, removals
- PRs: New content, corrections

## Recognition

Contributors will be listed in CONTRIBUTORS.md.

Major contributions (new categories, stacks, guides) get a shoutout in release notes.

## Questions?

Open a Discussion or DM the maintainers.

---

*Thanks for helping churches steward their resources wisely!*
