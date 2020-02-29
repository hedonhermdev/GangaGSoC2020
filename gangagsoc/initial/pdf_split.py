import os
from PyPDF2 import PdfFileWriter, PdfFileReader


if not os.path.exists("./cern-pages"):
    os.mkdir("cern-pages")

with open("./CERN.pdf", "rb") as pdf_file:
    pdf = PdfFileReader(pdf_file)

    num_pages = pdf.numPages

    for i in range(num_pages):
        output = PdfFileWriter()
        output.addPage(pdf.getPage(i))
        with open(f"cern-pages/page-{i}.pdf", "wb") as pdf_file:
            output.write(pdf_file)

    print("Successfully extracted PDF file into %d pages" % num_pages)
