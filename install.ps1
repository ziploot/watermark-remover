# ZipLoot AI Watermark Remover PowerShell Installer
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$OutputEncoding = [System.Text.Encoding]::UTF8

Write-Host "==================================================" -ForegroundColor Cyan
Write-Host "  ZIPLOOT AI WATERMARK REMOVER WEB STUDIO  " -ForegroundColor Cyan
Write-Host "==================================================" -ForegroundColor Cyan

$CacheBuster = Get-Date -UFormat %s
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/Ziplootapp/watermark-remover/main/video_web_app.py?v=$CacheBuster" -OutFile "video_web_app.py" -UseBasicParsing
Write-Host "[SUCCESS] Downloaded video_web_app.py successfully!" -ForegroundColor Green
Write-Host "[INFO] Opening ZipLoot Web Studio in your browser on http://localhost:7860..." -ForegroundColor Yellow

python video_web_app.py
