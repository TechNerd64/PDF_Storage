import os
import sys
from pypdf import PdfReader

# Encoder Configuration
ENCODER_VERSION = "1.0.0"
SQUARE_SIZE = 4

def decode(input_file):
    reader = PdfReader(input_file)
    metadata = reader.metadata
    if metadata is None:
        print("No metadata found in the PDF.")
        return

    filename = metadata.title
    extension = metadata.subject
    file_size = metadata.get('/Keywords')
    if filename or file_size is None:
        print("Metadata is incomplete or missing.")
        return

    try:
        file_size = int(file_size)
    except ValueError:
        print("Invalid file size in metadata.")
        return

    print(f"Decoding: {filename}")
    print(f"Original file size: {file_size} bytes")
    print(f"Original file extension: {extension}")

    #collect the bytes from the PDF
    data = bytearray()

    for page in reader.pages:
        content = page.get_contents()
        if content is None:
            continue

        operations = content.operations
        current_byte = None

        for operands, operator in operations:
            if operands[0] == b'g':
                # Get the grayscale value
                gray_value = operands[1][0]
                byte_value = int(gray_value * 255)
                data.append(byte_value)
        