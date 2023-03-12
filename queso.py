from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.shapes import Drawing
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import A4

from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.charts.legends import Legend

doc = SimpleDocTemplate("graficoQueso.pdf", pagesize=A4)
guion = []

d = Drawing(400, 200)

#GRAPHIC

gQueso = Pie()
d.add(gQueso)
gQueso.x = 60
gQueso.y = 15
gQueso.width = 170
gQueso.height = 170
gQueso.data = [10,20,30,40,50]
gQueso.labels = ["Edge", "Brave", "Safari", "Firefox", "Chrome"]


gQueso.slices.strokeWidth = 0.5
gQueso.slices[3].popout = 10
gQueso.slices[3].strokeWidth = 2
gQueso.slices[3].strokeDashArray = [2,2]
gQueso.slices[3].labelRadius = 1.75
gQueso.slices[3].fontColor = colors.red
gQueso.sideLabels = 1

guion.append(d)

#LEGEND

lenda = Legend()
lenda.x = 378
lenda.y = 9
lenda.dx = 8
lenda.dy = 8
lenda.fontName = 'Helvetica'
lenda.fontSize = 7
lenda.boxAnchor = 'n'
lenda.columnMaximum = 10
lenda.strokeWidth = 1
lenda.strokeColor = colors.black
lenda.deltax = 75
lenda.deltay = 10
lenda.autoXPadding = 5
lenda.yGap = 0
lenda.dxTextSpace = 5
lenda.alignment = 'right'
lenda.dividerLines = 1|2|4
lenda.dividerOffsY = 4.5
lenda.subCols.rpad = 30
colores = [colors.blue, colors.red, colors.green, colors.yellow, colors.pink]

for i, color in enumerate(colores):
    gQueso.slices[i].fillColor = color

    lenda.colorNamePairs = [(
        gQueso.slices[i].fillColor, (gQueso.labels[i][0:20], '%0.2f' % gQueso.data[i])
    )for i in range(len(gQueso.data))
    ]

d.add(lenda)
doc.build(guion)