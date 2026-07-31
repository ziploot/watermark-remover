# ZipLoot AI Watermark Remover PowerShell Installer
Write-Host "==================================================" -ForegroundColor Cyan
Write-Host "  ZIPLOOT AI WATERMARK REMOVER 1-CLICK INSTALLER  " -ForegroundColor Cyan
Write-Host "==================================================" -ForegroundColor Cyan

Invoke-WebRequest -Uri "https://raw.githubusercontent.com/Ziplootapp/watermark-remover/main/video_web_app.py" -OutFile "video_web_app.py"
Write-Host "[SUCCESS] Downloaded video_web_app.py successfully!" -ForegroundColor Green
python video_web_app.py
