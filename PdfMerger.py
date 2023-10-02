import PyPDF2


pdf_files = ["1.pdf", "2.pdf"]

merger = PyPDF2.PdfMerger()


for filename in pdf_files:
    with open(filename, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file) 
        merger.append(pdf_reader)

with open("merged.pdf", "wb") as merged_file:
    merger.write(merged_file)

 
