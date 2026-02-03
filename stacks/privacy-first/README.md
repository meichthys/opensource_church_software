# Privacy-First Stack

> Complete data ownership for security-conscious churches.

## The Philosophy

Your church data belongs to your church:
- **Member data** shouldn't be mined by third parties
- **Giving records** are sensitive financial information
- **Sermon content** shouldn't be subject to platform policies
- **Communication** should be private

This stack prioritizes **control** over **convenience**.

## The Stack

| Function | Tool | Hosting |
|----------|------|---------|
| **ChMS** | ChurchCRM | Self-hosted VPS |
| **Files** | Nextcloud | Self-hosted VPS |
| **Email** | Mail-in-a-Box | Self-hosted VPS |
| **Presentation** | OpenLP | Local PC |
| **Sermons** | ChurchCRM media module | Self-hosted VPS |
| **Communication** | Mattermost | Self-hosted VPS |

**Total monthly cost:** $5-20 (VPS)  
**Setup time:** 1-2 weeks  
**Technical skill:** Linux administration

---

## Requirements

### Technical
- Comfortable with SSH and command line
- Basic understanding of DNS
- Time to maintain and update systems

### Financial
- VPS: $5-20/month (Hetzner, DigitalOcean, Linode)
- Domain: $12/year
- Backup storage: $2-5/month

### Time
- Initial setup: 20-40 hours
- Monthly maintenance: 2-4 hours

---

## Infrastructure

### Recommended VPS Specs
- 2 CPU cores
- 4GB RAM minimum (8GB preferred)
- 80GB SSD storage
- Ubuntu 22.04 LTS

### Backup Strategy
- Daily automated backups to S3-compatible storage
- Test restores quarterly
- Offsite copy on church treasurer's home NAS

---

## Deployment

See the `deployments/` directory for:
- `docker-compose/` — All services in containers
- `ansible/` — Automated server setup
- `terraform/` — Infrastructure as code

---

## Security Checklist

- [ ] Fail2ban configured on all servers
- [ ] Automatic security updates enabled
- [ ] SSL certificates (Let's Encrypt)
- [ ] Firewall: Only necessary ports open
- [ ] Database not exposed to internet
- [ ] Admin passwords: 20+ characters, unique
- [ ] 2FA enabled where supported
- [ ] Backup encryption
- [ ] Quarterly security audits

---

## When This Makes Sense

✅ **DO:**
- You have a technical volunteer or staff member
- Your church values data privacy highly
- You're in a region with data sovereignty concerns
- You want to avoid vendor lock-in

❌ **DON'T:**
- Your tech person is about to leave
- You can't commit to regular maintenance
- You need 99.99% uptime without budget for redundancy
- Compliance requirements exceed your expertise

---

*Last updated: 2026-01-31*
