# Volunteer Scheduling & Management

> Coordinating volunteers for services, events, and ministry teams.

## Why It Matters

Most churches run on volunteers. Coordinating dozens (or hundreds) of volunteers across multiple ministries, services, and events quickly becomes unmanageable with spreadsheets. Good volunteer scheduling software:

- Prevents gaps in coverage (no more last-minute panic)
- Respects volunteer availability and preferences
- Enables easy substitutions and swaps
- Sends reminders and notifications
- Tracks serving history and preferences

## The Landscape

There are two main approaches:

1. **Dedicated Volunteer Schedulers** — Purpose-built for recurring ministry schedules
2. **General Scheduling Tools** — Adapted for church use (Doodle-style polling)

---

## OpenVolunteerPlatform

**Status:** ⚠️ Maintenance Mode (last commit: 2022)

**Skill Level:** Advanced

**True Cost:**
- Software: Free
- Hosting: $10-30/mo VPS (requires 2GB+ RAM)
- Setup Time: 8-12 hours
- Ongoing Maintenance: 2-4 hours/month

**What It Does:**
Full-featured volunteer management platform originally built for crisis response (COVID-19). Includes role-based scheduling, real-time tracking via GraphQL subscriptions, automated reporting, and offline-capable mobile apps.

**Why Churches Use It:**
- Hierarchical organization structure (nations → regions → areas → cities)
- Complex shift scheduling with capacity limits
- Mobile apps with offline support
- Real-time updates when volunteers check in/out
- Built-in reporting and statistics

**Installation:**
- **Docker:** Available but complex (requires Keycloak, PostgreSQL, MQTT broker)
- **Self-hosted:** See [deployment guide](https://github.com/aerogear/OpenVolunteerPlatform/blob/master/docs)

**Architecture:**
- Backend: Node.js/GraphQL with Graphback
- Frontend: React with Offix (offline support)
- Auth: Keycloak (SSO)
- Real-time: MQTT broker for subscriptions

**Caveats:**
- Last significant update was 2022 — appears to be in maintenance mode
- Overkill for small churches (< 50 volunteers)
- Requires DevOps knowledge to deploy and maintain
- Mobile apps need custom build for your instance

**Links:**
- GitHub: https://github.com/aerogear/OpenVolunteerPlatform
- Docs: https://github.com/aerogear/OpenVolunteerPlatform/tree/master/docs

---

## Volunteer Planner (volunteer-planner.org)

**Status:** ✅ Active (last commit: 2024)

**Skill Level:** Intermediate

**True Cost:**
- Software: Free
- Hosting: $5-15/mo VPS
- Setup Time: 2-4 hours
- Ongoing Maintenance: 1-2 hours/month

**What It Does:**
Django-based volunteer scheduling platform originally built for refugee aid coordination in Europe. Proven in production since 2015. Supports complex organizational hierarchies and shift-based scheduling.

**Why Churches Use It:**
- Battle-tested in high-volume environments (refugee aid)
- Simple, clean interface for volunteers
- Location-based hierarchy supports multi-site churches
- Multi-language support (Transifex integration)
- Self-contained — single Python application

**Installation:**
```bash
# Using Docker (recommended)
git clone https://github.com/coders4help/volunteer_planner.git
cd volunteer_planner
docker-compose up -d

# Or manual setup
git clone https://github.com/coders4help/volunteer_planner.git
cd volunteer_planner
virtualenv .venv
source .venv/bin/activate
pip install -r requirements/dev.txt
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver
```

**Features for Churches:**
- Create organizations ("Children's Ministry", "Worship Team")
- Add facilities/rooms ("Nursery", "Main Sanctuary")
- Define shifts ("Sunday 9AM Service - Nursery")
- Volunteers self-register and claim shifts
- Automatic conflict detection
- Email notifications

**Caveats:**
- European-focused ( GDPR-compliant by default)
- UI is utilitarian, not polished
- Email configuration required for notifications
- No built-in check-in/check-out (scheduling only)

**Links:**
- GitHub: https://github.com/coders4help/volunteer_planner
- Demo: https://volunteer-planner.org
- Docs: https://github.com/coders4help/volunteer_planner/blob/develop/README_DOCKER.md

---

## Rallly

**Status:** ✅ Very Active (last commit: 2025)

**Skill Level:** Beginner to Intermediate

**True Cost:**
- Software: Free
- Hosting: $5-10/mo VPS (or free tier on Railway/Render)
- Setup Time: 30 minutes
- Ongoing Maintenance: Minimal

**What It Does:**
Modern, Doodle-style scheduling tool for finding the best time for group meetings. While not built specifically for recurring volunteer schedules, it excels at event-based coordination and one-time scheduling needs.

**Why Churches Use It:**
- Beautiful, modern interface
- No account required for participants
- Works perfectly for: training sessions, one-time events, committee meetings
- Self-hostable with Docker
- Mobile-responsive
- Automatic timezone handling

**Installation (Docker):**
```yaml
version: "3"
services:
  rallly:
    image: lukevella/rallly:latest
    ports:
      - "3000:3000"
    environment:
      - DATABASE_URL=postgres://postgres:postgres@db:5432/rallly
      - SECRET_KEY=your-secret-key-here
    depends_on:
      - db
  db:
    image: postgres:14
    environment:
      - POSTGRES_PASSWORD=postgres
      - POSTGRES_DB=rallly
    volumes:
      - postgres-data:/var/lib/postgresql/data

volumes:
  postgres-data:
```

**When to Use Rallly:**
- Scheduling training sessions
- Finding best time for volunteer meetings
- Coordinating one-time events
- Committee scheduling

**When NOT to Use Rallly:**
- Recurring weekly volunteer rotations (use Volunteer Planner or ChMS instead)
- Complex shift management with capacity limits
- Organizations with 100+ recurring positions

**Links:**
- GitHub: https://github.com/lukevella/rallly
- Demo: https://rallly.co
- Self-hosting docs: https://support.rallly.co/self-hosting

---

## ChurchApps (CHUMS/B1)

**Status:** ✅ Very Active (last commit: 2025)

**Skill Level:** Beginner

**True Cost:**
- Software: Free (open source)
- Hosting: Cloud (free tier available) or self-hosted
- Setup Time: 15 minutes (cloud) or 2-4 hours (self-hosted)
- Ongoing Maintenance: Minimal (cloud) or 1-2 hours/month (self-hosted)

**What It Does:**
Full church management system with integrated volunteer scheduling, check-in, group management, and giving. The volunteer module includes scheduling, team management, and service planning.

**Why Churches Use It:**
- All-in-one solution (no integration needed)
- Native mobile apps for iOS/Android
- Check-in integration (volunteers and children)
- Service planning with volunteer assignments
- Free cloud tier for small churches
- Active development and community

**Deployment Options:**
- **Cloud:** https://b1.church/ (free for small churches)
- **Self-hosted:** Docker images available

**Volunteer Features:**
- Create volunteer teams/groups
- Schedule volunteers for services
- Self-check-in via mobile app
- Swapping/declining shifts
- Automated reminders
- Integration with service planning

**Caveats:**
- Full ChMS — may be overkill if you only need volunteer scheduling
- Self-hosted version requires multiple containers (API, web app, database)
- Cloud version has feature limitations on free tier

**Links:**
- GitHub: https://github.com/ChurchApps/B1Admin
- Website: https://b1.church/
- Docs: https://churchapps.org/dev

---

## Comparison Matrix

| Feature | OpenVolunteerPlatform | Volunteer Planner | Rallly | ChurchApps |
|---------|----------------------|-------------------|--------|------------|
| **Recurring Schedules** | ✅ | ✅ | ❌ | ✅ |
| **Self-Serve Swap** | ✅ | ✅ | N/A | ✅ |
| **Mobile Apps** | ✅ (build required) | ❌ | ✅ (web) | ✅ (native) |
| **Check-in Integration** | ✅ | ❌ | ❌ | ✅ |
| **Skill Level** | Advanced | Intermediate | Beginner | Beginner |
| **Setup Time** | 8-12 hrs | 2-4 hrs | 30 min | 15 min (cloud) |
| **Maintenance** | High | Medium | Low | Low/Medium |

---

## Recommendation by Church Size

### Church Plant (< 50 people)
**Use:** Google Sheets/Calendar or Rallly
- Simple, free, no setup
- For recurring schedules: shared Google Sheet with volunteer preferences
- For events: Rallly cloud (free) or self-hosted

### Small Church (50-200)
**Use:** Volunteer Planner or ChurchApps Cloud
- Volunteer Planner: If you want self-hosted control
- ChurchApps Cloud: If you want all-in-one simplicity

### Mid-Size Church (200-1000)
**Use:** ChurchApps (self-hosted or cloud)
- Native mobile apps for volunteers
- Integrated with check-in and giving
- Service planning integration

### Large Church (1000+)
**Use:** Evaluate OpenVolunteerPlatform (if maintained) or commercial solutions
- May need custom development
- Consider integration with existing ChMS

---

## DIY QR Code Check-In for Volunteers

For churches wanting simple volunteer check-in without full scheduling:

### Simple PHP/MySQL Solution
```php
// Basic structure for volunteer check-in
// 1. Generate QR codes with volunteer IDs
// 2. Scan at check-in station
// 3. Log timestamp to database

// Requirements:
// - PHP 7.4+
// - MySQL/MariaDB
// - QR code library (endroid/qr-code)
// - Mobile device with camera for scanning (or cheap USB scanner)

// Estimated setup: 4-6 hours
// Hosting: $5/mo shared hosting
```

### Open-Source QR Libraries:
- **PHP:** `endroid/qr-code` (https://github.com/endroid/qr-code)
- **Python:** `qrcode` library + Flask/FastAPI
- **JavaScript:** `qrcodejs` (client-side generation)

---

## Integration Notes

### With ChurchCRM:
Use the Groups feature for volunteer teams, but it lacks scheduling. Export volunteer list to Volunteer Planner or use CalDAV integration for basic scheduling.

### With Nextcloud:
- Use **Calendar** for simple volunteer schedules
- Use **Polls** app for finding best times (Rallly alternative)
- Use **Forms** app for volunteer availability surveys

### With ChurchApps:
Native volunteer module included — no integration needed.

---

## Security Considerations

- **Volunteer data is personal data** — GDPR/CCPA compliance matters
- Use HTTPS for all volunteer-facing interfaces
- Implement rate limiting on login endpoints
- Regular backups of volunteer contact information
- Consider data retention policies (delete old records)

---

*Last Updated: 2026-02-03 | Maintained by: church-tech-stack maintainers*
