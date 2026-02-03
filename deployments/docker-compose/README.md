# Privacy-First Stack Deployment

This Docker Compose setup runs ChurchCRM and Nextcloud on a single VPS.

## Prerequisites

- VPS with 4GB+ RAM, 2+ CPU cores, 80GB+ storage
- Ubuntu 22.04 LTS (or similar)
- Docker and Docker Compose installed
- Domain name pointed to VPS IP

## Quick Start

1. **Clone this repository:**
   ```bash
   git clone https://github.com/yourusername/church-tech-stack.git
   cd church-tech-stack/deployments/privacy-first
   ```

2. **Create environment file:**
   ```bash
   cp .env.example .env
   nano .env  # Edit passwords
   ```

3. **Start services:**
   ```bash
   docker-compose up -d
   ```

4. **Initialize SSL:**
   ```bash
   docker-compose run --rm certbot certonly --webroot -w /var/www/certbot -d your-domain.com
   ```

5. **Complete setup:**
   - ChurchCRM: http://your-domain.com:8080
   - Nextcloud: http://your-domain.com:8081
   - Follow first-run wizards

## Environment Variables

Create `.env` file:

```bash
MYSQL_ROOT_PASSWORD=your-secure-root-password
MYSQL_PASSWORD=your-secure-app-password
NEXTCLOUD_ADMIN_PASSWORD=your-admin-password
```

Use strong passwords (20+ characters).

## SSL/HTTPS

The stack includes automatic Let's Encrypt certificate renewal.

### Initial Setup

```bash
# Run certbot interactively
docker-compose run --rm certbot certonly --standalone -d your-domain.com -d www.your-domain.com

# Or use webroot challenge
docker-compose run --rm certbot certonly --webroot -w /var/www/certbot -d your-domain.com
```

### Renewal

Automatic via certbot container (checks every 12 hours).

## Backup Strategy

### Automated Daily Backup

Create `backup.sh`:

```bash
#!/bin/bash
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="/backups"

# Backup MySQL
docker exec church-mysql mysqldump -u root -p${MYSQL_ROOT_PASSWORD} --all-databases > $BACKUP_DIR/mysql_$DATE.sql

# Backup volumes
docker run --rm -v churchcrm-data:/data -v $BACKUP_DIR:/backup alpine tar czf /backup/churchcrm_$DATE.tar.gz -C /data .
docker run --rm -v nextcloud-data:/data -v $BACKUP_DIR:/backup alpine tar czf /backup/nextcloud_$DATE.tar.gz -C /data .

# Sync to S3 (optional)
aws s3 sync $BACKUP_DIR s3://your-backup-bucket/church-backups/

# Keep only last 7 days locally
find $BACKUP_DIR -name "*.tar.gz" -mtime +7 -delete
find $BACKUP_DIR -name "*.sql" -mtime +7 -delete
```

Add to crontab:
```
0 2 * * * /path/to/backup.sh >> /var/log/church-backup.log 2>&1
```

## Updates

### Update Containers

```bash
docker-compose pull
docker-compose up -d
```

### Update ChurchCRM

```bash
# Backup first
./backup.sh

# Pull latest
docker-compose pull churchcrm
docker-compose up -d churchcrm
```

## Troubleshooting

### Can't connect to database

```bash
# Check MySQL is running
docker-compose ps

# Check logs
docker-compose logs mysql

# Verify credentials
docker exec -it church-mysql mysql -u root -p
```

### SSL certificate issues

```bash
# Force renewal
docker-compose run --rm certbot renew --force-renewal

# Check certificate
docker-compose exec nginx openssl x509 -in /etc/letsencrypt/live/your-domain.com/cert.pem -text -noout
```

### Out of disk space

```bash
# Check usage
df -h
docker system df

# Clean up
docker system prune -a
docker volume prune
```

## Security Hardening

1. **Change default passwords** immediately after setup
2. **Enable 2FA** in ChurchCRM and Nextcloud
3. **Configure firewall:**
   ```bash
   ufw allow 22/tcp
   ufw allow 80/tcp
   ufw allow 443/tcp
   ufw enable
   ```
4. **Disable direct port access** (8080, 8081) in production
5. **Set up fail2ban** for SSH brute force protection

## Support

- ChurchCRM docs: https://github.com/ChurchCRM/CRM/wiki
- Nextcloud docs: https://docs.nextcloud.com/

---

*Deployment version: 1.0 | Last updated: 2026-01-31*
