from tkinter import *

raiz = Tk() # Crear la ventana principal
raiz.title("Primera interfaz") # Titulo de la ventana
raiz.resizable(1, 1) # Permitir redimensionar la ventana
raiz.iconbitmap(r"D:\Dev_Projects\VS Projects\cursoPython\triforce.ico") # Icono de la ventana
raiz.geometry("800x600") # Tamaño de la ventana
raiz.config(bg="cyan") # Color de fondo de la ventana
raiz.config(bd=20) # Bordes de la ventana
raiz.config(relief=GROOVE) # Estilo de borde de la ventana
raiz.config(cursor="pirate") # Cambiar el cursor al pasar por la ventana
frm = Frame(raiz, bg="blue") # Crear un marco dentro de la ventana
frm.pack() # Colocar el marco en la ventana
frm.config(bg="lavender") # Color de fondo del marco
frm.config(width=800, height=600) # Tamaño del marco
frm.config(bd=10) # Bordes del marco
frm.config(relief=SUNKEN) # Estilo de borde del marco
frm.config(cursor="hand2") # Cambiar el cursor al pasar por el marco
raiz.mainloop() # Iniciar el bucle de eventos de la ventana
# La ventana se cierra al hacer clic en la X