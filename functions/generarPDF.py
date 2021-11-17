from reportlab.pdfgen import canvas #Libreria para crear un archivo pdf

#Funcion para crear y un archivo pdf
#Canvas -> crea el archivo css
#drawString -> imprime en el pdf, parametros => posicion x, posicion y, contenido
#save -> funcion para guardar el pdf
def imprimir(dato,cedula):
    c = canvas.Canvas(f"./reportes/Empleado-{cedula}.pdf")
    c.drawString(100,690,f"NOMBRE: {dato[0]}")
    c.drawString(100,670,f"TELEFONO: {dato[1]}")
    c.drawString(100,650,f"CÓDIGO DE TRABAJADOR: {dato[2]}")
    c.drawString(100,630,f"INFORMACION BANCARIA: ****-****-****-****")
    c.drawString(100,610,f"INFORMACIÓN LABORAL:")
    c.drawString(150,590,f"HORAS TRABAJADAS: {dato[3]}")
    c.drawString(150,570,f"HORAS EXTRAS TRABAJADAS: {dato[4]}")
    c.drawString(150,550,f"HORAS NO TRABAJADAS: {dato[5]}")
    c.drawString(150,530,f"NÚMERO DE VENTAS: {dato[6]}")
    c.drawString(150,510,f"BONIFICACIONES: {dato[7]:,.2f}")
    c.drawString(150,490,f"ICBF : {dato[8]:,.2f}")
    c.drawString(150,470,f"PENSION: {dato[9]:,.2f}")
    c.drawString(100,450,f"SUELDO: $ {dato[10]:,.2f}")
    c.drawString(100,430,f"AUXILIO DE TRANSPORTE: $ {dato[11]:,.2f}")
    c.drawString(100,410,f"TOTAL A PAGAR: $ {dato[12]:,.2f}")
    c.save()