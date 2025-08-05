# 🖼️ ASCII Art Converter

This is a Python command-line tool that converts images into ASCII art. It resizes the image, maps each pixel's brightness to a character from a defined ASCII set, and outputs the result to a text file.

---

## 🚀 Features

- Grayscale-to-ASCII mapping
- Adjustable scaling factor
- Custom ASCII character sets
- Outputs art to a `.txt` file
- Works with JPEG, PNG, and other common formats

---

## 📦 Requirements

- Python 3.x
- Pillow (`pip install Pillow`)

---

## 🔧 Installation & Usage

1. **Clone the repository**
   ```bash
   git clone https://github.com/LU-FFY/IMAGE-TO-ASCII.git
   cd IMAGE-TO-ASCII
2. **Install dependencies**
   ```bash
   pip install Pillow
   or (if using Python 3 explicitly):
   ```bash
   pip3 install Pillow
3.	**Run the script via CLI**
   ```bash
   python ascii_converter.py mona_lisa.jpg -s 3 -o mona_output.txt
4. **Customization:**
      You can tweak:
      	•	scale → How much the image is downscaled (lower = more detail)
      	•	charset → Change brightness-to-symbol mapping for your preferred look
      
      Example with a custom character set:
      ```bash
      python ascii_converter.py mona_lisa.jpg -s 2 -c "@#%=+-. "
5. **Contributing**

Pull requests are welcome!
Feel free to fork the repo, create a branch, and submit improvements.
