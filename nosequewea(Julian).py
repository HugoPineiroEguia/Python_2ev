import os.path

from reportlab.platypus import Paragraph
from reportlab.platypus import Image
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Spacer

from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors


class MineParagraphStyle(ParagraphStyle):
    def __init__(self):
        super().__init__(self, fontSize=18,
                         font="Helvetica",
                         textColor="Blue")


style_sheet = getSampleStyleSheet()

op = []

header = style_sheet["Heading4"]
header.pageBreakBefore = 1
header.keepWithNext = 1
header.backColor = colors.paleturquoise

paragarph = Paragraph("Docs header", header)
op.append(paragarph)

chainText = """Texto de contido de paragrafo que imos repetir unhas cantas veces. """
sampleText = style_sheet['BodyText']
paragarph2 = Paragraph(chainText * 500, sampleText)
op.append(paragarph2)
op.append(Spacer(0, 20))

image_file = "/home/oracle/Descargas/xd.jpg"
image = Image(os.path.realpath(image_file))
op.append(image)

paragarph3 = Paragraph(chainText * 5, MineParagraphStyle())
op.append(paragarph3)

doc = SimpleDocTemplate("Platypus(Julian).pdf", pagesize=A4, showBoundary=1)
doc.build(op)