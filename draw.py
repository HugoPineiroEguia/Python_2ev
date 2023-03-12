
from reportlab.graphics.shapes import Image, Drawing
from reportlab.graphics import renderPDF
from reportlab.lib.pagesizes import A4

op = []

img = Image(250, 0, 400, 400, "/home/oracle/Descargas/xd.jpg")

draw = Drawing(30, 30)
draw.add(img)
draw.translate(0, 400)
op.append(draw)

draw2 = Drawing(30, 30)
draw2.add(img)
draw2.rotate(30)
draw2.scale(0.5, 0.5)
op.append(draw2)

draw3 = Drawing(A4[0], A4[1])
for img in op:
    draw3.add(img)
renderPDF.drawToFile(draw3, "Draw(Julian).pdf")

"""
Este código genera un archivo PDF que contiene dos imágenes en diferentes posiciones y escalas, utilizando la librería ReportLab.

Primero, se define una lista llamada op, donde se guardarán las imágenes. Luego se crea un objeto Image con las dimensiones y ubicación de la imagen que se quiere agregar (en este caso, "/home/dam2a/Imágenes/Marta.jpg").

A continuación, se crea un objeto Drawing llamado draw, se le añade la imagen y se traslada hacia arriba. Este objeto se agrega a la lista op.

Luego se crea otro objeto Drawing llamado draw2, se le añade la misma imagen, se rota 30 grados y se escala a la mitad. Este objeto también se agrega a la lista op.

Finalmente, se crea un tercer objeto Drawing llamado draw3 con el tamaño de página A4 y se agrega cada uno de los objetos Drawing anteriores a él mediante un bucle for. Se utiliza renderPDF.drawToFile para exportar el resultado a un archivo PDF llamado "Draw(Julian).pdf".
"""