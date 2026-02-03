# Children's Check-In / Check-Out

> Secure, efficient systems for children's ministry safety and parent peace of mind.

## Why It Matters

Child safety is non-negotiable in churches. A proper check-in system:

- Ensures only authorized adults pick up children
- Provides allergy and medical alerts to workers
- Maintains accurate attendance records
- Enables emergency contact access
- Gives parents confidence in your safety procedures

## Key Requirements

1. **Security First:** Unique guardian-pickup codes, photo verification
2. **Speed:** Check-in must be < 30 seconds per family
3. **Reliability:** Works without internet (or has offline mode)
4. **Accessibility:** Easy for first-time guests
5. **Integration:** Works with your ChMS

---

## ChurchApps Check-In

**Status:** ✅ Very Active (last commit: 2025)

**Skill Level:** Beginner

**True Cost:**
- Software: Free (open source)
- Hosting: Cloud (free tier) or self-hosted
- Hardware: Tablets/phones for check-in stations ($50-200 each)
- Setup Time: 30 minutes (cloud) or 2-4 hours (self-hosted)
- Ongoing Maintenance: Minimal

**What It Does:**
Purpose-built check-in system integrated with ChurchApps ChMS. Supports QR codes, phone number lookup, and name search. Prints labels with security codes, allergy alerts, and pickup permissions.

**Why Churches Use It:**
- Purpose-built for church child check-in
- Multiple check-in methods (QR, phone, name search)
- Prints security labels with unique codes
- Allergy and special needs alerts on labels
- Real-time room capacity monitoring
- Parent mobile app for pre-check-in
- Works offline with sync

**Check-In Methods:**
1. **QR Code:** Returning families scan QR code on their phone
2. **Phone Number:** Quick lookup for regular families
3. **Name Search:** For guests or when QR won't scan
4. **Pre-check:** Parents check in via mobile app before arriving

**Label Information:**
- Child's name and age/grade
- Security code (matches parent pickup tag)
- Allergy alerts (prominent visual indicator)
- Special needs notes
- Parent/guardian contact

**Installation:**
- **Cloud:** Sign up at https://b1.church/ → Enable Check-in module
- **Self-hosted:** Docker compose with ChurchApps stack

**Hardware Requirements:**
- Check-in stations: Tablets, phones, or computers with camera
- Label printers: Brother QL-series recommended (USB or network)
- Network: WiFi coverage in check-in area

**Security Features:**
- Unique security codes every week
- Photo verification option
- Authorized pickup list enforcement
- Digital audit trail (who checked in/out, when)
- Room capacity limits with alerts

**Caveats:**
- Requires ChurchApps account (either cloud or self-hosted)
- Label printer setup can be tricky on some devices
- Best experience requires modern tablets/phones
- Self-hosted version needs API server + web app

**Links:**
- GitHub: https://github.com/ChurchApps/B1Admin
- Website: https://b1.church/
- Mobile App: "B1 Church" on iOS/Android

---

## ChurchCRM + Custom Check-In

**Status:** ✅ Active (last commit: 2025)

**Skill Level:** Intermediate to Advanced

**True Cost:**
- Software: Free
- Hosting: $5-10/mo VPS
- Development: 4-8 hours for basic QR check-in
- Setup Time: 2-4 hours (ChurchCRM) + custom dev
- Ongoing Maintenance: Low

**What It Does:**
ChurchCRM includes basic group/event check-in. For dedicated children's check-in, you'll need to build or extend the existing Sunday School check-in features.

**Built-in Check-In:**
ChurchCRM has `Checkin.php` for Sunday School classes:
- Child check-in by name
- Parent/guardian assignment
- Classroom assignment
- Basic attendance tracking

**Extending for QR Codes:**
```php
// Basic approach to add QR check-in to ChurchCRM:
// 1. Generate QR codes with family ID encoded
// 2. Create check-in endpoint that:
//    - Reads QR code → looks up family
//    - Shows children in family
//    - Records check-in to database
//    - Prints label (if printer configured)
// 3. Create check-out endpoint for secure pickup

// Estimated development: 4-8 hours for basic version
// PHP knowledge required
```

**DIY QR Check-In Architecture:**
```
[QR Code] → [Scanner/Camera] → [Web App] → [ChurchCRM Database]
                                        ↓
                                  [Label Printer]
```

**Why Churches Use It:**
- Free and fully self-hosted
- Data stays in your ChMS
- Customizable to your exact needs
- No per-check-in fees

**Caveats:**
- Requires PHP development skills to extend
- No native mobile app
- Label printing requires additional setup
- No offline mode (requires internet)

**Links:**
- GitHub: https://github.com/ChurchCRM/CRM
- Docs: https://github.com/ChurchCRM/CRM/wiki
- Check-in code: https://github.com/ChurchCRM/CRM/blob/master/src/Checkin.php

---

## Jethro Pastoral Ministry Manager

**Status:** ✅ Active (last commit: 2024)

**Skill Level:** Intermediate

**True Cost:**
- Software: Free
- Hosting: $5-10/mo VPS
- Setup Time: 2-3 hours
- Ongoing Maintenance: Low

**What It Does:**
Australian-developed church management system with attendance tracking, rosters, and basic check-in capabilities. Less feature-rich than dedicated check-in systems but functional for smaller churches.

**Attendance Features:**
- Sunday School attendance tracking
- Roster management for children's ministries
- Contact management for families
- Basic check-in recording

**Why Churches Use It:**
- Simple, no-frills approach
- Good for small churches already using Jethro
- Australian support timezone
- Less complex than ChurchCRM

**Caveats:**
- No QR code support (manual entry)
- No label printing
- Primarily designed for Australian churches
- Smaller community than ChurchCRM

**Links:**
- GitHub: https://github.com/tbar0970/jethro-pmm
- Website: https://jethro-pmm.sourceforge.net/

---

## DIY Self-Hosted Check-In System

**Status:** Community Recipe

**Skill Level:** Intermediate to Advanced

**True Cost:**
- Software: Free
- Hosting: $5-10/mo VPS or local Raspberry Pi
- Hardware: ~$100-300 per check-in station
- Setup Time: 8-16 hours development + 2-4 hours deployment
- Ongoing Maintenance: Low

**Architecture Overview:**

```
┌─────────────────────────────────────────────────────────────┐
│                    CHECK-IN STATION                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │  Tablet/PC   │  │ USB Camera   │  │ Label Printer│      │
│  │  (Browser)   │  │ (for QR)     │  │ (Brother QL) │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                  CHECK-IN SERVER                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │   Web App    │  │   Database   │  │  QR Service  │      │
│  │  (PHP/Node)  │  │  (SQLite/   │  │  (Generator  │      │
│  │              │  │   MariaDB)   │  │   & Scanner) │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└─────────────────────────────────────────────────────────────┘
```

**Technology Stack Options:**

### Option A: PHP + MySQL (Beginner-Friendly)
```php
// Core components:
// - qr_code table: id, family_id, hash, created_at
// - checkin_log table: child_id, checked_in_at, checked_out_at, guardian_id
// - children table: name, family_id, allergies, special_needs
// - guardians table: name, phone, photo, authorized_pickup (boolean)

// Libraries:
// - chillerlan/php-qrcode (QR generation)
// - endroid/qr-code (alternative)
// - jquery (frontend)
// - Bootstrap (UI)
```

### Option B: Node.js + SQLite (Lightweight)
```javascript
// Core components:
// - Express.js web server
// - Better-sqlite3 database
// - qrcode library
// - jsQR (QR scanning in browser)
// - Pug/EJS templates

// Benefits:
// - Single-file database (easy backup)
// - Fast setup
// - Good for single-check-in-station deployments
```

### Option C: Python + Flask (Rapid Development)
```python
# Core components:
# - Flask web framework
# - SQLAlchemy ORM
# - qrcode library
# - pyzbar (QR decoding)
# - Jinja2 templates

# Benefits:
# - Very readable code
# - Easy to extend
# - Good for custom integrations
```

**Hardware Shopping List (Per Station):**
- Tablet or cheap laptop: $50-150 (Amazon Fire tablet, used iPad, Chromebook)
- USB webcam (if device lacks camera): $15-30
- Brother QL-800 label printer: $80-120
- Labels (continuous roll DK-2205): $15/roll
- Optional: Tablet stand/enclosure: $20-40

**Security Best Practices:**
1. **Unique Security Codes:** Generate random 4-6 digit codes each week
2. **Code Expiration:** Codes expire after service ends
3. **Photo Verification:** Optional photo display on guardian record
4. **Authorized Pickup List:** Enforce strictly — no exceptions
5. **Audit Logging:** Log every check-in/out with timestamp and user
6. **Data Encryption:** Encrypt sensitive child data at rest
7. **Network Security:** HTTPS only, local network preferred
8. **Physical Security:** Secure check-in stations, controlled access to printers

**Sample Database Schema:**
```sql
-- Families
CREATE TABLE families (
    id INTEGER PRIMARY KEY,
    family_name TEXT NOT NULL,
    phone TEXT,
    email TEXT,
    qr_code_hash TEXT UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Children
CREATE TABLE children (
    id INTEGER PRIMARY KEY,
    family_id INTEGER,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    birth_date DATE,
    allergies TEXT,
    special_needs TEXT,
    photo_path TEXT,
    FOREIGN KEY (family_id) REFERENCES families(id)
);

-- Guardians/Parents
CREATE TABLE guardians (
    id INTEGER PRIMARY KEY,
    family_id INTEGER,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    phone TEXT NOT NULL,
    photo_path TEXT,
    authorized_pickup BOOLEAN DEFAULT 1,
    is_primary BOOLEAN DEFAULT 0,
    FOREIGN KEY (family_id) REFERENCES families(id)
);

-- Check-in/Out Log
CREATE TABLE checkin_log (
    id INTEGER PRIMARY KEY,
    child_id INTEGER,
    guardian_checkin_id INTEGER,
    guardian_checkout_id INTEGER,
    room_id INTEGER,
    security_code TEXT,
    checked_in_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    checked_out_at TIMESTAMP NULL,
    FOREIGN KEY (child_id) REFERENCES children(id),
    FOREIGN KEY (guardian_checkin_id) REFERENCES guardians(id),
    FOREIGN KEY (guardian_checkout_id) REFERENCES guardians(id)
);

-- Service/Sessions
CREATE TABLE services (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    service_date DATE,
    start_time TIME,
    end_time TIME
);
```

**Label Template (2.4" x 3.9" Brother label):**
```
┌─────────────────────────────┐
│  [CHURCH LOGO]              │
│                             │
│  Emma Johnson               │
│  Age 4 / Preschool          │
│                             │
│  ⚠️ NUT ALLERGY             │
│                             │
│  Security Code: 4582        │
│  Room: 201                  │
│                             │
│  [BARCODE: 4582]            │
└─────────────────────────────┘
```

**Recommended Open Source Libraries:**
- **QR Generation:**
  - PHP: `chillerlan/php-qrcode`, `endroid/qr-code`
  - Node.js: `qrcode` (npm)
  - Python: `qrcode` (PyPI)
  
- **QR Scanning (Browser-based):**
  - `html5-qrcode` (JavaScript library)
  - `jsQR` (pure JavaScript QR decoder)
  - `zxing-js` (port of ZXing)

- **Label Printing:**
  - Brother QL: `brother_ql` (Python)
  - Generic: CUPS printing with PDF generation

**Caveats:**
- Requires technical expertise to build and maintain
- No commercial support
- You are responsible for security and compliance
- Plan for 8-16 hours of development time

---

## Comparison Matrix

| Feature | ChurchApps | ChurchCRM+Custom | Jethro | DIY System |
|---------|------------|------------------|--------|------------|
| **QR Code Check-In** | ✅ | ⚠️ (custom dev) | ❌ | ✅ (build it) |
| **Label Printing** | ✅ | ⚠️ (custom dev) | ❌ | ✅ (build it) |
| **Offline Mode** | ✅ | ❌ | ❌ | ✅ (build it) |
| **Mobile App** | ✅ Native | ❌ | ❌ | ❌ (PWA possible) |
| **Pre-check-in** | ✅ | ❌ | ❌ | ✅ (build it) |
| **Setup Time** | 30 min | 4-8 hrs | 2-3 hrs | 8-16 hrs |
| **Skill Level** | Beginner | Intermediate | Intermediate | Advanced |
| **Cost** | Free | Free | Free | Free (+ dev time) |

---

## Security Checklist

☐ **Unique security codes** every service/session  
☐ **Authorized pickup list** strictly enforced  
☐ **Photo verification** for unknown guardians  
☐ **Two-person rule** for children under 2  
☐ **Room capacity limits** enforced by system  
☐ **Emergency contact** info readily accessible  
☐ **Audit log** of all check-ins/outs  
☐ **Background checks** documented for all workers  
☐ **Secure network** (HTTPS, local preferred)  
☐ **Backup plan** if system fails (paper backup)  

---

## Recommendations by Church Size

### Church Plant (< 50 people)
**Use:** Paper sign-in sheets or simple spreadsheet
- Not worth the complexity yet
- Use printed name tags with highlighters for allergies

### Small Church (50-200)
**Use:** ChurchApps Cloud (free tier)
- Professional check-in with minimal setup
- Native mobile apps included
- Scales as you grow

### Mid-Size Church (200-1000)
**Use:** ChurchApps (self-hosted) or DIY system
- Self-hosted gives you full control
- DIY option if you have development resources
- Multiple check-in stations needed

### Large Church (1000+)
**Use:** Evaluate ChurchApps vs commercial solutions
- May need multiple concurrent check-in stations
- Consider integration with access control systems
- Professional support may be worth the cost

---

## Integration Notes

### With ChurchCRM:
- Extend existing Sunday School check-in
- Use Groups feature for room assignments
- API available for custom integrations

### With ChurchApps:
- Native integration — no additional work needed
- Check-in data flows to attendance reports
- Parent contact info already in system

### With Jethro:
- Use attendance tracking features
- Export data for reporting
- Roster integration for worker assignments

### Standalone (DIY):
- Design export format early (CSV/JSON)
- Consider ChMS import for long-term storage
- Keep family records synced manually or via API

---

*Last Updated: 2026-02-03 | Maintained by: church-tech-stack maintainers*
