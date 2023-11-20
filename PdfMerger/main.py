import PyPDF2 as P

pdfFiles = ['1.pdf', '2.pdf']

merger = P.PdfMerger()

for filename in pdfFiles:
    pdfFile = open(filename, 'rb')
    pdfReader = P.PdfReader(pdfFile)
    merger.append(pdfReader)
    pdfFile.close()
merger.write("merged.pdf")