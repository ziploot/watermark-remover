#!/bin/bash
echo "=================================================="
echo "  ZIPLOOT AI WATERMARK REMOVER 1-CLICK INSTALLER  "
echo "=================================================="
curl -sL "https://raw.githubusercontent.com/Ziplootapp/watermark-remover/main/video_web_app.py" -o video_web_app.py
echo "[SUCCESS] Downloaded video_web_app.py successfully!"
python3 video_web_app.py
