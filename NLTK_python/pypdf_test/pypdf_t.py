#coding:utf-8



if __name__ == '__main__':
    from pyPdf import PdfFileWriter, PdfFileReader
  
    pdf = PdfFileReader(file('EMNLP2013_RNTN.pdf', 'rb'))
    out = PdfFileWriter()
  
    for page in pdf.pages:
        page.mediaBox.upperRight = (580,800)
        page.mediaBox.lowerLeft = (128,232)
    out.addPage(page)
 
    ous = file('target.pdf', 'wb')
    
    out.write(ous)
    ous.close()
    pass