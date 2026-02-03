# GitHub Workflows & Templates - Manual Setup Required

These files need to be added via the GitHub web interface because they require
`workflow` scope permissions that the current OAuth token doesn't have.

## Files to Add

### Workflows (`.github/workflows/`)

1. **link-checker.yml** - Weekly automated link validation
2. **stale-checker.yml** - Monthly status updates for projects

### Issue Templates (`.github/ISSUE_TEMPLATE/`)

1. **new-project.yml** - Form for submitting new tools
2. **update-project.yml** - Form for updating existing entries
3. **remove-project.yml** - Form for deprecating stale projects

### PR Template (`.github/`)

1. **PULL_REQUEST_TEMPLATE.md** - Standardized PR checklist

## How to Add

### Via GitHub Web UI:

1. Go to your fork: https://github.com/boomertechie/opensource_church_software
2. Click **"Add file"** → **"Create new file"**
3. Enter path: `.github/workflows/link-checker.yml`
4. Copy contents from `link-checker.yml` in this directory
5. Commit to main
6. Repeat for other files

### Via Local Push (if you have proper permissions):

```bash
git add .github/
git commit -m "Add GitHub Actions and issue templates"
git push origin main
```

## After Adding

1. Go to **Actions** tab in your repo
2. Enable workflows if prompted
3. The link-checker will run weekly (Sundays)
4. The stale-checker runs monthly (1st of each month)

## Required Secrets

The stale-checker workflow needs a GitHub token with API access:

1. Go to **Settings** → **Secrets and variables** → **Actions**
2. Click **New repository secret**
3. Name: `GITHUB_TOKEN`
4. Value: Create a personal access token at https://github.com/settings/tokens
   - Required scopes: `repo`, `workflow`

## Testing

To test workflows manually:

1. Go to **Actions** tab
2. Select the workflow
3. Click **Run workflow**

---

*These files are kept here because the automated push was blocked by GitHub's
OAuth security policy for workflow files.*
