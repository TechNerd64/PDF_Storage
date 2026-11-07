
import os

from pypdf import PdfReader


# Configuration
SQUARE_SIZE = 4


def decode(input_file):
    reader = PdfReader(input_file)

    # Retrieve PDF metadata
    metadata = reader.metadata

    if metadata is None:
        raise ValueError("PDF metadata not found.")

    filename = metadata.title
    extension = metadata.subject
    file_size = metadata.get("/Keywords")

    if not filename or file_size is None:
        raise ValueError("Missing file metadata.")

    try:
        file_size = int(file_size)
    except (ValueError, TypeError):
        raise ValueError("Invalid file size metadata.")

    if file_size < 0:
        raise ValueError("Invalid file size.")

    print(f"Original filename: {filename}")
    print(f"Original extension: {extension}")
    print(f"Original size: {file_size} bytes")

    # Collect encoded bytes
    data = bytearray()

    for page in reader.pages:

        contents = page.get_contents()

        if contents is None:
            continue

        operations = contents.operations
        current_gray = None

        for operands, operator in operations:

            # Read grayscale fill color
            if operator == b"g":
                current_gray = float(operands[0])

            # Read rectangle operations
            elif operator == b"re":

                if current_gray is None:
                    continue

                x, y, width, height = map(float, operands)

                # Identify encoded rectangles
                if (
                    abs(width - SQUARE_SIZE) < 0.001
                    and abs(height - SQUARE_SIZE) < 0.001
                ):
                    value = round(current_gray * 255)
                    data.append(value)

    # Validate recovered data
    if len(data) < file_size:
        raise ValueError(
            f"Insufficient data: expected {file_size} bytes, "
            f"found {len(data)} bytes."
        )

    # Trim to original file size
    data = data[:file_size]

    # Determine output filename
    filename = os.path.basename(filename)
    output_file = os.path.join(
        os.path.dirname(os.path.abspath(input_file)),
        filename
    )

    # Avoid overwriting existing files
    if os.path.exists(output_file):
        output_file = os.path.join(
            os.path.dirname(os.path.abspath(input_file)),
            "recovered_" + filename
        )

    # Save reconstructed file
    with open(output_file, "wb") as f:
        f.write(data)

    print("\nDecoding complete!")
    print(f"Recovered file: {output_file}")
    print(f"Recovered bytes: {len(data)}")

    return output_file

