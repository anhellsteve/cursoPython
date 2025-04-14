# Métodos de cadenas o strings

# 1. upper() - Convierte la cadena a mayúsculas
cadena = "hola mundo"
print(cadena.upper())  # HOLA MUNDO

# 2. lower() - Convierte la cadena a minúsculas
cadena = "HOLA MUNDO"
print(cadena.lower())  # hola mundo

# 3. capitalize() - Convierte la primera letra de la cadena a mayúscula
cadena = "hola mundo"
print(cadena.capitalize())  # Hola mundo

# 4. isdigit() - Verifica si la cadena contiene solo dígitos
edad = (input("¿Cuál es tu edad? "))

while (edad.isdigit() == False):
    print("Error, ingresa solo números")
    edad = (input("¿Cuál es tu edad? "))

if (int(edad)<18):
    print("Eres menor de edad No puedes Pasar")
else:
    print("Eres mayor de edad Puedes Pasar")


'''Ejercicio 1:
• Crea un programa que pida introducir una dirección de email por teclado.
• El programa debe imprimir en consola si la dirección de email es correcta o no en función de si esta tiene el símbolo @.
• Si tiene una @ la dirección será correcta. Si tiene más de una o ninguna @ la dirección será errónea.
• Si la @ está al comienzo de la dirección de email o al final, la dirección también será errónea,'''


email = input("Introduce tu dirección de email: ")
if email.count('@') == 1 and email[0] != '@' and email[-1] != '@':
    print("La dirección de email es correcta.")
else:
    print("La dirección de email es incorrecta.")

# count() - Cuenta el número de veces que aparece un carácter en la cadena