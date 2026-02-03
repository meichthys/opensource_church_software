# Starter Stack

> Get your church online with member management, a website, newsletters, and secure password sharing — in about an hour.

## What You Get

| Tool | What It Does | Replaces |
|------|--------------|----------|
| **WordPress** | Church website with sermons, events, contact forms | Wix, Squarespace |
| **ChurchCRM** | Track members, groups, attendance, giving | Planning Center, Breeze |
| **Listmonk** | Send email newsletters to your congregation | Mailchimp |
| **Vaultwarden** | Share passwords securely with staff | LastPass, shared spreadsheets |

**Total cost:** $5-10/month for a small VPS (DigitalOcean, Linode, Vultr)

## What You Need

- A domain name (e.g., yourchurch.com)
- A VPS with 2GB RAM ($10-12/month) running Ubuntu 22.04
- About 1 hour for initial setup
- Basic comfort with command line (copy/paste is fine)

## Setup Guide

### Step 1: Get a Server

Sign up for a VPS at [DigitalOcean](https://digitalocean.com), [Linode](https://linode.com), or [Vultr](https://vultr.com).

- Choose **Ubuntu 22.04 LTS**
- Choose **2GB RAM** ($10-12/month)
- Choose a location near your congregation

Save the IP address they give you.

### Step 2: Point Your Domain

Log into your domain registrar and create these DNS records pointing to your server IP:

```
www.yourchurch.com      → A Record → YOUR_SERVER_IP
members.yourchurch.com  → A Record → YOUR_SERVER_IP
news.yourchurch.com     → A Record → YOUR_SERVER_IP
vault.yourchurch.com    → A Record → YOUR_SERVER_IP
```

Wait 5-10 minutes for DNS to propagate.

### Step 3: Connect to Your Server

On Mac/Linux, open Terminal. On Windows, use PowerShell.

```bash
ssh root@YOUR_SERVER_IP
```

Type "yes" when asked about fingerprints, then enter your password.

### Step 4: Install Docker

Copy and paste these commands one at a time:

```bash
# Update the system
apt update && apt upgrade -y

# Install Docker
curl -fsSL https://get.docker.com | sh

# Install Docker Compose plugin
apt install docker-compose-plugin -y
```

### Step 5: Download the Stack

```bash
# Create a folder for your church stack
mkdir -p /opt/church && cd /opt/church

# Download the configuration files
curl -O https://raw.githubusercontent.com/church-tech-stack/main/stacks/starter/docker-compose.yml
curl -O https://raw.githubusercontent.com/church-tech-stack/main/stacks/starter/.env.example

# Create your configuration file
cp .env.example .env
```

### Step 6: Configure Your Settings

```bash
nano .env
```

Update these values:
- Replace `yourchurch.com` with your actual domain
- Replace `CHANGE_ME_X` passwords with strong passwords

To generate strong passwords, open a new terminal and run:
```bash
openssl rand -base64 24
```

Save the file: Press `Ctrl+X`, then `Y`, then `Enter`.

### Step 7: Start Everything

```bash
docker compose up -d
```

Wait 2-3 minutes for everything to start. Check status with:
```bash
docker compose ps
```

All services should show "running".

### Step 8: Complete Setup for Each Service

**WordPress** (https://www.yourchurch.com)
1. Follow the setup wizard
2. Pick a theme (search "flavor starter theme" for good ones)
3. Recommended plugins: Jewtify (sermons) and The Events Calendar

**ChurchCRM** (https://members.yourchurch.com)
1. Create your admin account
2. Add your church info in Settings
3. Start adding members manually or import from CSV

**Listmonk** (https://news.yourchurch.com)
1. Log in with credentials from your .env file
2. Go to Settings → Settings → SMTP to configure email sending
3. Create your first mailing list (e.g., "Weekly Newsletter")

**Vaultwarden** (https://vault.yourchurch.com)
1. Go to https://vault.yourchurch.com/admin
2. Enter your admin token from .env
3. Invite staff members via email
4. Have everyone install the Bitwarden app (it works with Vaultwarden)

## Day-to-Day Use

### Sending Newsletters

1. Log into Listmonk
2. Click Campaigns → New
3. Write your newsletter
4. Select your list and send

### Adding New Members

1. Log into ChurchCRM
2. Click People → Add New Family
3. Fill in details

### Updating Your Website

1. Log into WordPress
2. Edit pages, add sermons, update events

### Sharing Passwords with Staff

1. Open Bitwarden app (or browser extension)
2. Create an Organization for your church
3. Add shared items (WiFi password, social media logins, etc.)
4. Invite staff to the organization

## Backups

**Critical:** Set up backups or you will lose everything if your server fails.

Create a backup script:

```bash
nano /opt/church/backup.sh
```

Paste this:

```bash
#!/bin/bash
DATE=$(date +%Y%m%d)
BACKUP_DIR="/opt/church/backups"
mkdir -p $BACKUP_DIR

# Backup all data
docker run --rm \
  -v starter_wordpress-data:/source/wordpress:ro \
  -v starter_churchcrm-data:/source/churchcrm:ro \
  -v starter_vaultwarden-data:/source/vaultwarden:ro \
  -v starter_listmonk-data:/source/listmonk:ro \
  -v $BACKUP_DIR:/backup \
  alpine tar czf /backup/church-backup-$DATE.tar.gz -C /source .

# Backup databases
docker exec starter-wordpress-db mysqldump -u wordpress -p${WORDPRESS_DB_PASSWORD} wordpress > $BACKUP_DIR/wordpress-$DATE.sql
docker exec starter-churchcrm-db mysqldump -u churchcrm -p${CHURCHCRM_DB_PASSWORD} churchcrm > $BACKUP_DIR/churchcrm-$DATE.sql
docker exec starter-listmonk-db pg_dump -U listmonk listmonk > $BACKUP_DIR/listmonk-$DATE.sql

# Keep only last 7 days
find $BACKUP_DIR -name "*.tar.gz" -mtime +7 -delete
find $BACKUP_DIR -name "*.sql" -mtime +7 -delete

echo "Backup complete: $DATE"
```

Make it run automatically:

```bash
chmod +x /opt/church/backup.sh

# Run daily at 2 AM
(crontab -l 2>/dev/null; echo "0 2 * * * /opt/church/backup.sh") | crontab -
```

**Important:** Copy backups offsite! Use `scp` to copy to another computer or set up automatic sync to Backblaze B2 ($5/month for plenty of storage).

## Updates

Update your services monthly:

```bash
cd /opt/church
docker compose pull
docker compose up -d
```

Update WordPress plugins through the WordPress admin panel.

## Troubleshooting

### "Site can't be reached"

```bash
# Check if services are running
docker compose ps

# Check logs for errors
docker compose logs wordpress
docker compose logs traefik
```

### "SSL certificate error"

Wait 5 minutes — certificates take time to generate. If still failing:

```bash
# Check Traefik logs
docker compose logs traefik

# Verify DNS is pointing to your server
dig +short www.yourchurch.com
```

### "Forgot my password"

For WordPress, Listmonk, or ChurchCRM — use their built-in password reset via email.

For Vaultwarden admin token — it's in your .env file.

## Getting Help

- WordPress: https://wordpress.org/support/
- ChurchCRM: https://github.com/ChurchCRM/CRM/wiki
- Listmonk: https://listmonk.app/docs/
- Vaultwarden: https://github.com/dani-garcia/vaultwarden/wiki

## Next Steps

When you outgrow this stack:

- **Need file sharing?** → Graduate to Small Church Stack (adds Nextcloud)
- **Need video calls?** → Graduate to Privacy-First Stack (adds Jitsi)
- **Need monitoring?** → Add Uptime Kuma to get alerts when things go down

---

*Keep it simple. Serve your people.*
