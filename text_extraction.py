import requests
import PyPDF2


def extract_text_from_pdf(url):
    # Download and save the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Read the PDF and extract its text content
    pdf_file = open('temp.pdf', 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    text = ""
    for page in range(pdf_reader.numPages):
        text += pdf_reader.getPage(page).extract_text()

    # Close the PDF file
    pdf_file.close()

    # Return the extracted text
    return text


# PDF URL
pdf_url = 'https://arxiv.org/pdf/2307.03171'

# Extract text from the PDF
text = extract_text_from_pdf(pdf_url)

# Save the extracted text to a file
output_file = 'output.txt'
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(text)

print(f'Text saved to {output_file}')
