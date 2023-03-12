from reportlab.pdfgen import canvas

aux =  canvas.Canvas("imagen.pdf")

aux.drawString(0, 0, "Me gusta la cuca")
aux.drawString(50, 100, "a mi el pico")
aux.drawString(150, 500, "Y a mi la mismisima poronga")

aux.drawImage("/home/oracle/Descargas/xd.jpg", 200,200,225,225)

aux.showPage()
aux.save()