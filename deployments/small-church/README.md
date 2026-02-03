# Small Church Stack

> Balanced setup for established churches with 50-200 members.

## What's Included

| Function | Tool | Purpose |
|----------|------|---------|
| **Website** | WordPress | Sermons, events, announcements |
| **ChMS** | ChurchCRM | Members, groups, check-in, giving tracking |
| **Files** | Nextcloud | Document storage, collaboration, calendars |
| **Email** | Listmonk | Newsletters, announcements, automated emails |
| **Monitoring** | Uptime Kuma | Service health monitoring |
| **Updates** | Watchtower | Automatic container updates |

## System Requirements

- **Server:** VPS with 2GB RAM (4GB recommended), 50GB storage
- **OS:** Ubuntu 22.04 LTS or Debian 12
- **Domain:** One domain with wildcard or multiple subdomains
- **Skills:** Basic Linux, Docker familiarity, DNS management

## Quick Start

### 1. Prepare Your Server

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

# Create directory
mkdir -p ~/small-church && cd ~/small-church
```

### 2. Configure DNS

Point these subdomains to your server IP:

```
www.yourchurch.com     → A Record → your-server-ip
crm.yourchurch.com     → A Record → your-server-ip
files.yourchurch.com   → A Record → your-server-ip
news.yourchurch.com    → A Record → your-server-ip
status.yourchurch.com  → A Record → your-server-ip
```

### 3. Download and Configure

```bash
# Download files
curl -o docker-compose.yml https://raw.githubusercontent.com/church-tech-stack/main/stacks/small-church/docker-compose.yml
curl -o .env.example https://raw.githubusercontent.com/church-tech-stack/main/stacks/small-church/.env.example
cp .env.example .env

# Edit configuration
nano .env
```

### 4. Start the Stack

```bash
docker-compose up -d
```

Wait 2-3 minutes for all services to initialize.

### 5. Complete Setup

**WordPress:**
- Visit `https://www.yourchurch.com`
- Complete setup wizard
- Install recommended plugins:
  - Sermon Manager
  - The Events Calendar
  - WP Mail SMTP
  - Wordfence Security

**ChurchCRM:**
- Visit `https://crm.yourchurch.com`
- Create admin account
- Configure email settings
- Set up groups and Sunday School classes
- Configure check-in for children's ministry

**Nextcloud:**
- Visit `https://files.yourchurch.com`
- Admin account already created from environment variables
- Install recommended apps:
  - Calendar (share church calendars)
  - Contacts (shared address book)
  - Deck (project management)
  - Forms (surveys, sign-ups)
  - Polls (schedule voting)
- Configure external storage if needed

**Listmonk:**
- Visit `https://news.yourchurch.com`
- Login with credentials from .env
- Configure SMTP settings (Settings → Settings → SMTP)
- Create subscriber lists:
  - All Church
  - Staff
  - Volunteers
  - Parents
- Import subscribers or add signup form to website
- Create templates for newsletters

**Uptime Kuma:**
- Visit `https://status.yourchurch.com`
- Create admin account
- Add monitors for:
  - https://www.yourchurch.com
  - https://crm.yourchurch.com
  - https://files.yourchurch.com
  - https://news.yourchurch.com
- Configure notifications (email, Discord, etc.)

## Maintenance

### Backup Strategy

Create `backup.sh`:

```bash
#!/bin/bash
set -e

DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="$HOME/backups"
mkdir -p $BACKUP_DIR

echo "Starting backup at $DATE..."

# WordPress
docker run --rm -v small-church_wordpress-data:/data -v $BACKUP_DIR:/backup alpine \
  tar czf /backup/wordpress_$DATE.tar.gz -C /data .
docker exec small-church-wordpress-db mysqldump -u root -p${MYSQL_ROOT_PASSWORD} wordpress > \
  $BACKUP_DIR/wordpress_db_$DATE.sql

# ChurchCRM
docker run --rm -v small-church_churchcrm-data:/data -v $BACKUP_DIR:/backup alpine \
  tar czf /backup/churchcrm_$DATE.tar.gz -C /data .
docker exec small-church-churchcrm-db mysqldump -u root -p${MYSQL_ROOT_PASSWORD_2} churchcrm > \
  $BACKUP_DIR/churchcrm_db_$DATE.sql

# Nextcloud
docker run --rm -v small-church_nextcloud-data:/data -v $BACKUP_DIR:/backup alpine \
  tar czf /backup/nextcloud_$DATE.tar.gz -C /data .
docker exec small-church-nextcloud-db mysqldump -u root -p${MYSQL_ROOT_PASSWORD_3} nextcloud > \
  $BACKUP_DIR/nextcloud_db_$DATE.sql

# Listmonk
docker run --rm -v small-church_listmonk-data:/data -v $BACKUP_DIR:/backup alpine \
  tar czf /backup/listmonk_$DATE.tar.gz -C /data .
docker exec small-church-listmonk-db pg_dump -U listmonk listmonk > \
  $BACKUP_DIR/listmonk_db_$DATE.sql

# Cleanup old backups (keep 14 days)
find $BACKUP_DIR -name "*.tar.gz" -mtime +14 -delete
find $BACKUP_DIR -name "*.sql" -mtime +14 -delete

echo "Backup completed: $(date)"
```

Make executable and schedule:
```bash
chmod +x backup.sh
# Add to crontab - runs daily at 2 AM
(crontab -l 2>/dev/null; echo "0 2 * * * /home/youruser/small-church/backup.sh >> /var/log/church-backup.log 2>&1") | crontab -
```

### Restore from Backup

```bash
# Restore WordPress files
docker run --rm -v small-church_wordpress-data:/data -v $BACKUP_DIR:/backup alpine \
  sh -c "cd /data && tar xzf /backup/wordpress_YYYYMMDD_HHMMSS.tar.gz"

# Restore WordPress database
docker exec -i small-church-wordpress-db mysql -u root -p${MYSQL_ROOT_PASSWORD} wordpress < \
  wordpress_db_YYYYMMDD_HHMMSS.sql
```

### Updates

> **WARNING: Watchtower Risks**
>
> Watchtower automatically updates containers, which can break things without warning. Mitigations:
> 1. **Monitor notifications** — Watchtower emails you when updates occur
> 2. **Test backups monthly** — Ensure you can restore if an update breaks something
> 3. **Consider pinning critical images** — Change `image: wordpress:latest` to `image: wordpress:6.4` for stability
> 4. **No rollback built-in** — If an update breaks things, you must restore from backup or manually pull old image
>
> For production stability, consider disabling Watchtower and doing manual updates during maintenance windows.

Watchtower handles automatic container updates. For application updates:

**WordPress:** Use admin panel → Updates
**ChurchCRM:** Built-in updater
**Nextcloud:** Admin panel → Overview → Update
**Listmonk:** Update container image version in docker-compose.yml

### Monitoring

Check Uptime Kuma dashboard regularly. Common issues:

- **High CPU/Memory:** Check `docker stats`
- **Slow Nextcloud:** Redis helps; consider enabling PHP OPcache
- **Database errors:** Check individual service logs

## Integration Guide

### ChurchCRM ↔ WordPress

1. Export members from ChurchCRM
2. Use WP All Import plugin to create WordPress users
3. Sync giving data manually or via custom script

### Nextcloud ↔ ChurchCRM

1. Export contacts from ChurchCRM
2. Import to Nextcloud Contacts app
3. Share church calendars publicly or with specific groups

### Listmonk ↔ WordPress

1. Add subscription form to WordPress footer/sidebar
2. Use Listmonk subscription API
3. Example integration plugin available

### Listmonk ↔ ChurchCRM

1. Export email list from ChurchCRM
2. Import to Listmonk
3. Set up regular sync via CSV export/import

## Troubleshooting

### Services won't start
```bash
# Check logs
docker-compose logs [service-name]

# Check disk space
df -h

# Check memory
free -h
```

### SSL certificate issues
```bash
# Force renewal
docker-compose down
rm -f letsencrypt/acme.json
docker-compose up -d
```

### Database connection errors
```bash
# Verify databases are healthy
docker-compose ps

# Check specific database logs
docker-compose logs [db-name]
```

### Nextcloud performance issues
```bash
# Enable Redis in Nextcloud config
docker exec -it small-church-nextcloud \
  su -s /bin/sh www-data -c "php occ config:system:set memcache.local --value='\\OC\\Memcache\\Redis'"
docker exec -it small-church-nextcloud \
  su -s /bin/sh www-data -c "php occ config:system:set memcache.locking --value='\\OC\\Memcache\\Redis'"
docker exec -it small-church-nextcloud \
  su -s /bin/sh www-data -c "php occ config:system:set redis host --value=nextcloud-redis"
```

## Security Best Practices

1. **Keep .env secure:** Never commit to git
2. **Regular backups:** Daily automated, test restore monthly
3. **Firewall:**
   ```bash
   sudo ufw allow 22/tcp
   sudo ufw allow 80/tcp
   sudo ufw allow 443/tcp
   sudo ufw enable
   ```
4. **Fail2ban:** Install and configure for SSH protection
5. **Updates:** Enable automatic security updates
6. **Monitoring:** Check Uptime Kuma regularly
7. **Nextcloud security:** Enable 2FA for all admin accounts

## Scaling Considerations

When approaching 200+ members:

1. **Upgrade VPS:** 4GB RAM → 8GB RAM
2. **Separate databases:** Consider dedicated database server
3. **CDN:** Add Cloudflare for WordPress/Nextcloud
4. **Object storage:** Move Nextcloud files to S3-compatible storage
5. **Monitoring:** Add more detailed logging and alerting

## Migration from Church Plant Stack

1. Set up Small Church Stack on new server
2. Export WordPress content (Tools → Export)
3. Export ChurchCRM database
4. Import to new stack
5. Set up additional services
6. Test thoroughly
7. Update DNS
8. Decommission old server

## Support Resources

- WordPress: https://wordpress.org/support/
- ChurchCRM: https://github.com/ChurchCRM/CRM/wiki
- Nextcloud: https://docs.nextcloud.com/
- Listmonk: https://listmonk.app/docs/
- Uptime Kuma: https://github.com/louislam/uptime-kuma

---

*Stack Version: 1.0 | Last Updated: 2026-02-03*
