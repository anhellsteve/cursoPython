from io import open
# open() abre un archivo y devuelve un objeto de archivo
# open(archivo, modo, encoding)
# archivo: nombre del archivo que se va a abrir
# modo: 'r' (lectura), 'w' (escritura), 'a' (agregar), 'b' (binario)
# encoding: 'utf-8', 'latin-1', 'ascii', etc.
# 'r' = lectura (read)
# 'w' = escritura (write) (sobrescribe el archivo si ya existe)
# 'a' = agregar (append) (agrega al final del archivo si ya existe)

archivo_texto = open('archivo.txt', 'w', encoding='utf-8')

frase = 'Estupendo, ya tenemos nuestro primer archivo de texto usando Python\nhoy'

archivo_texto.write(frase)  # Escribe la frase en el archivo
archivo_texto.close()  # Cierra el archivo
# El archivo se guarda en la misma carpeta donde se ejecuta el script

archivo_texto = open('archivo.txt', 'r', encoding='utf-8')  # Abre el archivo en modo lectura
contenido = archivo_texto.read()  # Lee el contenido del archivo
archivo_texto.close()  # Cierra el archivo
print(contenido)  # Imprime el contenido del archivo

archivo_texto = open('archivo.txt', 'r', encoding='utf-8')  # Abre el archivo en modo lectura
lineas = archivo_texto.readlines()  # Lee todas las líneas del archivo y las guarda en una lista
archivo_texto.close()  # Cierra el archivo
print(lineas)  # Imprime la lista de líneas
print(lineas[0])  # Imprime la primera línea del archivo
print(lineas[1])  # Imprime la segunda línea del archivo

archivo_texto = open('archivo.txt', 'a', encoding='utf-8')  # Abre el archivo en modo agregar
frase = '\nEsta es una nueva línea que se agrega al final del archivo\n'
archivo_texto.write(frase)  # Escribe la frase en el archivo
archivo_texto.close()  # Cierra el archivo
# El archivo se guarda en la misma carpeta donde se ejecuta el script

print('---------------------------------------------------------------------')

archivo_texto = open('archivo.txt', 'r', encoding='utf-8')  # Abre el archivo en modo lectura
print(archivo_texto.read())  # Imprime el contenido del archivo
print('-')
print(archivo_texto.read())  # Imprime el contenido del archivo (vacío porque ya se leyó)
print('-')
archivo_texto.seek(0)  # Regresa al inicio del archivo
print(archivo_texto.read())  # Imprime el contenido del archivo (desde el inicio)
print('-')
archivo_texto.seek(11)  # Regresa a la posición 11 del archivo
print(archivo_texto.read())  # Imprime el contenido del archivo (desde la posición 11)
print('-')
archivo_texto.seek(0) # Regresa al inicio del archivo
print(archivo_texto.read(11))  # Imprime 11 caracteres del archivo (desde la posición 11)
print('-')
print(archivo_texto.read()) # Imprime el contenido del archivo (desde la posición 22)
print('-')
archivo_texto.seek(0)  # Regresa al inicio del archivo
archivo_texto.seek(len(archivo_texto.read())/2)  # Regresa a la mitad del archivo
print(archivo_texto.read())  # Imprime el contenido del archivo (desde la mitad)
print('-')
archivo_texto.seek(0)  # Regresa al inicio del archivo
archivo_texto.seek(len(archivo_texto.readline()))   # Regresa al final de la primera línea
print(archivo_texto.read())  # Imprime el contenido del archivo (desde el final de la primera línea)
archivo_texto.close()  # Cierra el archivo
# El archivo se guarda en la misma carpeta donde se ejecuta el script
print('---------------------------------------------------------------------')
archivo_texto = open('archivo.txt', 'r+', encoding='utf-8')  # Abre el archivo en modo lectura y escritura
archivo_texto.write('Comienzo de texto\n')  # Escribe la frase en el archivo
archivo_texto.seek(0)  # Regresa al inicio del archivo
print(archivo_texto.readlines())  # Imprime el contenido del archivo
archivo_texto.close()  # Cierra el archivo
print('---------------------------------------------------------------------')
archivo_texto = open('archivo.txt', 'r+', encoding='utf-8')  # Abre el archivo en modo lectura y escritura
lineas_texto = archivo_texto.readlines()  # Lee todas las líneas del archivo y las guarda en una lista
lineas_texto[1]= 'Esta nueva linea a sido incluida desde el exterior\n'   # Cambia la segunda línea del archivo
archivo_texto.seek(0)  # Regresa al inicio del archivo
archivo_texto.writelines(lineas_texto)  # Escribe la lista de líneas en el archivo
archivo_texto.close()  # Cierra el archivo