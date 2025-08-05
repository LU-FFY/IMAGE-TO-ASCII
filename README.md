# 🖼️ ASCII Art Converter

A Python command-line tool that converts images into ASCII art. It resizes the image, maps pixel brightness to ASCII characters, and outputs the result to a `.txt` file.

---

## 🚀 Features

- Grayscale-to-ASCII character mapping  
- Adjustable scaling factor (`-s`)  
- Custom ASCII character sets (`-c`)  
- Outputs art to a `.txt` file  
- Supports common formats: `.jpg`, `.jpeg`, `.png`, `.webp`, etc.

---

## 📦 Requirements

- Python 3.10 or newer  
- Pillow (Python Imaging Library)

Install with:

```bash
pip install pillow
```

Or, if using Python 3 explicitly:

```bash
pip3 install pillow
```

---

## 🔧 Installation & Usage

1. **Clone the repository**

```bash
git clone https://github.com/LU-FFY/IMAGE-TO-ASCII.git
cd IMAGE-TO-ASCII
```

2. **Install dependencies**

```bash
pip install pillow
```

3. **Run the script**

```bash
python ascii_converter.py mona_lisa.jpg -s 3 -o mona_output.txt
```

> This will create a text file `mona_output.txt` containing the ASCII art.

---

## 🎛️ Optional Arguments

| Flag | Description |
|------|-------------|
| `-s` or `--scale` | Adjust the downscaling factor (default: `1`) |
| `-c` or `--charset` | Custom ASCII characters ordered from dark to light |
| `-o` or `--output` | Output file name (default: `output.txt`) |

### 🧪 Example with custom charset:

```bash
python ascii_converter.py mona_lisa.jpg -s 2 -c "@#%=+-. " -o ascii_mona.txt
```

---

## 🧠 Notes

- Higher scale values = more zoomed out = smaller output  
- Shorter charsets = less contrast  
- Darker characters (like `@` or `#`) should appear **first** in the charset

---

## 🤝 Contributing

Pull requests are welcome!  
Feel free to fork the repo, make changes, and submit improvements via PR.

---

## 📄 License

MIT License – do what you want, but give credit where it's due.
