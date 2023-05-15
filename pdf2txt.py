import fitz  # PyMuPDF
import os

# Directory containing the PDF files
pdf_dir = '/home/sunzhaoyang/PycharmProjects/kkk-main/kkk/现代文本/论文集/中华中医药学刊'

# Directory to save the txt files
txt_dir = '/home/sunzhaoyang/PycharmProjects/kkk-main/kkk/现代文本/论文集/中华中医药学刊/中华中医药学刊txt'

# List all files in the directory
files = os.listdir(pdf_dir)

# Filter out all the PDF files
pdf_files = [file for file in files if file.endswith('.pdf')]

# List of keywords to remove
keywords = ['中医杂志', '通讯作者', '基金项目', '中华中医药杂志', '中华中医药学刊']

# Loop through all the PDF files
for pdf_file in pdf_files:
    # Open the PDF file
    doc = fitz.open(os.path.join(pdf_dir, pdf_file))

    # Extract the text
    text = ""
    for i in range(len(doc)):
        page = doc.load_page(i)
        text += page.get_text("text")
    text = text.replace(' ', '')
    ref_keywords = ['参考文献', '参 考 文 献', '参\n考\n文\n献']

    # Remove the text after reference keywords
    for ref_keyword in ref_keywords:
        index = text.find(ref_keyword)
        if index != -1:
            text = text[:index]

    # Remove lines containing the keywords
    lines = text.split('\n')
    lines = [line for line in lines if not any(keyword in line for keyword in keywords)]
    text = '\n'.join(lines)

    # Save the text to a txt file
    txt_file = pdf_file.replace('.pdf', '.txt')
    with open(os.path.join(txt_dir, txt_file), 'w', encoding='utf-8') as f:
        f.write(text)
