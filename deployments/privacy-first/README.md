# Privacy-First Stack

> Fully self-hosted church technology stack for data sovereignty and privacy.

## Philosophy

This stack is for churches that:
- Believe member data belongs to the church, not third parties
- Want to avoid vendor lock-in and subscription fees
- Have (or can develop) technical expertise
- Value privacy and security

**What "Privacy-First" Means:**
- All data stored on your servers
- No third-party analytics or tracking
- Open source throughout
- Encrypted backups you control
- Self-hosted email capability

## What's Included

| Function | Tool | Purpose |
|----------|------|---------|
| **Website** | WordPress | Content, sermons, events |
| **ChMS** | ChurchCRM | Membership, giving, check-in |
| **Files/Collaboration** | Nextcloud | Documents, calendars, contacts |
| **Document Editing** | OnlyOffice | Collaborative document editing |
| **Email Lists** | Listmonk | Newsletters, announcements |
| **Email Server** | Mail-in-a-Box | Self-hosted email (separate VM) |
| **Video Conferencing** | Jitsi Meet | Online meetings, Bible studies |
| **Password Management** | Vaultwarden | Team password vault |
| **Monitoring** | Uptime Kuma | Service health monitoring |
| **Backups** | Duplicati | Encrypted, deduplicated backups |

## System Requirements

### Main Server
- **VPS/Dedicated:** 4GB RAM minimum, 8GB recommended
- **Storage:** 100GB minimum (more for file storage)
- **OS:** Ubuntu 22.04 LTS
- **Domain:** Main domain + multiple subdomains
- **IP:** Static IP address

### Email Server (Mail-in-a-Box)
- **Separate VPS:** 1GB RAM, 25GB storage
- **OS:** Ubuntu 22.04 LTS
- **Domain:** mail.yourdomain.com
- **IP:** Static IP with good reputation

## Quick Start

### Phase 1: Server Preparation

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Docker
curl -fsSL https://get.docker.com | sh
sudo usermod -aG docker $USER
newgrp docker

# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Set up firewall
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw allow 10000/udp  # Jitsi
sudo ufw --force enable
```

### Phase 2: DNS Configuration

Configure these DNS records pointing to your server IP:
- www.yourchurch.com (WordPress)
- crm.yourchurch.com (ChurchCRM)
- cloud.yourchurch.com (Nextcloud)
- office.yourchurch.com (OnlyOffice)
- news.yourchurch.com (Listmonk)
- meet.yourchurch.com (Jitsi)
- pass.yourchurch.com (Vaultwarden)
- status.yourchurch.com (Uptime Kuma)
- backup.yourchurch.com (Duplicati)

### Phase 3: Deploy

```bash
# Download and configure
curl -o docker-compose.yml https://raw.githubusercontent.com/church-tech-stack/main/stacks/privacy-first/docker-compose.yml
curl -o .env.example https://raw.githubusercontent.com/church-tech-stack/main/stacks/privacy-first/.env.example
cp .env.example .env

# Edit .env with your domains and secure passwords
nano .env

# Start services
docker-compose up -d
```

### Phase 4: Configure Each Service

1. **Nextcloud** - Enable Calendar, Contacts, Deck apps; connect OnlyOffice
2. **ChurchCRM** - Import members, set up groups, configure check-in
3. **Listmonk** - Configure SMTP, create mailing lists, import subscribers
4. **Jitsi** - Test video calls, create persistent rooms
5. **Vaultwarden** - Enable 2FA, create organization, invite users
6. **Duplicati** - Set up encrypted backups to S3/B2

## Security Best Practices

- Use strong, unique passwords for all services
- Enable 2FA on all admin accounts
- Configure fail2ban on the host
- Regular security updates
- Encrypted offsite backups
- Monitor Uptime Kuma alerts

## Support Resources

See individual service documentation for detailed help.

---

*Stack Version: 1.0 | Last Updated: 2026-02-03*
