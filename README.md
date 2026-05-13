# ASCIIcam

A real-time ASCII art camera that converts video feed into ASCII characters, creating a unique text-based visualization of your webcam.

## Features

- 🎥 Real-time webcam capture
- 📝 ASCII art conversion
- ⚡ Fast and efficient processing
- 🎨 Multiple character sets
- 🖥️ Display in terminal or window

## Installation

```bash
git clone https://github.com/powderedLamb40/ASCIIcam.git
cd ASCIIcam
```

### Requirements

- Python 3.7+
- OpenCV (`cv2`)
- Pillow (PIL)

### Setup

```bash
pip install opencv-python pillow
```

## Usage

Run the application:

```bash
python asciicam.py
```

### Controls

- `q` - Quit the application
- `s` - Save current frame as ASCII art
- `c` - Cycle through character sets

## Configuration

You can customize the behavior by editing the configuration section in the script:

```python
# Adjust these values
WIDTH = 100
HEIGHT = 50
CHAR_SET = "@%#*+=-:. "
```

## How It Works

1. Captures frames from your webcam
2. Resizes frames to ASCII dimensions
3. Converts pixel brightness to ASCII characters
4. Displays the result in real-time

## Examples

<img width="1920" height="1052" alt="image" src="https://github.com/user-attachments/assets/dc86d258-4951-4b29-8c78-a7efd0f5402e" />


## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source. See the LICENSE file for details.

## Author

[powderedLamb40](https://github.com/powderedLamb40)
