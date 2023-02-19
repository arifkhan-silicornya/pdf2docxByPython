from pdf2docx import Converter

pdf_file_path = 'MD-Arif-Khan-cover.pdf'

docx_file_path = 'output.docx'

c = Converter(pdf_file_path)

c.convert(docx_file_path)

c.close()