import tkinter, my_first_bot

# Crea objeto de tkinter
ventana = tkinter.Tk()
ventana.geometry("400x300")
ventana.title("My Bot App")
ventana.iconbitmap("./hola.ico")

# Crea 1er botón
boton_paint = tkinter.Button(ventana, text = "ABRE PAINT", command = my_first_bot.abrepaint)
boton_paint.pack()

# Crea 2do botón
boton_youtube = tkinter.Button(ventana, text = "ABRE YOUTUBE", command = my_first_bot.abreyoutube)
boton_youtube.pack()

boton_googledocs = tkinter.Button(ventana, text = "ABRE Documento de Google", command = my_first_bot.documentogoogle)
boton_googledocs.pack()

# Loop de ejecución
ventana.mainloop()
