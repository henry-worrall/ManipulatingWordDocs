from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter
from copy import deepcopy

pdf_path = Path('output.pdf')

pdf_reader = PdfFileReader(str(pdf_path)) # may need strict=False argument
pdf_writer = PdfFileWriter()

page0 = deepcopy(pdf_reader.getPage(0))
pdf_writer.addPage(page0)

# rotate page clockwise
page1 = deepcopy(pdf_reader.getPage(0))
page1.rotateClockwise(90)
pdf_writer.addPage(page1)

# rotate page anticlockwise
page2 = deepcopy(pdf_reader.getPage(0))
page2.rotateCounterClockwise(90)
pdf_writer.addPage(page2)

# Set page3 to be rotated by 90 degrees clockwise
page3 = deepcopy(pdf_reader.getPage(0))
page3.rotateCounterClockwise(90)

# logic to test if page is rotated by 90
try:
    if page3['/Rotate'] == 90:
        page3.rotateClockwise(90)
        print('Page 3 was 90 clockwise.')
except Exception as e: # if the page isn't rotated, then the pageobject won't have the key '/Rotate' so it will return a KeyError: '/Rotate'.
    # This error can be seen is you comment out line 25.
    print(f'Error: {e}')
pdf_writer.addPage(page3)

# save the output of the pdf file writer
with Path("Name of new output file.pdf").open(mode="wb") as output_file: # EDIT output file name and location
    pdf_writer.write(output_file)
