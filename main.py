import cv2
import os
import numpy as np

# ตัวอักษรที่ใช้แทนระดับความสว่าง (จากมืดไปสว่าง)
ASCII_CHARS = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

def main():
    # เปิดกล้อง (0 คือกล้องหลัก)
    cap = cv2.VideoCapture(1)
    
    # ตั้งค่าความละเอียดกล้องเป็น 1920x1080 (ถ้ากล้องรองรับ)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

    # ตรวจสอบขนาด Terminal เพื่อบีบอัดภาพให้พอดีหน้าจอ
    # เพราะ 1 ตัวอักษรใหญ่กว่า 1 พิกเซลมาก
    cols, rows = os.get_terminal_size()
    
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # ย่อขนาดภาพให้เท่ากับขนาด Terminal
            frame_resized = cv2.resize(frame, (cols, rows))
            
            # แปลงเป็น Gray เพื่อหาความสว่าง
            gray_frame = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2GRAY)
            
            output = ""
            for y in range(rows):
                for x in range(cols):
                    # เลือกตัวอักษรจากความสว่าง
                    pixel_brightness = gray_frame[y, x]
                    char = ASCII_CHARS[int(pixel_brightness / 256 * len(ASCII_CHARS))]
                    
                    # ดึงสี RGB (OpenCV เป็น BGR)
                    b, g, r = frame_resized[y, x]
                    
                    # ใช้ ANSI Escape Code สำหรับสีพื้นหลังและสีตัวอักษร
                    # \x1b[38;2;R;G;Bm คือการกำหนดสีตัวอักษรแบบ TrueColor
                    output += f"\x1b[38;2;{r};{g};{b}m{char}"
                output += "\n"

            # พิมพ์ออกไปทีเดียว (ถอยกลับไปจุดเริ่มต้น 0,0 เพื่อลดการกระพริบ)
            print("\x1b[H" + output, end="")

    except KeyboardInterrupt:
        pass
    finally:
        cap.release()
        print("\x1b[0m") # ล้างค่าสี

if __name__ == "__main__":
    main()
