"""
convert_image.py — Convert images to 1-bit BMP for PocketMage e-ink display.

Usage:
    python convert_image.py input.png output.bmp
    python convert_image.py input.jpg output.bmp --width 300 --height 180

Output will be a 1-bit (monochrome) BMP file suitable for displaying
on the PocketMage 320x240 e-ink panel.
"""

import argparse
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("Error: Pillow is required. Install with: pip install Pillow")
    sys.exit(1)


def convert_to_1bit_bmp(input_path: str, output_path: str,
                         max_width: int = 320, max_height: int = 200):
    img = Image.open(input_path)

    # Convert to grayscale first
    img = img.convert('L')

    # Resize to fit within max dimensions, preserving aspect ratio
    img.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)

    # Convert to 1-bit with Floyd-Steinberg dithering
    img = img.convert('1')

    # Save as BMP
    img.save(output_path, format='BMP')
    print(f"Converted: {input_path} -> {output_path} ({img.width}x{img.height}, 1-bit BMP)")


def main():
    parser = argparse.ArgumentParser(
        description="Convert images to 1-bit BMP for PocketMage e-ink display.")
    parser.add_argument('input', help="Input image file (PNG, JPG, etc.)")
    parser.add_argument('output', help="Output BMP file path")
    parser.add_argument('--width', type=int, default=320,
                        help="Maximum width in pixels (default: 320)")
    parser.add_argument('--height', type=int, default=200,
                        help="Maximum height in pixels (default: 200)")
    args = parser.parse_args()

    if not Path(args.input).exists():
        print(f"Error: Input file not found: {args.input}")
        sys.exit(1)

    convert_to_1bit_bmp(args.input, args.output, args.width, args.height)


if __name__ == '__main__':
    main()
