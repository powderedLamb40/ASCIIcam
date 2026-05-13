import cv2
import os
import numpy as np

ASCII_CHARS = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

def main():
    cap = cv2.VideoCapture(1)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

    cols, rows = os.get_terminal_size()
    
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            frame_resized = cv2.resize(frame, (cols, rows))
            gray_frame = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2GRAY)
            output = ""
            for y in range(rows):
                for x in range(cols):
                    pixel_brightness = gray_frame[y, x]
                    char = ASCII_CHARS[int(pixel_brightness / 256 * len(ASCII_CHARS))]
                    b, g, r = frame_resized[y, x]
                    output += f"\x1b[38;2;{r};{g};{b}m{char}"
                output += "\n"
            print("\x1b[H" + output, end="")
    except KeyboardInterrupt:
        pass
    finally:
        cap.release()
        print("\x1b[0m")

if __name__ == "__main__":
    main()import cv2
import os
import numpy as np

ASCII_CHARS = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

def main():
    cap = cv2.VideoCapture(1)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

    cols, rows = os.get_terminal_size()
    
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            frame_resized = cv2.resize(frame, (cols, rows))
            gray_frame = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2GRAY)
            output = ""
            for y in range(rows):
                for x in range(cols):
                    pixel_brightness = gray_frame[y, x]
                    char = ASCII_CHARS[int(pixel_brightness / 256 * len(ASCII_CHARS))]
                    b, g, r = frame_resized[y, x]
                    output += f"\x1b[38;2;{r};{g};{b}m{char}"
                output += "\n"
            print("\x1b[H" + output, end="")
    except KeyboardInterrupt:
        pass
    finally:
        cap.release()
        print("\x1b[0m")

if __name__ == "__main__":
    main()
