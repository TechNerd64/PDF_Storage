# Act as a general wrapper for the project. This file will be used to run the project and will be the main entry point for the project.
import os
import sys
import encoder
import decoder

def main():

    if len(sys.argv) != 3:
        print("Usage:")
        print("  python3 main.py encode <input_file>")
        print("  python3 main.py decode <input.pdf>")
        return

    operation = sys.argv[1].lower()
    input_file = sys.argv[2]

    # Validate input
    if not os.path.isfile(input_file):
        print(f"Error: File '{input_file}' does not exist.")
        return

    try:

        if operation == "encode":
            encoder.encode(input_file)

        elif operation == "decode":
            decoder.decode(input_file)

        else:
            print(f"Unknown operation: {operation}")
            print("Available operations: encode, decode")

    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
