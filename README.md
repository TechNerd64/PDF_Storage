# PDF Storage

PDF Storage is a Python-based utility that encodes arbitrary files into PDF documents using grayscale graphical elements. It allows files such as PNGs, ZIPs, PDFs, and other binary formats to be stored within a PDF and subsequently reconstructed.

## Encoding and Decoding

PDF Storage consists of three main components:

- **Main:** Handles command-line arguments and routes requests to the appropriate module.
- **Encoder:** Reads source files as binary data and encodes their contents into grayscale rectangles within a PDF. Original file information is stored in the PDF metadata.
- **Decoder:** Reads the encoded graphical elements and PDF metadata to reconstruct the original file.

The encoder and decoder use matching encoding rules to ensure that recovered files retain their original binary contents.

## Installation

Install the required dependencies:

```bash
python3 -m pip install reportlab pypdf
```

## Usage

PDF Storage uses the following command syntax:

```bash
python3 main.py <operation> <file>
```

### Encode

To encode a file into a PDF:

```bash
python3 main.py encode <input_file>
```

Example:

```bash
python3 main.py encode picture.png
```

This generates `picture.pdf` containing the encoded data.

### Decode

To recover an encoded file:

```bash
python3 main.py decode <input_pdf>
```

Example:

```bash
python3 main.py decode picture.pdf
```

This reconstructs the original file using its filename and metadata stored within the PDF.

## Building

PDF Storage can be compiled into a standalone Linux executable using PyInstaller.

Install PyInstaller:

```bash
python3 -m pip install pyinstaller
```

Build the executable:

```bash
pyinstaller --onefile --name pdf-storage main.py
```

The resulting executable will be located in `dist/`.

Usage with the compiled executable:

```bash
./dist/pdf-storage encode picture.png
./dist/pdf-storage decode picture.pdf
```

## Project Structure

```text
PDF_Storage/
├── main.py
├── encoder.py
├── decoder.py
├── requirements.txt
├── build/
├── dist/
└── pdf-storage.spec
```

## Development Status

PDF Storage is currently in early development.

The initial encoder and decoder implementations establish a basic grayscale-based PDF storage format. Further development will focus on improving data identification, reliability, compatibility, and storage efficiency.