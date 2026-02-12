# 🎬 AI Shorts Automator

An automated short-form video generator (TikTok, Reels, Shorts) powered by Python. This script transforms plain text into engaging vertical videos with AI-generated voiceovers, smart text wrapping, and automatic 9:16 cropping.

## 🚀 Features
- **AI Voiceover**: High-quality narration using `edge-tts` (Microsoft Azure Neural TTS).
- **Auto-Formatting**: Automatically resizes and crops any input video to a perfect 1080x1920 (9:16) format.
- **Smart Typography**: Dynamic text rendering with word wrap, safe margins, and stroke for maximum readability.
- **File-Driven Workflow**: Simply update `script.txt` to generate a new video in seconds.

## 🛠 Tech Stack
- **Python 3.10+**
- **MoviePy v2.0**: Professional video editing and processing.
- **Edge-TTS**: Microsoft Edge Online Text-to-Speech.
- **ImageMagick**: Advanced text rendering engine.

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/ai-shorts-automator.git](https://github.com/YOUR_USERNAME/ai-shorts-automator.git)
   cd ai-shorts-automator
   ```
2. **Install dependencies:
   ```bash
   pip install moviepy edge-tts
   ```
3.Install ImageMagick: Text rendering requires ImageMagick.

Note for Windows users: During installation, you MUST check the box "Install legacy utilities (e.g. convert)".

🚦 Usage
  1.Place your background video in the project folder and name it background.mp4.

  2.Edit script.txt and type the text you want to be narrated.

  3.Run the script:
  ```bash
  python main.py
  ```
  4.Find your generated video as result_tiktok_final.mp4.

⚙️ Configuration (in main.py)
VOICE: Change the AI voice (e.g., en-US-GuyNeural or uk-UA-OstapNeural).

FONT_PATH: Set your preferred system font.

size=(800, None): Adjust text block width for safe areas.

Built for content automation. Streamline your social media presence! 🚀
---
*Created by Vitalii Musiienko*
