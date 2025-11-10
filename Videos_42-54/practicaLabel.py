from tkinter import *
root = Tk() # Crea la ventana principal
miFrame = Frame(root, width=500, height=400) # Crea un frame
miFrame.pack() # Lo empaqueta en la ventana principal
miImagen = PhotoImage(file="D:\Dev_Projects\VS Projects\cursoPython\gir.png")
miLabel = Label(miFrame, image=miImagen) # Crea una etiqueta con la imagen
miLabel.place(x=0, y=0) # Coloca la etiqueta en el frame
Label(miFrame, text="Hola Mundo", fg="green", font=("Cambria",18)).place(x=450/2, y=350/2) # Crea una etiqueta con texto con un color y fuente
root.mainloop()