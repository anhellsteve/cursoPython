import sqlite3

miConexion = sqlite3.connect("PrimeraBase")

miCursor = miConexion.cursor()

#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

miCursor.execute("CREATE TABLE IF NOT EXISTS PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

#miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON', 15, 'DEPORTES')")

'''variosProductos = [
    ("Camiseta", 10, "Deportes"),
    ("Jarron", 90, "Ceramica"), 
    ("Camion", 20, "Jugueteria")
]
miCursor.executemany("INSERT INTO PRODUCTOS VALUES(?, ?, ?)", variosProductos)'''

miCursor.execute("SELECT * FROM PRODUCTOS")

variosProductos = miCursor.fetchall()
print(variosProductos)

for producto in variosProductos:
    print(producto)

for producto in variosProductos:
    print("Nombre Articulo: ", producto[0], "- Precio: ", producto[1], "- Seccion: ", producto[2])

miConexion.commit()

miConexion.close()
