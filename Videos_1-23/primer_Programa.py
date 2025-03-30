message="Hola Mundo"
print (message)

print("Hola Alumnos")

print("Hola Alumnos"); print("Hola Mundo")

#<---Se usa escribir comentarios

mi_nombre = "Mi nombre es Steve!"
print(mi_nombre)
mi_nombre = "Mi nombre es \
Steve!"
print(mi_nombre)

a=0

for i in range (5) :
    a+=1
    print(a)

#Operadores
message = 5+6
print ("Esto es una suma de 5+6: " + str(message))

message = 10%3
print ("Esto es el modulo de 10/3: " + str(message))

message = 5**3
print ("Esto es la potencia de 5^3: " + str(message))

message = 9/2
print ("Esto es la division de 9/2: " + str(message))

message = 9//2
print ("Esto es la division entera de 9/2: " + str(message))

#Tipos de variables
nombre = 5
print (type(nombre))

nombre = "Steve"
print (type(nombre))

nombre = 5.5
print (type(nombre))

message = """Esto es un mensaje
con tres saltos
de linea"""
print (message)

num1 = 5
num2 = 7

if num1 > num2:
    print ("num1 es mayor que num2")
else:
    print ("num2 es mayor que num1")
