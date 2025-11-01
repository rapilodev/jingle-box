# Jingle‑Box

**Browser-based Jingle & Station ID Player**

Jingle‑Box is an open-source, profile-based player for creating radio jingles, sweepers, and station IDs from modular audio clips—entirely in the browser, no backend required. Multiple profiles let users maintain separate audio libraries, with flexible playback and sequence customization.

---

## Features

- Profiles with audio categories: `uhr` (time), `sender` (station), `studio`, `sendereihe` (show), `spruch` (phrases), `frequenz` (frequency), `soundbett` (background)  
- Select fixed or random clips; preview individual elements  
- Drag-and-drop to reorder categories; playback sequence customizable  
- Settings saved per profile in local storage  
- `content.cgi` generates JSON from the directory/file structure for the player  

---

## Setup

1. Clone the repo to your Apache web root (e.g., `/var/www/html/jingle-box`)  
2. Enable CGI and make `content.cgi` executable:

```bash
sudo a2enmod cgi
chmod +x content.cgi
```

3. Open `index.html` in a modern browser  
4. Add audio clips using the folder structure:

```text
default/
  spruch/
  sender/
  frequenz/
  sendereihe/
  uhr/
  studio/
  soundbett/
```

- Use lowercase, hyphens for filenames (e.g., `18-00.wav`)  

---

## Usage

- Select a profile, enable/disable categories, choose fixed or random clips  
- Preview clips, drag categories to reorder, and press **Play**  
- Volume slider included; all settings saved per profile  

**Default sequence:** Uhrzeit → Sender → Studio → Sendereihe → Spruch → Soundbett  

---

## License

GPL-3.0 — see [LICENSE](LICENSE)  

---

Jingle‑Box is a lightweight, open-source tool for assembling radio jingles in the browser, with flexible profiles, customizable playback, and easy setup.

