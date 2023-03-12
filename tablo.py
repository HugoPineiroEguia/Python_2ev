from reportlab.platypus import (SimpleDocTemplate,
                                PageBreak,
                                Image,
                                Spacer,
                                Paragraph,
                                Table,
                                TableStyle)

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

doc = SimpleDocTemplate("tableExample.pdf", pageSize=4)
op = []

data = [('', 'Ventas', 'Compras'),
         ('Xaneiro', 300, 500),
         ('Febreiro', 2354, 6798),
         ('Marzo', 2354, -67980),
         ('Abril', 4577, 2355),
         ('Maio', 2346, 47568)]
table = Table(data, colWidths=100, rowHeights=30)
style = [
    # ('ATRIBUTO', DESDE(ROW=0,COL=1), HASTA(ROW=0,COL=-1), COLOR=colors.blue)
    ('TEXTCOLOR', (0, 1), (0, 5), colors.blue),
    ('TEXTCOLOR', (1, 1), (2, 5), colors.red),
    ('TEXTCOLOR', (1, 0), (2, 0), colors.green),
    ('BACKGROUND', (1, 1), (-1, -1), colors.lightcyan),
    ('BOX', (1, 1), (-1, -1), 1.5, colors.lightgrey),
    ('INNERGRID', (1, 1), (-1, -1), 1, colors.black),
    ('VALING', (0, 0), (-1, -1), 'MIDDLE')
]

for r, row in enumerate(data):
    for v, value in enumerate(row):
        if type(value) == int:
            if value > 0:
                style.append(('BACKGROUND', (v, r), (v, r), colors.lightgreen))
            else:
                style.append(('BACKGROUND', (v, r), (v, r), colors.lightpink))

table.setStyle(style)
op.append(table)

doc.build(op)