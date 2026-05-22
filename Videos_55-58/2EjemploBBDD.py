import sqlite3

miConexion = sqlite3.connect("GestionProductos")
miCursor = miConexion.cursor()

#miCursor.execute('''CREATE TABLE IF NOT EXISTS PRODUCTOS (
#    CODIGO_ARTICULO VARCHAR(5) PRIMARY KEY, 
#    NOMBRE_ARTICULO VARCHAR(50), 
#    PRECIO INTEGER, 
#    SECCION VARCHAR(20))''')

'''productos =[
    ("AR01", "Balon", 20, "Jugueteria"),
    ("AR02", "Pantalon", 15, "Confeccion"),
    ("AR03", "Destornillador", 20, "Ferreteria"),
    ("AR04", "Jarron", 45, "Ceramica")
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?,?)", productos)'''

#miCursor.execute("INSERT INTO PRODUCTOS VALUES ('AR05', 'tren', 15, 'Jugueteria')")

#miCursor.execute('''CREATE TABLE IF NOT EXISTS PRODUCTOS (
#    ID INTEGER PRIMARY KEY AUTOINCREMENT, 
#    NOMBRE_ARTICULO VARCHAR(50) UNIQUE, 
#    PRECIO INTEGER, 
#    SECCION VARCHAR(20))''')

'''productos =[
    ("Balon", 20, "Jugueteria"),
    ("Pantalon", 15, "Confeccion"),
    ("Destornillador", 20, "Ferreteria"),
    ("Jarron", 45, "Ceramica"),
    ("tren", 15, "Jugueteria")
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)

miCursor.execute("INSERT INTO PRODUCTOS VALUES (NULL, 'Pantalones', 35, 'Confeccion')")'''

miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION = 'Confeccion'")

productos = miCursor.fetchall()

print(productos)

miCursor.execute("UPDATE PRODUCTOS SET PRECIO = 35 WHERE NOMBRE_ARTICULO = 'Balon'")

miCursor.execute("DELETE FROM PRODUCTOS WHERE ID = 7")

miConexion.commit()
miConexion.close()