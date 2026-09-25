from pathlib import Path

from pypdf import PdfReader
from docx import Document


def extract_pdf(path):

    reader = PdfReader(
        str(path)
    )

    pages = []

    for page in reader.pages:

        text = page.extract_text()

        if text:
            pages.append(text)

    return "\n".join(pages)


def extract_docx(path):

    document = Document(
        str(path)
    )

    return "\n".join(
        paragraph.text
        for paragraph in document.paragraphs
    )


def extract_text(path):

    # Defend against paths pasted with surrounding quotes
    # (e.g. copied from Windows Explorer or a quoted terminal arg).
    if isinstance(path, str):
        path = path.strip().strip('"').strip("'")

    path = Path(path)

    extension = path.suffix.lower()

    if extension == ".pdf":
        return extract_pdf(path)

    if extension == ".docx":
        return extract_docx(path)

    if extension == ".txt":
        return path.read_text(
            encoding="utf-8"
        )

    raise ValueError(
        "Only PDF, DOCX and TXT are supported."
    )
