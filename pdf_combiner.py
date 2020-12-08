"""
This script allows you to combine pages of different pdfs together and save as a new pdf file. The for loop allows for multiple pages of one document to be copied and added for speed. This has been useful for me when signing contracts.
"""

from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

#locations of files to be used
pdf_path1 = Path('route/to/input_file1.pdf') #EDIT PATHS
pdf_path2 = Path('route/to/input_file2.pdf')
pdf_path3 = Path('route/to/input_file3.pdf')

# allow those files to be read by the PyPDF2 package
input_pdf1 = PdfFileReader(str(pdf_path1),strict=False) #N.B. this returns an error when strict=True
input_pdf2 = PdfFileReader(str(pdf_path2),strict=False)
input_pdf3= PdfFileReader(str(pdf_path3),strict=False)

#define individual pages
page1 = input_pdf3.getPage(0) #EDIT pages
page2 = input_pdf1.getPage(0)
page12 = input_pdf2.getPage(0)

#define the PyPDF2 package file writer
pdf_writer = PdfFileWriter()

#write individual pages
pdf_writer.addPage(page1) #EDIT pages
pdf_writer.addPage(page2)

# write multiple sequential pages
for n in range(2,11): # EDIT and copy range of pages
    page = input_pdf3.getPage(n)
    pdf_writer.addPage(page)

#write individual pages
pdf_writer.addPage(page12) #EDIT pages

# save the output of the pdf file writer
with Path("Name of output file.pdf").open(mode="wb") as output_file: # EDIT output file name and location
    pdf_writer.write(output_file)
