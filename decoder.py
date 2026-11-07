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
