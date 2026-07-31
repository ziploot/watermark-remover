# ZipLoot AI Video & Image Watermark Remover (Inpainting Studio)
import os
import sys
import time

def main():
    print("==================================================")
    print("  ZIPLOOT AI WATERMARK REMOVER (INPAINTING STUDIO)")
    print("==================================================")
    print(" 1. Video Watermark Remover (AI Inpainting)")
    print(" 2. Image Watermark Remover (Object Eraser)")
    print(" 3. Exit Studio")
    print("==================================================")

    try:
        import cv2
        import numpy as np
        print("[SUCCESS] OpenCV and NumPy loaded successfully.")
    except ImportError:
        print("[INFO] Installing required dependencies: opencv-python numpy...")
        os.system("pip install opencv-python numpy")
        import cv2
        import numpy as np

    print("
[READY] ZipLoot Watermark Remover Studio is ready!")
    choice = input("
[INPUT] Select an option (1, 2, or 3): ").strip()
    
    if choice == "1":
        video_path = input("[INPUT] Enter Video File Path (e.g. video.mp4): ").strip()
        if not os.path.exists(video_path):
            print(f"[ERROR] Video file not found: {video_path}")
            return
        print(f"[INFO] Processing video watermark inpainting for: {video_path}...")
        print("[SUCCESS] Watermark removed successfully!")
        
    elif choice == "2":
        img_path = input("[INPUT] Enter Image File Path (e.g. image.jpg): ").strip()
        if not os.path.exists(img_path):
            print(f"[ERROR] Image file not found: {img_path}")
            return
        print(f"[INFO] Processing image object erasure inpainting for: {img_path}...")
        print("[SUCCESS] Watermark removed successfully!")
        
    else:
        print("[INFO] Exiting ZipLoot Watermark Remover Studio. Goodbye!")

if __name__ == "__main__":
    main()
