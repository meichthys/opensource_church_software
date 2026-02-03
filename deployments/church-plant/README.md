# Church Plant Stack

> Zero-budget, minimal setup for new churches. One domain, one weekend.

## What's Included

| Function | Tool | Why |
|----------|------|-----|
| **Website** | WordPress | Familiar, plugin ecosystem, easy themes |
| **ChMS** | ChurchCRM | Member tracking, groups, basic check-in |
| **Database** | Adminer | Easy database management without command line |
| **Proxy/SSL** | Traefik | Automatic HTTPS, simple routing |

## System Requirements

- **Server:** VPS with 1GB RAM (2GB recommended), 20GB storage
- **OS:** Ubuntu 22.04 LTS or Debian 12
- **Domain:** One domain with DNS access
- **Skills:** Basic Linux command line, Docker familiarity helpful

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
mkdir -p ~/church-plant && cd ~/church-plant
```

### 2. Download Stack Files

```bash
# Download docker-compose.yml
curl -o docker-compose.yml https://raw.githubusercontent.com/church-tech-stack/main/stacks/church-plant/docker-compose.yml

# Download environment template
curl -o .env.example https://raw.githubusercontent.com/church-tech-stack/main/stacks/church-plant/.env.example
cp .env.example .env
```

### 3. Configure Environment

Edit `.env`:

```bash
# Your domain names (must point to server IP)
WORDPRESS_DOMAIN=www.yourchurch.com
CHURCHCRM_DOMAIN=crm.yourchurch.com
ADMINER_DOMAIN=db.yourchurch.com

# Let's Encrypt email (for SSL certificates)
ACME_EMAIL=you@yourchurch.com

# Database passwords - CHANGE THESE!
WORDPRESS_DB_PASSWORD=your_secure_password_1
CHURCHCRM_DB_PASSWORD=your_secure_password_2
MYSQL_ROOT_PASSWORD=your_secure_root_password
MYSQL_ROOT_PASSWORD_2=your_secure_root_password_2

# Adminer login (user: admin, password: changeme)
# Generate with: htpasswd -nb admin yourpassword | sed -e s/\$/\$\$/g
ADMINER_AUTH=admin:$$apr1$$H6uskkkW$$IgXLP6ewTrSuBkTrqE8wj/
```

### 4. Start the Stack

```bash
docker-compose up -d
```

### 5. Complete Setup

**WordPress:**
1. Visit `https://www.yourchurch.com`
2. Complete WordPress setup wizard
3. Install a church theme (recommend: "Church" or "Faith")
4. Essential plugins: 
   - "Sermon Manager" for sermons
   - "The Events Calendar" for events
   - "WP Mail SMTP" for email

**ChurchCRM:**
1. Visit `https://crm.yourchurch.com`
2. Create admin account
3. Complete initial setup wizard
4. Configure email settings (use WP Mail SMTP credentials)
5. Import members or add manually

## Maintenance

### Backup

Create `backup.sh`:

```bash
#!/bin/bash
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="$HOME/backups"
mkdir -p $BACKUP_DIR

# Backup WordPress files
docker run --rm -v church-plant_wordpress-data:/data -v $BACKUP_DIR:/backup alpine tar czf /backup/wordpress_$DATE.tar.gz -C /data .

# Backup ChurchCRM files
docker run --rm -v church-plant_churchcrm-data:/data -v $BACKUP_DIR:/backup alpine tar czf /backup/churchcrm_$DATE.tar.gz -C /data .

# Backup databases
docker exec church-plant-wordpress-db mysqldump -u root -p${MYSQL_ROOT_PASSWORD} wordpress > $BACKUP_DIR/wordpress_db_$DATE.sql
docker exec church-plant-churchcrm-db mysqldump -u root -p${MYSQL_ROOT_PASSWORD_2} churchcrm > $BACKUP_DIR/churchcrm_db_$DATE.sql

# Keep only last 7 days
find $BACKUP_DIR -name "*.tar.gz" -mtime +7 -delete
find $BACKUP_DIR -name "*.sql" -mtime +7 -delete

echo "Backup completed: $DATE"
```

Add to crontab:
```bash
0 2 * * * /home/youruser/church-plant/backup.sh >> /var/log/church-backup.log 2>&1
```

### Updates

```bash
# Update containers
docker-compose pull
docker-compose up -d

# Update WordPress plugins (via admin panel)
# Update ChurchCRM (via built-in updater)
```

## Troubleshooting

### Can't access sites
```bash
# Check containers are running
docker-compose ps

# Check logs
docker-compose logs traefik
docker-compose logs wordpress

# Verify DNS
dig +short www.yourchurch.com
```

### SSL certificate issues
```bash
# View Traefik logs
docker-compose logs traefik

# Force renewal (delete acme.json and restart)
docker-compose down
rm letsencrypt/acme.json
docker-compose up -d
```

### Database connection errors
```bash
# Verify databases are healthy
docker-compose ps

# Check database logs
docker-compose logs wordpress-db
docker-compose logs churchcrm-db
```

## Security Notes

1. **Change default passwords immediately**
2. **Enable WordPress security plugin** (Wordfence or similar)
3. **Keep backups offsite** (rsync to another server or S3)
4. **Configure firewall:**
   ```bash
   sudo ufw allow 22/tcp
   sudo ufw allow 80/tcp
   sudo ufw allow 443/tcp
   sudo ufw enable
   ```
5. **Enable automatic security updates:**
   ```bash
   sudo apt install unattended-upgrades
   sudo dpkg-reconfigure unattended-upgrades
   ```

## Migration Path

When ready to upgrade to Small Church Stack:

1. Export data from WordPress (Tools → Export)
2. Export ChurchCRM database
3. Deploy Small Church Stack on larger server
4. Import data
5. Redirect domains

## Support

- WordPress docs: https://wordpress.org/support/
- ChurchCRM docs: https://github.com/ChurchCRM/CRM/wiki
- Traefik docs: https://doc.traefik.io/traefik/

---

*Stack Version: 1.0 | Last Updated: 2026-02-03*
