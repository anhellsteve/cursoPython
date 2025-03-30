#Funciones sin parámetros

def message():
    print("Estamos aprendiendo Python")
    print("Estamos aprendiendo instrucciones básicas")
    print("Poco a poco iremos avanzando")

message()

message()

print("Ejecutando código fuera de función")
message()

def suma():
    num1=5
    num2=7
    print(num1+num2)

suma()

#Funciones con Parámetros
def suma(num1, num2):
    print(num1+num2)

suma(5,7)
suma(25,82)
suma(6,10)

#Funciones con parámetros y return
def suma(num1, num2):
    result=num1+num2
    return result

print(suma(5,7))
print(suma(25,82))
print(suma(6,10))

almacena_resultado = suma(5,8)

print(almacena_resultado)