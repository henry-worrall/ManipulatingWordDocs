import sys
import os
import comtypes.client

wdFormatPDF = 17

in_file = os.path.abspath("template_doc.docx")
out_file = os.path.abspath("C:/Users/hworr/Documents/GitHub/ManipulatingWordDocs/output.pdf")

word = comtypes.client.CreateObject('Word.Application', dynamic = True)
word.Visible = False
word.Documents.Open(in_file)
word.Documents[0].SaveAs(out_file, wdFormatPDF)
word.Documents[0].SaveAs()
word.Documents[0].Close()
word.Quit()
