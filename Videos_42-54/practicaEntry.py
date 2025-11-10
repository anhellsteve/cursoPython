from tkinter import *

root = Tk() # Crea la ventana principal
#root.geometry("1280x720") # Tamaño de la ventana
miFrame = Frame(root, width=1280, height=720) # Crea un frame
miFrame.pack() # Lo empaqueta en la ventana principal
minombre = StringVar() # Variable para almacenar el nombre
# Para ordenar los elementos en el frame usaremos grid en vez de place
passLabel = Label(miFrame, text="Password:") # Crea una etiqueta con texto
passLabel.grid(row=0, column=0, padx=10, pady=10, sticky="w") # Coloca la etiqueta en el frame
nombreLabel = Label(miFrame, text="Nombre:") # Crea una etiqueta con texto
nombreLabel.grid(row=1, column=0, padx=10, pady=10, sticky="w") # Coloca la etiqueta en el frame
apellidoLabel = Label(miFrame, text="Apellido:") # Crea una etiqueta con texto
apellidoLabel.grid(row=2, column=0, padx=10, pady=10, sticky="w") # Coloca la etiqueta en el frame
direccionLabel = Label(miFrame, text="Dirección:") # Crea una etiqueta con texto
direccionLabel.grid(row=3, column=0, padx=10, pady=10, sticky="w") # Coloca la etiqueta en el frame
comentariosLabel = Label(miFrame, text="Comentarios:") # Crea una etiqueta con texto
comentariosLabel.grid(row=4, column=0, padx=10, pady=10, sticky="nw") # Coloca la etiqueta en el frame
# Entradas de texto 
passTexto = Entry(miFrame, show="*") # Crea un campo de entrada de texto
passTexto.grid(row=0, column=1, padx=10, pady=10) # Coloca el campo de entrada en <el frame
nombreTexto = Entry(miFrame, textvariable=minombre) # Crea un campo de entrada de texto
nombreTexto.grid(row=1, column=1, padx=10, pady=10) # Coloca el campo de entrada en el frame
nombreTexto.config(fg="red", justify="center") # Configura el color del texto y la alineación
apellidoTexto = Entry(miFrame) # Crea un campo de entrada de texto
apellidoTexto.grid(row=2, column=1, padx=10, pady=10) # Coloca el campo de entrada en el frame
direccionTexto = Entry(miFrame) # Crea un campo de entrada de texto
direccionTexto.grid(row=3, column=1, padx=10, pady=10) # Coloca el campo de entrada en el frame
comentariosTexto = Text(miFrame, width=16, height=5) # Crea un campo de texto
comentariosTexto.grid(row=4, column=1, padx=10, pady=10) # Coloca el campo de texto en el frame
scrollVert = Scrollbar(miFrame, command=comentariosTexto.yview) # Crea una barra de desplazamiento vertical
scrollVert.grid(row=4, column=2, sticky="nsew") # Coloca la barra de desplazamiento en el frame
comentariosTexto.config(yscrollcommand=scrollVert.set) # Configura la barra de desplazamiento para el campo de texto
def codigoBoton():
    minombre.set("Juan") # Establece el valor de la variable asociada al campo de texto nombreTexto
botonEnviar = Button(root, text="Enviar", command=codigoBoton) # Crea un botón
botonEnviar.pack() # Empaqueta el botón en la ventana principal
root.mainloop() # Mantiene la ventana abierta