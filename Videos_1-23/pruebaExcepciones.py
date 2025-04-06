def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        print("No se puede dividir por 0")
        return "Operación Errónea"

while True:
    try:
        op1=(int(input("Introduce el primer número: ")))
        op2=(int(input("Introduce el segundo número: ")))
        break;
    except ValueError:
        print("Los valores introducidos deben ser numéricos, inténtalo de nuevo")

operacion=input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operación no contemplada")

print("Operación ejecutada. Continuación de ejecución del programa\n")


#Prueba de excepciones 2 capturar varias excepciones

def division():
    try:
        op1 = float(input("Ingresa el primer número "))
        op2 = float(input("Ingresa el segundo número "))
        print (f"La division es: {op1/op2}")    
    except ValueError:
        print ("Solo debes ingresar números")
    except ZeroDivisionError:
        print ("No se puede dividir por 0")
    
    print ("Calculo Finalizado\n")

division()

# Prueba de Excepciones 3 Lanzar tus excepciones

def evaluaEdad (edad):
    if edad < 0:
        raise TypeError ("No existe edades negativas")
    elif edad < 20:
        return "Eres muy joven\n"
    elif edad < 40:
        return "Eres joven\n"
    elif edad < 65:
        return "Eres maduro\n"
    elif edad < 100:
        return "Cuídate\n"

print(evaluaEdad(35))

# Ejemplo lanzando tus excepciones y capturarlas

import math

def raizCalc (num):
    if num < 0:
        raise ValueError ("El numero no puede ser negativo")
    else:
        return math.sqrt(num)
num1 = (int(input("Ingrese un numero ")))
try:
    print (raizCalc(num1))
except ValueError as NumNegativeError:
    print (NumNegativeError)
print ("Programa terminado\n")
