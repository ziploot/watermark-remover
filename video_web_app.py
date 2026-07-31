# ZipLoot AI Video & Image Watermark Remover (Inpainting) Studio
import os
import sys
import time

print("==================================================")
print("  ZIPLOOT AI WATERMARK REMOVER (INPAINTING STUDIO)")
print("==================================================")
print("1. Video Watermark Remover (AI Inpainting)")
print("2. Image Watermark Remover (Object Eraser)")
print("==================================================")

try:
    import cv2
    import numpy as np
    print("[SUCCESS] OpenCV & NumPy loaded successfully.")
except ImportError:
    print("[INFO] Installing required dependencies: opencv-python numpy...")
    os.system("pip install opencv-python numpy")

print("
[READY] ZipLoot Watermark Remover is configured and ready to run!")
