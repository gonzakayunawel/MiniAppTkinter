import tkinter, my_first_bot

# Crea objeto de tkinter
ventana = tkinter.Tk()
ventana.geometry("400x300")
ventana.title("My Bot App")
ventana.iconbitmap("./hola.ico")

# Crea 1er botón
boton0 = tkinter.Button(ventana, text = "ABRE PAINT", command = my_first_bot.abrepaint)
boton0.pack()

# Crea 2do botón
boton1 = tkinter.Button(ventana, text = "ABRE YOUTUBE", command = my_first_bot.abreyoutube)
boton1.pack()

boton2 = tkinter.Button(ventana, text = "ABRE Documento de Google", command = my_first_bot.documentogoogle)
boton2.pack()

# Loop de ejecución
ventana.mainloop()
