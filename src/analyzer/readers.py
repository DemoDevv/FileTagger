import pypdf
import docx
import pptx
import pandas as pd

def pdf_reader(file_path):
    with open(file_path, "rb") as file:
        reader = pypdf.PdfReader(file)
        return " ".join(
            page.extract_text() for page in reader.pages
        )


def docx_reader(file_path):
    doc = docx.Document(file_path.__str__())
    return " ".join(paragraph.text for paragraph in doc.paragraphs)


def doc_reader(file_path):
    pass


def xlsx_reader(file_path):
    df = pd.read_excel(file_path)
    return " ".join(df.astype(str).values.flatten())


def pptx_reader(file_path):
    prs = pptx.Presentation(file_path.__str__())

    text_buffer = []

    for slide in prs.slides:
        for shape in slide.shapes:
            if not shape.has_text_frame:
                continue
            for paragraph in shape.text_frame.paragraphs: # type: ignore
                for run in paragraph.runs:
                    text_buffer.append(run.text)

    return " ".join(text_buffer)


def txt_reader(file_path):
    with open(
        file_path, "r", encoding="utf-8", errors="ignore"
    ) as file:
        return file.read()
