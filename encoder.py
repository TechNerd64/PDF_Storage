
import os

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4


# Configuration
PAGE_WIDTH, PAGE_HEIGHT = A4
SQUARE_SIZE = 4
MARGIN = 10

ENCODER_VERSION = "1.0.0"


def encode(input_file):
    # Read input file as binary
    with open(input_file, "rb") as f:
        data = f.read()

    filename = os.path.basename(input_file)
    extension = os.path.splitext(filename)[1].lower()

    output_file = os.path.splitext(input_file)[0] + ".pdf"

    # Prevent overwriting an input PDF
    if os.path.abspath(output_file) == os.path.abspath(input_file):
        output_file = os.path.splitext(input_file)[0] + "_encoded.pdf"

    # Create PDF
    pdf = canvas.Canvas(output_file, pagesize=A4)

    # PDF metadata
    pdf.setTitle(filename)
    pdf.setSubject(extension)
    pdf.setKeywords(str(len(data)))
    pdf.setCreator(f"PDF Encoder v{ENCODER_VERSION}")
    pdf.setAuthor("PDF Encoder - TechNerd64")

    # Calculate page capacity
    columns = int((PAGE_WIDTH - 2 * MARGIN) / SQUARE_SIZE)
    rows = int((PAGE_HEIGHT - 2 * MARGIN) / SQUARE_SIZE)

    total_capacity = columns * rows

    print(f"Encoding: {filename}")
    print(f"File size: {len(data)} bytes")
    print(f"Page capacity: {total_capacity} bytes")

    # Encode bytes into grayscale rectangles
    for i, byte in enumerate(data):

        # Start new page when full
        if i > 0 and i % total_capacity == 0:
            pdf.showPage()

        position = i % total_capacity

        x = MARGIN + (position % columns) * SQUARE_SIZE

        y = PAGE_HEIGHT - MARGIN - (
            (position // columns) + 1
        ) * SQUARE_SIZE

        # Convert byte to grayscale
        shade = byte / 255

        pdf.setFillGray(shade)

        pdf.rect(
            x,
            y,
            SQUARE_SIZE,
            SQUARE_SIZE,
            fill=1,
            stroke=0
        )

    pdf.save()

    print("\nEncoding complete!")
    print(f"Output: {output_file}")

    return output_file
