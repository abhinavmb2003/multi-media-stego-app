# 🕵️ Multi-Media ShadowCode Framework

A desktop steganography application built with Python and CustomTkinter that lets you **hide secret messages inside multimedia files** — images, audio, video, and text — using Least Significant Bit (LSB) encoding.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![GUI](https://img.shields.io/badge/GUI-CustomTkinter-blueviolet)

---

## ✨ Features

- **Multi-medium steganography** — encode and decode hidden messages in:
  - 🖼️ Images (`.png`, `.bmp`)
  - 🔊 Audio (`.wav`)
  - 🎬 Video (`.avi` — FFV1 codec)
  - 📄 Text (`.txt`)
- **Modern dark-mode GUI** powered by [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
- **LSB (Least Significant Bit)** encoding — visually and audibly imperceptible
- **Delimiter-based message boundary detection** for reliable decoding
- **Live date/time display** on the welcome screen
- **In-app User Guide** / Help page

---

## 🖥️ Screenshots

> Place your screenshots in a `screenshots/` folder and update the paths below.

| Welcome Screen | Encode Tab | Decode Tab |
|:-:|:-:|:-:|
| *(screenshot)* | *(screenshot)* | *(screenshot)* |

---

## 🚀 Getting Started

### Prerequisites

- Python **3.8 or higher**
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/your-username/shadowcode.git
cd shadowcode

# 2. Install dependencies
pip install -r requirements.txt

# 3. Add your logo image
# Place your logo as Image.png in the project root
# (or update the logo_path in SHADOWCODE.py)

# 4. Run the app
python SHADOWCODE.py
```

---

## 📁 Project Structure

```
shadowcode/
├── SHADOWCODE.py       # Main application source
├── Image.png           # App logo (add your own)
├── requirements.txt    # Python dependencies
├── README.md
├── LICENSE
└── screenshots/        # (optional) UI screenshots
```

---

## 📖 How to Use

### Encoding a Message

1. Launch the app and click **Let's Start**.
2. Go to the **Encode** tab.
3. Select a medium: **Text / Image / Audio / Video**.
4. Type your secret message in the text box.
5. Click **Select Input File** and choose a carrier file.
6. For images, choose **PNG** or **BMP** format.
7. Click **Choose Save Path** to set the output file location.
8. Click **Encode** — your message is now hidden!

### Decoding a Message

1. Go to the **Decode** tab.
2. Select the medium and format matching the stego file.
3. Click **Select Stego File** and open the encoded file.
4. Click **Decode** — the hidden message appears in the output box.

---

## ⚠️ Supported File Formats

| Medium | Input Format | Notes |
|--------|-------------|-------|
| Image  | `.png`, `.bmp` | Lossless formats only — JPEG is not supported |
| Audio  | `.wav` | Uncompressed PCM WAV only |
| Video  | `.avi` | FFV1 codec (lossless); output uses FFV1 |
| Text   | `.txt` | Stores message directly |

> **Important:** Always use lossless formats. Lossy compression (JPEG, MP3) will destroy the hidden data.

---

## 🔧 Configuration

The logo image path is currently hardcoded. To change it, update this line in `SHADOWCODE.py`:

```python
logo_path = r"Image.png"   # relative path from the project root
```

---

## 📦 Dependencies

| Package | Purpose |
|---------|---------|
| `customtkinter` | Modern themed Tkinter GUI widgets |
| `opencv-python` | Image and video read/write |
| `Pillow` | Image loading for the GUI logo |
| `numpy` | Array operations (used with OpenCV) |

Standard library modules used: `tkinter`, `wave`, `os`, `datetime`.

---

## 🛡️ How It Works (LSB Steganography)

Each character of the secret message is converted to its 8-bit binary representation. Each bit is then written into the **least significant bit** of a pixel channel (R, G, or B), audio sample byte, or video frame pixel. A fixed **delimiter** (`1111111111111110`) marks the end of the message so decoding stops at the right place.

Because only the last bit of each byte changes, the visual/audio difference is imperceptible to the human eye and ear.

---

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## 🙌 Acknowledgements

- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) by Tom Schimansky
- [OpenCV](https://opencv.org/) for image and video processing
- [Pillow](https://python-pillow.org/) for image handling
