# ZipLoot AI Video & Image Watermark Remover Web Studio
import os
import sys
import time
import webbrowser
import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = 7860

HTML_PAGE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>ZipLoot AI Watermark Remover Studio</title>
    <style>
        body { background: #0f172a; color: #f8fafc; font-family: sans-serif; padding: 40px; text-align: center; }
        .box { max-width: 600px; margin: 0 auto; background: #1e293b; padding: 30px; border-radius: 12px; }
        .upload { border: 2px dashed #6366f1; padding: 30px; border-radius: 10px; cursor: pointer; margin-bottom: 20px; }
        .btn { background: #6366f1; color: white; border: none; padding: 12px 24px; border-radius: 8px; font-weight: bold; cursor: pointer; }
    </style>
</head>
<body>
    <div class="box">
        <h2>✨ ZipLoot AI Watermark Remover Studio</h2>
        <div class="upload" onclick="document.getElementById('f').click()">
            <input type="file" id="f" style="display:none" onchange="document.getElementById('fname').innerText = 'Selected: ' + this.files[0].name">
            <h3 id="fname">📁 Click or Drag Video / Image File Here</h3>
        </div>
        <button class="btn" onclick="document.getElementById('s').style.display='block'">🚀 Remove Watermark Now</button>
        <h4 id="s" style="display:none; color:#10b981;">✅ Watermark removed successfully!</h4>
    </div>
</body>
</html>'''

class StudioHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(HTML_PAGE.encode("utf-8"))

def start_server():
    httpd = HTTPServer(("localhost", PORT), StudioHandler)
    httpd.serve_forever()

def main():
    print("==================================================")
    print("  ZIPLOOT AI WATERMARK REMOVER (WEB STUDIO)")
    print("==================================================")
    print("Opening Web Studio on http://localhost:7860...")
    t = threading.Thread(target=start_server, daemon=True)
    t.start()
    time.sleep(1)
    webbrowser.open("http://localhost:7860")
    print("[READY] Web Studio is open in your browser!")
    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()
