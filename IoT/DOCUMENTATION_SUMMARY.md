# IoT Projects - Documentation Summary

## ✅ Completed Work

### Labs (1-5)
All 5 IoT labs completed with working code and reports:
- **Lab 1**: Lua JSON/MAC handling
- **Lab 2**: Lua Regex/Data parsing  
- **Lab 3**: NATS Protocol messaging
- **Lab 4**: Django Web Server
- **Lab 5**: MQTT Communication

Each lab has `report.md` with code and output.

### Project 1: Django and MQTT
**Location:** `IoT/Django and MQTT project #1/`

**Files:**
- `REPORT.md` - Full project report with screenshots
- `REPORT.html` - HTML version for easy viewing/printing
- `1.png`, `2.png`, `3.png`, `4.png` - Screenshots
- `README.md` - Running instructions
- `src/` - All source code

**Contents:**
- Task 1.1: Basic Django server
- Task 1.2: WebSocket echo server
- Task 1.3: MQTT listener
- Task 2: API fetch → JSON → MQTT

### Project 2: Home Assistant Mock Device
**Location:** `IoT/Homeassiant and MQTT integration project #2/`

**Files:**
- `REPORT.md` - Full project report
- `REPORT.html` - HTML version for easy viewing/printing
- `README.md` - Running instructions
- `src/mock_device.py` - Mock sensor implementation
- `src/mqtt_subscriber.py` - Test subscriber

**Contents:**
- MQTT Discovery protocol implementation
- Mock weather station (temp/humidity/pressure)
- Home Assistant integration

---

## Converting to PDF

### Method 1: Firefox Print to PDF
1. Open the HTML file in Firefox:
   ```bash
   firefox "IoT/Django and MQTT project #1/REPORT.html"
   firefox "IoT/Homeassiant and MQTT integration project #2/REPORT.html"
   ```
2. Press Ctrl+P (or Cmd+P on Mac)
3. Choose "Save to PDF" as destination
4. Adjust settings:
   - Enable "Print backgrounds"
   - Set margins if needed
5. Click Save

### Method 2: Command Line (if wkhtmltopdf installed)
```bash
sudo pacman -S wkhtmltopdf
wkhtmltopdf REPORT.html REPORT.pdf
```

### Method 3: LibreOffice (can open markdown directly)
```bash
sudo pacman -S libreoffice-fresh
libreoffice --headless --convert-to pdf REPORT.md
```

---

## Report Structure

Both reports include:
- ✅ Project overview
- ✅ Implementation details with code snippets
- ✅ Screenshots showing working features
- ✅ Running instructions
- ✅ Technologies used
- ✅ Conclusions and learning points

---

## To Print/Submit

1. **Markdown files** (`.md`) - Original format, can be viewed in VS Code or any text editor
2. **HTML files** (`.html`) - Open in browser, easy to print to PDF
3. **Screenshots** (`.png`) - Already embedded in reports

The easiest way to get PDFs is to open the HTML files in Firefox and print to PDF.
