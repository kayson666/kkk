import os
import subprocess
import pdfplumber

def caj_to_pdf(caj_file_path, output_pdf_path, temp_pdf_path):
    caj2pdf_tool_path = '/home/sunzhaoyang/PycharmProjects/kkk-main/caj2pdf/caj2pdf'
    subprocess.run(["python3", caj2pdf_tool_path, "convert", caj_file_path, "-o", temp_pdf_path])
    os.rename(temp_pdf_path, output_pdf_path)

def batch_convert(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.endswith('.caj'):
                input_file_path = os.path.join(root, file)
                pdf_file_path = os.path.join(output_dir, f'{os.path.splitext(file)[0]}.pdf')
                temp_pdf_file_path = os.path.join(output_dir, f'{os.path.splitext(file)[0]}.pdf.tmp')
                txt_file_path = os.path.join(output_dir, f'{os.path.splitext(file)[0]}.txt')

                # Convert CAJ to PDF
                caj_to_pdf(input_file_path, pdf_file_path, temp_pdf_file_path)
                # Convert PDF to TXT
                pdf_to_txt(pdf_file_path, txt_file_path)

def pdf_to_txt(pdf_file_path, output_txt_path):
    with pdfplumber.open(pdf_file_path) as pdf:
        with open(output_txt_path, 'w', encoding='utf-8') as output_file:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    output_file.write(text)
                    output_file.write('\n')


input_dir = '/home/sunzhaoyang/PycharmProjects/kkk-main/kkk/现代文本/论文集/中医杂志/知网论文'
output_dir = '/home/sunzhaoyang/PycharmProjects/kkk-main/kkk/现代文本/论文集/中医杂志/知网论文'
batch_convert(input_dir, output_dir)
