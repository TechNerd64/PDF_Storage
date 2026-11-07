# PDF Storage

PDF Storage encodes information into a PDF so it can be stored or shared as a document. The decoder is designed to perform the inverse operation and recover the original information.

## Encoding and decoding

- **Encoder:** Accepts source data, transforms it into the project's encoded representation, and writes that representation to a PDF.
- **Decoder:** Will read the encoded representation from a PDF and apply the inverse transformation to reconstruct the source data.

For successful round trips, both sides must agree on the representation and transformation rules. The decoder should therefore mirror the encoder's format, interpreting the PDF content in the same order and reversing each encoding step.

## Usage

Use the encoder's supported inputs and options to create a PDF. Once implemented, the decoder will accept that PDF and produce the recovered data. Refer to the encoder's source code for the exact format and invocation details.

Use "python3 encoder.py <input_file>" to encode your file into a PDF.

To decode, simply use "python3 decoder.py <input_pdf>" to decode and spawn a copy of your original encoded file.

## Status

The encoder establishes the PDF format. The decoder is expected to follow the corresponding reverse process.
