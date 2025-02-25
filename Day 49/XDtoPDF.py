import xml.etree.ElementTree as ET
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def xd_to_pdf(xd_file, pdf_file):
    tree = ET.parse(xd_file)
    root = tree.getroot()

    c = canvas.Canvas(pdf_file, pagesize=letter)
    width, height = letter

    y = height - 40
    for child in root:
        c.drawString(40, y, f"{child.tag}: {child.text}")
        y -= 20

    c.save()

xd_to_pdf('Java-OOP-Project.xd', 'output.pdf')
