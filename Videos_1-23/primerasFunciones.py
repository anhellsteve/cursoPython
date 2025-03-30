#Funciones sin parámetros

def message():
    print("Estamos aprendiendo Python")
    print("Estamos aprendiendo instrucciones básicas")
    print("Poco a poco iremos avanzando\n")

message()

message()

print("Ejecutando código fuera de función\n")
message()

def suma():
    num1=5
    num2=7
    print(str(num1+num2)+"\n")

suma()

#Funciones con Parámetros
def suma(num1, num2):
    print(str(num1+num2)+"\n")

suma(5,7)
suma(25,82)
suma(6,10)

#Funciones con parámetros y return
def suma(num1, num2):
    result=num1+num2
    return result

print(str(suma(5,7))+"\n")
print(str(suma(25,82))+"\n")
print(str(suma(6,10))+"\n")

almacena_resultado = suma(5,8)

print(str(almacena_resultado)+"\n")