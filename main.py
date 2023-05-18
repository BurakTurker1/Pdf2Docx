from pdf2docx import Converter

pdf_file="input.pdf"#pdf dosyası
docx_file="output.docx"#docx dosyası
cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()
