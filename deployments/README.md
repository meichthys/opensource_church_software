# Docker Compose Deployments

Ready-to-deploy Docker Compose stacks for self-hosting church software.

## Choose Your Stack

| Stack | Best For | RAM | What's Included |
|-------|----------|-----|-----------------|
| **[Starter](starter/)** | Most churches | 2GB | WordPress, ChurchCRM, Listmonk, Vaultwarden |
| [Church Plant](church-plant/) | Minimal setup | 1-2GB | WordPress, ChurchCRM only |
| [Small Church](small-church/) | Need file sharing | 2-4GB | + Nextcloud, Monitoring |
| [Privacy-First](privacy-first/) | Full self-hosted | 4-8GB | + Jitsi, OnlyOffice, Backups |

**Start with [Starter](starter/)** unless you have a specific reason for the others.

## Quick Start

```bash
cd deployments/starter
cp .env.example .env
# Edit .env with your domains and passwords
docker compose up -d
```

## What You Need

- A VPS with 2GB+ RAM ($10-12/month from DigitalOcean, Linode, or Vultr)
- A domain name pointed to your server
- Basic command line familiarity (copy/paste is fine)

## Stack Comparison

| Feature | Starter | Church Plant | Small Church | Privacy-First |
|---------|---------|--------------|--------------|---------------|
| Website (WordPress) | ✅ | ✅ | ✅ | ✅ |
| Member Management (ChurchCRM) | ✅ | ✅ | ✅ | ✅ |
| Email Newsletters (Listmonk) | ✅ | ❌ | ✅ | ✅ |
| Password Sharing (Vaultwarden) | ✅ | ❌ | ❌ | ✅ |
| File Storage (Nextcloud) | ❌ | ❌ | ✅ | ✅ |
| Video Calls (Jitsi) | ❌ | ❌ | ❌ | ✅ |
| Document Editing (OnlyOffice) | ❌ | ❌ | ❌ | ✅ |
| Monitoring (Uptime Kuma) | ❌ | ❌ | ✅ | ✅ |
| Encrypted Backups (Duplicati) | ❌ | ❌ | ❌ | ✅ |

## Legacy Stack

The [docker-compose/](docker-compose/) directory contains a basic nginx-based deployment. The newer tiered stacks above use Traefik for simpler SSL management and are recommended for new deployments.
