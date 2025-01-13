from fpdf import FPDF
import webbrowser

def pdfMaker() :
    # create FPDF object
    # Layout ('P' , 'L')
    # Unit ('mm', 'cm', 'in')
    # format ('A3', 'A4' (default), 'AS', 'Letter', 'Legal', (100,150)
    pdf = FPDF('P', 'mm', 'Letter')

    # Add a page
    pdf.add_page()

    #specify font
    # fonts ('times', 'courier', 'helvetica', 'symbol', 'zpfdingbats')
    # 'B' (bold), 'U' (underline), 'I' (italics), '' (regular), combination (ie , ('BU'))
    pdf.set_font('helvetica', '', 16)

    # Add text
    # w = width
    # h = height
    pdf.cell(40,10, 'Hello World !')
    pdf.output('pythonPDF.pdf')
    get_url = webbrowser.open('file:///Users/lathan/Documents/Python/PDFmaker/pythonPDF.pdf')

pdfMaker()