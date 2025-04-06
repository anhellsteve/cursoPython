# Practica Generadores crear una lista con números pares

# Forma sin generador
def generarPares (limit):
    num = 1
    miLista=[]
    
    while num < limit:
        miLista.append(num*2)
        num += 1
    return miLista

print (generarPares(10))

# Forma usando generadores

def generarPares (limit):
    num = 1
    
    while num < limit:
        yield num*2
        num += 1

devuelvePares = generarPares(10)

for i in devuelvePares:
    print (i)

''' También se va generando por cada llamada esto solo ocupa espacio en memoria de los números generados'''
devuelvePares = generarPares(10)

print("")
print(next(devuelvePares))
print("Código de ejemplo")
print(next(devuelvePares))
print("Código de ejemplo")
print(next(devuelvePares))
print("")

# Generadores segunda parte

def devuelveCiudades(*ciudades): # se pone un * delante por que se podrán pasar n parámetros
    for elementos in ciudades:
        yield elementos

ciudadesDevueltas = devuelveCiudades("Cali", "Medellin", "Bogota", "Barranquilla")

print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))
print("")

# con el siguiente obtenemos elementos de un elemento como una matriz
def devuelveCiudades(*ciudades): # se pone un * delante por que se podrán pasar n parámetros
    for elementos in ciudades:
        for subElementos in elementos:
            yield subElementos

ciudadesDevueltas = devuelveCiudades("Cali", "Medellin", "Bogota", "Barranquilla")

print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))
print("")

# Pero con generadores se puede simplificar
def devuelveCiudades(*ciudades): # se pone un * delante por que se podrán pasar n parámetros
    for elementos in ciudades:
        yield from elementos

ciudadesDevueltas = devuelveCiudades("Cali", "Medellin", "Bogota", "Barranquilla")

print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))

