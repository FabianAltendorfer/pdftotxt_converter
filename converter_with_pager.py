import os
import PyPDF2

# Get a list of all PDF files in the current directory
pdf_files = [f for f in os.listdir() if f.endswith(".pdf")]

# Loop through each PDF file
for pdf_file in pdf_files:
    # Open the PDF file
    with open(pdf_file, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)

        # Create the output text file
        text_file = pdf_file[:-4] + ".txt"
        with open(text_file, "w", encoding="utf-8") as out_file:
            # Read each page of the PDF and write it to the text file
            for page in range(len(pdf_reader.pages)):
                page_text = pdf_reader.pages[page].extract_text()
                out_file.write(page_text + "\n\n" + "NEW PAGE" + "\n")
