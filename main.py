from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.shapes import Drawing
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import A4

doc = SimpleDocTemplate("graficoBarras.pdf", pagesize=A4)
guion = []

d = Drawing(400, 200)

datos = [
    (13, 14, 15, 16, 17, 18, 19),
    (3, 34, 6, 26, 17, 18, 9)
]

gbarras = VerticalBarChart()
gbarras.x = 50
gbarras.y = 50
gbarras.height = 125
gbarras.width = 300
gbarras.data = datos
gbarras.strokeColor = colors.black
gbarras.valueAxis.valueMin = 0
gbarras.valueAxis.valueMax = 60
gbarras.valueAxis.valueStep = 10
gbarras.categoryAxis.labels.boxAnchor = 'ne'
gbarras.categoryAxis.labels.dx = 8
gbarras.categoryAxis.labels.dy = -2
gbarras.categoryAxis.labels.angle = 30
gbarras.categoryAxis.categoryNames = ["Xan", "Feb", "Mar", "Abr", "Mai", "Xun","Xul","Ago"]
gbarras.groupSpacing = 30
gbarras.barSpacing = 2
d.add(gbarras)
guion.append(d)

doc.build(guion)