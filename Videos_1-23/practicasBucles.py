# Validando el uso de continue pass y else en los loops
for i in "python":
    print (f"Viendo la letra {i}")

print ("")

# El uso de continue en el loop para saltarse una iteración
for i in "python":
    if i=="h":
        continue
    print (f"Viendo la letra {i}")

print ("")

nombre = "píldoras informáticas"
print (len(nombre)) # len no trae la longitud del string nos da 21 porque cuenta como carácter el espacio en blanco
print ("")
contador = 0

for i in nombre:
    contador += 1

print (contador) # nos trae el mismo valor que usando el len
print ("")

contador = 0

for i in nombre:
    if i == " ":
        continue
    contador += 1

print (contador) # vale 20 opr que ya no toma el espacio en blanco
print ("")

# Pass sirve para que el valor sea null - se crea un loop infinito se sale con ctrl + p

'''while True:
    pass'''

# else en el loop

email = input("Ingresa tu email: ")

for i in email:
    if i == "@":
        arroba= True
        break;
else:
    arroba= False

print(arroba)
print ("")
