import PyPDF2

def extract_pdf_page(input_pdf_path, output_pdf_path, page_number):
    with open(input_pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)

        if page_number < 1 or page_number > num_pages:
            raise ValueError("Invalid page number. Please select a valid page.")

        pdf_writer = PyPDF2.PdfWriter()
        pdf_writer.add_page(pdf_reader.pages[page_number - 1])

        with open(output_pdf_path, 'wb') as output_file:
            pdf_writer.write(output_file)

if __name__ == "__main__":
    input_pdf_path = input("Enter main pdf file name: ")
    output_pdf_path = input("Enter output pdf file name: ")
    page_number_to_extract = int(input("Enter a page number to extract: "))

    try:
        extract_pdf_page(input_pdf_path, output_pdf_path, page_number_to_extract)
        print(f"Page {page_number_to_extract} extracted and saved to {output_pdf_path}.")
    except Exception as e:
        print("Error:", e)
