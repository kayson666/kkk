import os
import docx
from pathlib import Path

def convert_docx_to_txt(docx_path, txt_path):
    doc = docx.Document(docx_path)
    with open(txt_path, "w", encoding="utf-8") as txt_file:
        for paragraph in doc.paragraphs:
            paragraph_text = paragraph.text.replace('获取更多中医课程资料加微信 yqx2016h', '')
            paragraph_text = paragraph_text.replace('获取更多中医课程资料 加微信 yqx2016h', '')
            paragraph_text = paragraph_text.replace(' ', '')
            paragraph_text = paragraph_text.replace('读医书网制作整理请记住我们的域名：www.DuYiShu.Com', '')
            paragraph_text = paragraph_text.replace('为医学专业人士及健康需求人群提供优质试读本', '')

            txt_file.write(paragraph_text)

def batch_convert_word_to_txt(input_folder, output_folder):
    input_path = Path(input_folder)
    output_path = Path(output_folder)

    if not output_path.exists():
        output_path.mkdir()

    for docx_file in input_path.glob("*.docx"):
        txt_file = output_path / f"{docx_file.stem}.txt"
        convert_docx_to_txt(docx_file, txt_file)


input_folder = 'kkk'
output_folder = 'kkk'
batch_convert_word_to_txt(input_folder, output_folder)