import os
import re
import pdfplumber
from docx import Document

def clean_text(text):
    # 移除非打印字符（ASCII 0-31 和 127）
    text = re.sub(r"[\x00-\x1F\x7F]", " ", text)
    return text

def pdf_to_word(pdf_file, word_file):
    with pdfplumber.open(pdf_file) as pdf:
        doc = Document()

        for page in pdf.pages:
            text = page.extract_text()
            if text:
                text = clean_text(text)
                doc.add_paragraph(text)

        doc.save(word_file)

def batch_convert(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(input_folder, filename)
            word_filename = os.path.splitext(filename)[0] + ".docx"
            word_path = os.path.join(output_folder, word_filename)
            pdf_to_word(pdf_path, word_path)

input_folder = "kkk/论文"
output_folder = "kkk/论文"
batch_convert(input_folder, output_folder)
