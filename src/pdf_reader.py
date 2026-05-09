from pypdf import PdfReader


def read_pdf(file_path):
    """
    Extract text content from a PDF file.

    Parameters:
        file_path (str): Path to PDF file

    Returns:
        str: Extracted text
    """

    reader = PdfReader(file_path)
    text = ""

    # Iterate through all pages
    for page in reader.pages:
        content = page.extract_text()

        # Skip pages with no text
        if content:
            text += content + "\n"

    return text