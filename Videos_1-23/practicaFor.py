#Loop for ejemplo de uso con una lista
for i in [1,2,3]:
    print("hola")

print("\n")

#Loop for se repite no por los números puestos sino por la cantidad de elementos en la lista
for i in ["primavera","verano","otoño","invierno"]:
    print("hola")

print("\n")

#Loop for asigna a i los valores de la lista en cada iteración hasta que ya no cuente con mas
for i in ["primavera","verano","otoño","invierno"]:
    print(i)

print("\n")

#Loop for podemos hacer que todo se imprima un una sola linea
for i in [1,2,3]:
    print("hola", end=" ")

print("\n")

#Loop for cuando ponemos a recorrer un string lo hace como caracteres tenga
for i in "cursopython@outlook.com":
    print("hola", end=" ")

print("\n")

#con el loop for también podemos validar un carácter en especifico como el @ de un email
email = False
for i in "cursopython@outlook.com":
    if (i=="@"):
        email = True

if email:
    print("Email correcto")
else:
    print("Email incorrecto")

print("\n")

#Ingresando cualquier email con input para el loop for
email = False
miEmail = input("Ingrese su email: ")
for i in miEmail:
    if (i=="@"):
        email = True

if email:
    print("\nEmail correcto")
else:
    print("\nEmail incorrecto")

print("\n")

#usando contadores en los loop for
contador = 0
miEmail = input("Ingrese su email: ")
for i in miEmail:
    if (i=="@" or i=="."):
        contador += 1

if contador==2:
    print("\nEmail correcto")
else:
    print("\nEmail incorrecto")

print("\n")

#loop for utilizando range
for i in range(5):
    print("hola", end=" ")

print("\n")

#loop for utilizando f para combinar variable y texto
for i in range(5):
    print(f"Valor de la variable {i}")

print("\n")

#loop for utilizando range podemos indicar con 2 parámetros de donde queremos que empiece a contar y en donde termina
for i in range(5,10):
    print(f"Valor de la variable {i}")

print("\n")

'''loop for utilizando range podemos indicar con 3 parámetros
de donde queremos que empiece a contar hasta donde finalizar y de cuanto en cuanto contar'''
for i in range(5,51,3):
    print(f"Valor de la variable {i}")

print("\n")

#usando len en los loop for
valido=False
email=input("Ingrese su email: ")
for i in range(len(email)):
    if email[i] =="@":
        valido=True

if valido:
    print("Email correcto")
else:
    print("Email incorrecto")

print("\n")
