from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.shapes import Drawing
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import A4

doc = SimpleDocTemplate("graficoUwU.pdf", pagesize=A4)
guion = []

d = Drawing(400, 200)

datos = [
    (50, 64, 14, 27, 87, 45, 8, 24, 36),
    (40, 6, 84, 72, 88, 41, 87, 26, 37),
    (5, 4, 1, 4, 81, 55, 85, 56, 45)
]

gbarras = VerticalBarChart()
gbarras.x = 50
gbarras.y = 50
gbarras.height = 200
gbarras.width = 300
gbarras.data = datos
gbarras.strokeColor = colors.black
gbarras.valueAxis.valueMin = 0
gbarras.valueAxis.valueMax = 100
gbarras.valueAxis.valueStep = 20
gbarras.categoryAxis.labels.boxAnchor = 'ne'
gbarras.categoryAxis.labels.dx = 8
gbarras.categoryAxis.labels.dy = -2
gbarras.categoryAxis.labels.angle = 0
gbarras.categoryAxis.categoryNames = ["Caca", "Culo", "Pedo", "Pis", "La", "Comida", "De" ,"Paris"]
gbarras.groupSpacing = 10
gbarras.barSpacing = 2
d.add(gbarras)
guion.append(d)

doc.build(guion)