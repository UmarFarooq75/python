import PyPDF2

def Merger_PDF(pdfiles):
    merger=PyPDF2.PdfMerger()
    for filename in pdfiles:
        pdFile=open(filename,'rb')
        pdfReader=PyPDF2.PdfReader(pdFile)
        merger.append(pdfReader)
    pdFile.close()
    merger.write('merged.pdf')
    
if __name__ == "__main__":
    print("            Welcome to PDF-Merger Program")
    pdfiles=['1.pdf','2.pdf']
    Merger_PDF(pdfiles)