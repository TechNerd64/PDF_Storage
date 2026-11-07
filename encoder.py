import os
import sys

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

# Configuration of PDF page size and layout
PAGE_WIDTH, PAGE_HEIGHT = A4
SQUARE_SIZE = 4
MARGIN = 10

ENCODER_VERSION = "1.0.0"

def encode(input_file):
    # Read the input file and encode its contents into a PDF
    with open(input_file, 'rb') as f:
        data = f.read()

    filename = os.path.basename(input_file)
    extension = os.path.splitext(filename)[1].lower()
    output_file = os.path.splitext(input_file)[0] + ".pdf"

    # create pdf canvas
    pdf = canvas.Canvas(output_file, pagesize=A4)

    # Store the filename and extension in the PDF metadata
    pdf.setTitle(filename)
    pdf.setSubject(extension)
    pdf.setKeywords(str(len(data)))
    pdf.setCreator(f"PDF Encoder v{ENCODER_VERSION}")
    pdf.setAuthor("PDF Encoder - TechNerd64")

    
    
