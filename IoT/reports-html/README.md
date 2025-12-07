# 📚 IoT Reports - Complete Documentation

## ✅ All Reports Compiled

All lab reports and project reports have been converted to HTML and organized in the `reports-html/` folder.

### 📁 Location
```
IoT/reports-html/
├── index.html                      # Main navigation page
├── Lab1-Report.html                # Lab 1: Basic Lua Handling
├── Lab2-Report.html                # Lab 2: Lua Regex and Data Parsing
├── Lab3-Report.html                # Lab 3: NATS Protocol Testing
├── Lab4-Report.html                # Lab 4: Django Testing
├── Lab5-Report.html                # Lab 5: MQTT and Home Assistant
├── Project1-Django-MQTT.html       # Project 1 with screenshots
└── Project2-HA-Mock-Device.html    # Project 2
```

### 🌐 Viewing Reports

**Open the index page:**
```bash
firefox "IoT/reports-html/index.html"
```

The index page provides:
- Navigation to all 5 lab reports
- Navigation to 2 project reports
- Descriptions of each report
- Instructions for printing to PDF
- Technologies summary

### 📄 Converting to PDF

**Method 1: From Browser (Easiest)**
1. Open any report HTML file in Firefox
2. Press `Ctrl+P`
3. Select "Save to PDF"
4. Enable "Print backgrounds"
5. Click Save

**Method 2: Batch conversion with LibreOffice**
```bash
cd "IoT/reports-html"
for file in *.html; do
    libreoffice --headless --convert-to pdf "$file"
done
```

### 📊 Report Contents

**Labs (5 reports):**
- Code implementations
- Command outputs
- Conclusions
- Technologies used

**Projects (2 reports):**
- Complete implementation details
- Code snippets
- **Screenshots embedded** (Project 1 has 1.png, 2.png, 3.png, 4.png)
- Step-by-step results
- Learning points and conclusions

### 🎯 Summary

**Total:** 7 HTML reports ready for submission
- All properly formatted
- All include code and outputs
- Project 1 includes all 4 screenshots
- Ready to print to PDF
- Professional styling

**Technologies Covered:**
- Python, Lua, JavaScript
- Django, Channels, WebSockets
- MQTT, NATS protocols
- Docker, Mosquitto broker
- Home Assistant integration
- API integration
