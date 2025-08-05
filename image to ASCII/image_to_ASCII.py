import argparse
from PIL import Image
import os

# Default ASCII character set (from dark to light)
DEFAULT_CHARS = "@%#*+=-:. "

def get_ascii_char(value, charset):
    """Map a grayscale value (0-255) to an ASCII character."""
    index = int((value / 255) * (len(charset) - 1))
    return charset[index]

def convert_image_to_ascii(image_path, scale=3, output_file="ascii_output.txt", charset=DEFAULT_CHARS):
    # Open image and get original size
    try:
        img = Image.open(image_path)
    except Exception as e:
        print(f"❌ Failed to open image: {e}")
        return

    # Resize image based on scale factor and aspect correction
    width, height = img.size
    aspect_ratio = height / width
    new_width = width // scale
    new_height = int((height // scale) * 0.55)  # aspect ratio fix for font height
    img = img.resize((new_width, new_height))

    # Convert to grayscale
    img = img.convert('L')  # 'L' = 8-bit pixels, black and white

    # Generate ASCII
    ascii_art = ""
    for y in range(new_height):
        for x in range(new_width):
            pixel_value = img.getpixel((x, y))
            ascii_art += get_ascii_char(pixel_value, charset)
        ascii_art += "\n"

    # Write to output file
    with open(output_file, "w") as f:
        f.write(ascii_art)

    print(f"✅ ASCII art saved to: {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Convert an image to ASCII art.")
    parser.add_argument("image", help="Path to the input image file.")
    parser.add_argument("-s", "--scale", type=int, default=3, help="Scaling factor (default=3)")
    parser.add_argument("-o", "--output", default="ascii_output.txt", help="Output text file name")
    parser.add_argument("-c", "--charset", default=DEFAULT_CHARS, help="Custom character set (dark to light)")
    args = parser.parse_args()

    convert_image_to_ascii(args.image, args.scale, args.output, args.charset)

if __name__ == "__main__":
    main()
