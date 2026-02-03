# Church Plant Stack

> Zero-budget setup for new churches. One weekend, one person.

## The Philosophy

Church plants have:
- **No budget** for software subscriptions
- **No IT staff** (maybe one volunteer)
- **No time** to configure complex systems
- **A mission** that matters more than tech

This stack prioritizes **speed of deployment** over **feature richness**.

## The Stack

| Function | Tool | Why This One |
|----------|------|--------------|
| **Website** | WordPress.com Free | Drag-and-drop, done in 2 hours |
| **Sermons** | YouTube (unlisted) + ChurchApps | Free hosting, embeddable player |
| **Giving** | Zelle/Venmo + Google Sheets | Zero fees, simple tracking |
| **Communication** | Signal Groups | Encrypted, everyone has it |
| **Presentation** | OpenLP | Free, works offline |
| **Calendar** | Google Calendar | Shareable, integrates with everything |

**Total monthly cost:** $0  
**Setup time:** 1 weekend  
**Technical skill:** Can use a web browser

---

## Step-by-Step Setup

### Day 1: Morning (Website)

1. **Create WordPress.com account**
   - Go to wordpress.com
   - Choose free plan
   - Pick a church-appropriate theme

2. **Essential pages:**
   - Home (service times, location)
   - About (vision, pastor bio)
   - Sermons (embed YouTube playlist)
   - Contact (email form)

3. **Get a custom domain later** when budget allows (~$12/year)

### Day 1: Afternoon (Sermons)

1. **Create YouTube channel**
   - Use church name
   - Upload logo as profile picture
   - Create "Sunday Sermons" playlist

2. **Upload settings:**
   - Visibility: Unlisted (not searchable)
   - Add title format: "[Date] - [Sermon Title] - [Scripture]"

3. **Embed on website:**
   - WordPress block: YouTube
   - Paste playlist URL
   - Set to show latest first

### Day 2: Morning (Giving)

1. **Set up Zelle** (if your bank supports it)
   - Use church's dedicated email
   - No fees for church or giver

2. **Set up Venmo** (backup option)
   - Create business profile
   - Slightly higher fees but universal

3. **Create tracking spreadsheet:**
   - Google Sheets template: [link]
   - Columns: Date, Name, Amount, Fund, Notes
   - Share with treasurer only

### Day 2: Afternoon (Presentation)

1. **Download OpenLP**
   - https://openlp.org/
   - Install on presentation laptop

2. **Initial setup:**
   - Import sample songs
   - Configure display output
   - Test with projector

3. **Create basic library:**
   - 20 common worship songs
   - Church logo slide
   - Scripture slide template

### Day 3: Polish

1. **Test everything**
2. **Create simple instructions** for volunteers
3. **Document login credentials** in password manager

---

## When to Upgrade

Move to the [Small Church Stack](../small-church/) when:

- You have **consistent weekly attendance >80**
- You need **child check-in** for safety
- Giving volume exceeds **$5k/month** (trackability issues)
- You have **volunteers who can manage tech**

---

## Common Issues

### "Our internet is terrible"
- OpenLP works offline — preload everything
- Download sermons to USB as backup
- Use phone hotspot for giving (minimal data)

### "We don't have a projector"
- Large TV works fine (55"+ recommended)
- HDMI cable from laptop
- Test visibility from back row

### "Someone needs to manage the slides"
- Train one person (15 minutes)
- Have a backup person
- Keep it simple — don't over-produce

---

## Files in This Directory

- `wordpress-setup.md` — WordPress.com walkthrough
- `openlp-quickstart.md` — First-time setup guide
- `giving-tracking-template.xlsx` — Google Sheets template
- `signal-groups-guide.md` — Setting up church communication

---

*Last updated: 2026-01-31*
