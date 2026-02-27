# MechE Bible

A mechanical engineering dictionary and reference indexer for the [PocketMage PDA](https://github.com/ashtf8/PocketMage_PDA).

Browse, search, read, and create engineering reference entries stored as Markdown files on the SD card.

## Features

- Alphabetical entry browser with search-as-you-type filtering
- Markdown viewer with headings, bold, lists, code blocks, block quotes, and horizontal rules
- On-device line editor for creating and editing entries
- 1-bit BMP image support for diagrams on the e-ink display
- Content stored as plain `.md` files -- editable on any computer via USB

## Quick Start

1. Copy `MechE_Bible.tar` to `/apps/` on your PocketMage SD card
2. Create `/meche/entries/` and `/meche/images/` on the SD card
3. Copy sample entries from `sample_sd_content/meche/entries/` into `/meche/entries/`
4. Open the PocketMage App Loader, select MechE_Bible, install to an OTA slot
5. Launch the app

## SD Card Layout

```
/apps/
  MechE_Bible.tar          <-- app binary
/meche/
  entries/
    beam_deflection.md     <-- your reference entries
    bolted_joints.md
    fatigue_analysis.md
  images/
    diagram.bmp            <-- 1-bit BMP, max 320x200
```

## Controls

### Global

| Key | Action |
|---|---|
| FN + CENTER (d-pad click) | Exit to PocketMage OS (works from any screen) |
| Hold power button 3 sec | Hard reset to PocketMage OS |

### Browser

| Key | Action |
|---|---|
| < / > | Navigate entries |
| FN + < / > | Jump 10 entries |
| SPACE / ENTER / CENTER | Open selected entry |
| N | Create new entry |
| Type any letter | Search/filter |
| BACKSPACE | Remove filter character |
| ESC | Exit to PocketMage OS |

### Viewer

| Key | Action |
|---|---|
| < / > | Previous / next page |
| SPACE | Next page |
| FN + < / > | Previous / next chunk |
| E | Edit current entry |
| B or ESC | Back to browser |

### Editor

| Key | Action |
|---|---|
| < / > | Move cursor up / down (lines) |
| FN + < / > | Move cursor left / right (within line) |
| FN+SHIFT + < / > | Jump to start / end of line |
| ENTER | New line |
| BACKSPACE | Delete character |
| FN + ENTER | Save and exit |
| ESC | Discard and exit (confirms if unsaved changes) |

### Confirm Dialog

| Key | Action |
|---|---|
| SPACE / ENTER / CENTER | Yes |
| ESC | No |

## Entry Format

Each `.md` file is a self-contained reference entry using standard Markdown:

```markdown
# Entry Title

**Category:** Topic Area
**Tags:** keyword1, keyword2

---

Content here. Supported syntax:

## Subheadings
- Bullet lists
- **Bold text**
1. Numbered lists
> Block quotes

Images: ![filename.bmp]
```

## Adding Content

**On-device:** Press N in the browser to create a new entry. Type using the keyboard, then FN+ENTER to save.

**Via USB:** Connect the PocketMage, open `/meche/entries/`, and create or edit `.md` files with any text editor.

## Image Converter

Convert images to 1-bit BMP for the e-ink display:

```
pip install Pillow
python tools/convert_image.py input.png output.bmp
```

Options: `--width` and `--height` for max dimensions (default 320x200). Uses Floyd-Steinberg dithering.

## Building from Source

Requires [PlatformIO](https://platformio.org/).

```
cd Code/PocketMage_V3
pio run -e OTA_APP
```

Output: `.pio/build/OTA_APP/firmware.bin`

To package as `.tar` for the App Loader:

```
mkdir staging
copy .pio\build\OTA_APP\firmware.bin staging\MechE_Bible.bin
tar -cf MechE_Bible.tar -C staging MechE_Bible.bin
```

Place the `.tar` in `/apps/` on the SD card and install via the App Loader.

## Based On

Built on the [PocketMage PDA](https://github.com/ashtf8/PocketMage_PDA) platform using the OTA app framework. Markdown rendering approach inspired by [BookReader_PM](https://github.com/sosalover/BookReader_PM).

## License

Apache-2.0
