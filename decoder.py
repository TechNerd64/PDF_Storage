
import os
import sys

from pypdf import PdfReader

# Encoder configuration
SQUARE_SIZE = 4
ENCODER_VERSION = "1.0.0"


def decode(input_file):
    reader = PdfReader(input_file)

    # Retrieve PDF metadata
    metadata = reader.metadata

    if metadata is None:
        print("Error: PDF metadata not found.")
        return

    filename = metadata.title
    extension = metadata.subject
    file_size = metadata.get("/Keywords")

    if not filename or file_size is None:
        print("Error: Missing file metadata.")
        return

    try:
        file_size = int(file_size)
    except ValueError:
        print("Error: Invalid file size metadata.")
        return

    print(f"Original filename: {filename}")
    print(f"Original extension: {extension}")
    print(f"Original size: {file_size} bytes")

    data = bytearray()

    for page in reader.pages:

        contents = page.get_contents()

        if contents is None:
            continue

        operations = contents.operations
        current_gray = None

        for operands, operator in operations:

            if operator == b"g":
                current_gray = float(operands[0])

            elif operator == b"re":

                if current_gray is None:
                    continue

                x, y, width, height = map(float, operands)

                # Identify encoded squares
                if (
                    abs(width - SQUARE_SIZE) < 0.001
                    and abs(height - SQUARE_SIZE) < 0.001
                ):
                    value = round(current_gray * 255)
                    data.append(value)

    # Validate recovered data length
    if len(data) < file_size:
        print("Error: Not enough encoded data found.")
        print(f"Expected: {file_size} bytes")
        print(f"Recovered: {len(data)} bytes")
        return

    # Trim to original file size
    data = data[:file_size]

    # Save recovered file
    output_file = filename

    # Avoid overwriting the original PDF
    if os.path.abspath(output_file) == os.path.abspath(input_file):
        output_file = "recovered_" + filename

    with open(output_file, "wb") as f:
        f.write(data)

    print("\nDecoding complete!")
    print(f"Recovered file: {output_file}")
    print(f"Recovered bytes: {len(data)}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 decoder.py <input.pdf>")
        return

    input_file = sys.argv[1]

    if not os.path.isfile(input_file):
        print("Error: PDF does not exist.")
        return

    try:
        decode(input_file)
    except Exception as error:
        print(f"Decoding failed: {error}")


if __name__ == "__main__":
    main()
