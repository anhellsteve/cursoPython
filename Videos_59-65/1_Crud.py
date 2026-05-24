from tkinter import *
from tkinter import messagebox
import sqlite3


root = Tk()
root.title("CRUD con SQLite")
fieldFrame= Frame(root)
fieldFrame.pack()
btnFrame= Frame(root)
btnFrame.pack()
index = 0
usuarios = []

# FUNCIONES
# Conexión a la base de datos
def conexionBBDD():
    conn = sqlite3.connect("Usuarios.db")
    cursor = conn.cursor()
    try:
        cursor.execute('''
            CREATE TABLE USUARIOS (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE VARCHAR(50),
                APELLIDO VARCHAR(50),
                DIRECCION VARCHAR(100),
                EMAIL VARCHAR(100),
                COMENTARIOS TEXT
            )
        ''')
        conn.commit()
        messagebox.showinfo("BBDD", "Base de datos creada con éxito.")
    except sqlite3.OperationalError:
        messagebox.showwarning("BBDD", "La base de datos ya existe.")
    finally:
        conn.close()

# Función para borrar campos
def clearFields():
    ide.config(state="normal")
    ide.delete(0, END)
    ide.config(state="readonly")
    name.delete(0, END)
    lastname.delete(0, END)
    address.delete(0, END)
    email.delete(0, END)
    comments.delete("1.0", END)

# Función para crear un nuevo usuario
def createUser():
    conn = sqlite3.connect("Usuarios.db")
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO USUARIOS (NOMBRE, APELLIDO, DIRECCION, EMAIL, COMENTARIOS)
        VALUES (?, ?, ?, ?, ?)
    ''', (name.get(), lastname.get(), address.get(), email.get(), comments.get("1.0", END)))
    conn.commit()
    conn.close()
    messagebox.showinfo("Usuario", "Usuario creado con éxito.")
    clearFields()

# Función para leer un usuario
def readUser():
    global usuarios
    conn = sqlite3.connect("Usuarios.db")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM USUARIOS')
    usuarios = cursor.fetchall()
    conn.commit()
    conn.close()
    showUser()

# funcion para mostrar usuarios
def showUser():
    global usuarios
    global index
    user = usuarios[index]
    if user:
        clearFields()
        ide.config(state="normal")
        ide.delete(0, END)
        ide.insert(0, user[0])
        ide.config(state="readonly")
        name.delete(0, END)
        name.insert(0, user[1])
        lastname.delete(0, END)
        lastname.insert(0, user[2])
        address.delete(0, END)
        address.insert(0, user[3])
        email.delete(0, END)
        email.insert(0, user[4])
        comments.delete("1.0", END)
        comments.insert("1.0", user[5])
    else:
        messagebox.showwarning("Usuario", "No hay usuarios para mostrar.")

# Funcion para ver el siguiente usuario
def nextUser():
    global index
    if index < len(usuarios) - 1:
        index += 1
        showUser()
    else:
        messagebox.showinfo("Usuario", "No hay más usuarios para mostrar.")

# Funcion para ver el usuario anterior
def previousUser():
    global index
    if index > 0:
        index -= 1
        showUser()
    else:
        messagebox.showinfo("Usuario", "No hay usuarios anteriores para mostrar.")

# Función para actualizar un usuario
def updateUser():
    conn = sqlite3.connect("Usuarios.db")
    cursor = conn.cursor()
    if ide.get():
        cursor.execute('''
            UPDATE USUARIOS
            SET NOMBRE = ?, APELLIDO = ?, DIRECCION = ?, EMAIL = ?, COMENTARIOS = ?
            WHERE ID = ?
        ''', (name.get(), lastname.get(), address.get(), email.get(), comments.get("1.0", END), ide.get()))
        conn.commit()
        conn.close()
        messagebox.showinfo("Usuario", "Usuario actualizado con éxito.")
        clearFields()
    else:
        messagebox.showwarning("Usuario", "No hay usuario seleccionado para actualizar.")

# Función para borrar un usuario
def deleteUser():
    conn = sqlite3.connect("Usuarios.db")
    cursor = conn.cursor()
    if ide.get():
        cursor.execute('DELETE FROM USUARIOS WHERE ID = ?', (ide.get(),))
        conn.commit()
        conn.close()
        messagebox.showinfo("Usuario", "Usuario borrado con éxito.")
        clearFields()
    else:
        messagebox.showwarning("Usuario", "No hay usuario seleccionado para borrar.")

# Salida de la aplicación
def exitApp():
    if messagebox.askokcancel("Salir", "¿Deseas salir de la aplicación?"):
        root.destroy()

# Menu
menuBar = Menu(root)
root.config(menu=menuBar, width=300, height=300)

# Submenú BBDD
bbddMenu = Menu(menuBar, tearoff=0)
bbddMenu.add_command(label="Conectar", command=conexionBBDD)
bbddMenu.add_command(label="Salir", command=exitApp)

# Submenú Borrar
borrarMenu = Menu(menuBar, tearoff=0)
borrarMenu.add_command(label="Borrar campos", command=clearFields)

# Submenú CRUD
crudMenu = Menu(menuBar, tearoff=0)
crudMenu.add_command(label="Crear", command=createUser)
crudMenu.add_command(label="Leer", command=readUser)
crudMenu.add_command(label="Actualizar", command=updateUser)
crudMenu.add_command(label="Borrar", command=deleteUser)

# Submenú Ayuda
ayudaMenu = Menu(menuBar, tearoff=0)
ayudaMenu.add_command(label="Acerca de...")

# Menu principal
menuBar.add_cascade(label="BBDD", menu=bbddMenu)
menuBar.add_cascade(label="Borrar", menu=borrarMenu)
menuBar.add_cascade(label="CRUD", menu=crudMenu)
menuBar.add_cascade(label="Ayuda", menu=ayudaMenu)


# Etiquetas y campos de entrada
idLbl = Label(fieldFrame, text="ID:")
idLbl.grid(row=0, column=0, padx=10, pady=10)
ide = Entry(fieldFrame, state="readonly")
ide.grid(row=0, column=1, padx=10, pady=10)
nameLbl = Label(fieldFrame, text="Nombre:")
nameLbl.grid(row=1, column=0, padx=10, pady=10)
name = Entry(fieldFrame)
name.grid(row=1, column=1, padx=10, pady=10)
lastnameLbl = Label(fieldFrame, text="Apellido:")
lastnameLbl.grid(row=2, column=0, padx=10, pady=10)
lastname = Entry(fieldFrame)
lastname.grid(row=2, column=1, padx=10, pady=10)
addressLbl = Label(fieldFrame, text="Dirección:")
addressLbl.grid(row=3, column=0, padx=10, pady=10)
address = Entry(fieldFrame)
address.grid(row=3, column=1, padx=10, pady=10)
emailLbl = Label(fieldFrame, text="Email:")
emailLbl.grid(row=4, column=0, padx=10, pady=10)
email = Entry(fieldFrame)
email.grid(row=4, column=1, padx=10, pady=10)
commentsLbl = Label(fieldFrame, text="Comentarios:")
commentsLbl.grid(row=5, column=0, padx=10, pady=10)
comments= Text(fieldFrame, width=16, height=5)
comments.grid(row=5, column=1, padx=10, pady=10)
scrollVert = Scrollbar(fieldFrame, command=comments.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")
comments.config(yscrollcommand=scrollVert.set)
previousBtn = Button(btnFrame, text = "Anterior", command=previousUser)
previousBtn.grid(row=6, column=1, padx=10, pady=10)
nextBtn = Button(btnFrame, text = "Siguiente", command=nextUser)
nextBtn.grid(row=6, column=2, padx=10, pady=10)
createBtn = Button(btnFrame, text = "Crear", command=createUser)
createBtn.grid(row=7, column=0, padx=10, pady=10)
readBtn = Button(btnFrame, text = "Leer", command=readUser)
readBtn.grid(row=7, column=1, padx=10, pady=10)
updateBtn = Button(btnFrame, text = "Actualizar", command=updateUser)
updateBtn.grid(row=7, column=2, padx=10, pady=10)
deleteBtn = Button(btnFrame, text = "Borrar", command=deleteUser)
deleteBtn.grid(row=7, column=3, padx=10, pady=10)

root.mainloop()