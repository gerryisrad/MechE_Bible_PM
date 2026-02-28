# PocketMage Reference Manuals

A multi-manual, field-portable reference library for the [PocketMage PDA](https://www.pocketmage.com). Store any number of Markdown-based manuals on the SD card and browse, read, or write entries directly on-device.

---

## SD Card Structure

```
/manuals/
  Machining/
    entries/
      turning.md
      feeds_speeds.md
    images/
  Electrical/
    entries/
      ohms_law.md
      kirchhoffs_laws.md
    images/
  Fluids/
    entries/
    images/
```

Entries are plain `.md` files. Images are 1-bit BMP files placed in the `images/` folder and referenced in Markdown as `![filename.bmp]`.

---

## Controls

### Manual Selector (boot screen)
| Key | Action |
|-----|--------|
| `<` / `>` | Navigate manual list |
| `SPACE` or `ENTER` | Open selected manual |
| `FN+Q` | Exit to PocketMage OS |
| `FN+CENTER` | Force exit (any screen) |

### Browser (entry list)
| Key | Action |
|-----|--------|
| `<` / `>` | Navigate entries |
| `FN+<` / `FN+>` | Jump 10 entries |
| `SPACE` or `ENTER` | Open entry |
| `N` | New entry |
| Any letter/number | Search filter |
| `BACKSPACE` | Delete filter char |
| `FN+Q` | Back to Manual Selector |

### Viewer (reading an entry)
| Key | Action |
|-----|--------|
| `<` / `>` | Scroll page |
| `FN+<` / `FN+>` | Previous / next chunk |
| `E` | Edit this entry |
| `B` | Back to Browser |
| `FN+Q` | Back to Browser |

### Editor
| Key | Action |
|-----|--------|
| `<` / `>` | Navigate lines |
| `FN+<` / `FN+>` | Move cursor within line |
| `FN+SHIFT+<` / `FN+SHIFT+>` | Jump to start / end of line |
| `ENTER` | New line (commits to E-ink) |
| `BACKSPACE` | Delete char / merge line |
| `FN+ENTER` | Save & return to Browser |
| `FN+Q` | Discard & exit |

> **Note:** Typing only updates the OLED (live preview). The E-ink screen refreshes only on ENTER, line navigation, save, or merge — protecting the display from unnecessary wear.

---

## Supported Markdown

| Syntax | Style |
|--------|-------|
| `# Heading` | H1 |
| `## Heading` | H2 |
| `### Heading` | H3 |
| `**bold**` | Bold |
| `- item` | Unordered list |
| `1. item` | Ordered list |
| `> quote` | Blockquote |
| ` ``` ` | Code block |
| `---` | Horizontal rule |
| `![file.bmp]` | Embedded image |

---

## Build & Flash

1. Open in PlatformIO
2. Build: `pio run -e OTA_APP`
3. Output: `.pio/build/OTA_APP/firmware.bin`
4. Package: repack into `RefManuals.tar` with your icon (`RefManuals_ICON.bin`)
5. Drop `RefManuals.tar` on your PocketMage SD card and install via the OS app manager

---

## Adding a New Manual

Simply create a folder inside `/manuals/` on the SD card:
```
/manuals/YourManualName/entries/
/manuals/YourManualName/images/
```
Drop `.md` files in `entries/`. The app will automatically detect it on the next launch.
