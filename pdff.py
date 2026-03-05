import sys
import os
from PyPDF2 import PdfMerger, PdfReader


def main():
    # STEP 1 & 2 — Read output filename from command line
    if len(sys.argv) < 2:
        print("Error: Merge file name not specified.")
        print("Usage: python pdf.py filename")
        sys.exit(1)

    output_name = sys.argv[1] + ".pdf"
    output_text_option = False

    # BONUS OPTION CHECK
    if len(sys.argv) > 2 and sys.argv[2] == "--extract":
        output_text_option = True

    # STEP 3 — Initialize merger object
    merger = PdfMerger()

    # STEP 4 — Retrieve files from current directory
    files = os.listdir(".")

    # STEP 5 — Filter only PDF files
    pdf_files = [file for file in files if file.lower().endswith(".pdf")]

    # STEP 6 — Sort alphabetically
    pdf_files.sort()

    # Remove output file if it already exists (avoid merging into itself)
    pdf_files = [file for file in pdf_files if file != output_name]

    # STEP 7 — Report to user
    print(f"\nPDF files found: {len(pdf_files)}")
    print("List:\n")

    for file in pdf_files:
        print(file)

    # If no files found, exit
    if len(pdf_files) == 0:
        print("\nNo PDF files found to merge.")
        sys.exit(0)

    # STEP 8 — Prompt user
    choice = input("\nContinue (y/n): ").strip().lower()

    if choice != "y":
        print("Operation cancelled.")
        sys.exit(0)

    # STEP 9 — Append PDFs
    for pdf in pdf_files:
        try:
            merger.append(pdf)
        except Exception as e:
            print(f"Error merging {pdf}: {e}")

    # STEP 10 — Export merged file
    try:
        merger.write(output_name)
        merger.close()
        print(f"\nMerged file saved as: {output_name}")
    except Exception as e:
        print(f"Error saving merged file: {e}")
        sys.exit(1)

    # BONUS STEP — Extract text
    if output_text_option:
        try:
            reader = PdfReader(output_name)
            text_content = ""

            for page in reader.pages:
                extracted = page.extract_text()
                if extracted:
                    text_content += extracted + "\n"

            text_filename = sys.argv[1] + ".txt"

            with open(text_filename, "w", encoding="utf-8") as text_file:
                text_file.write(text_content)

            print(f"Extracted text saved as: {text_filename}")

        except Exception as e:
            print(f"Error extracting text: {e}")


if __name__ == "__main__":
    main()