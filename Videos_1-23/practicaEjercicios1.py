'''Crea un programa que pida dos números por teclado.
El programa tendrá una función llamada “DevuelveMax”
encargada de devolver el número más alto de los dos introducidos.'''

def DevuelveMax(num1, num2):
    if(num1 < num2):
        print("\n"+str(num2)+" Es el número mayor\n")
    elif(num2 < num1):
        print("\n"+str(num1)+" Es el número mayor\n")
    else:
        print("\nLos números son iguales\n")

num1 = int(input("Ingrese el 1er numero a comparar "))
num2 = int(input("\nIngrese el 2do numero a comparar "))

DevuelveMax(num1, num2)


'''Crea un programa que pida por teclado “Nombre”, “Dirección” y “Tfno”.
Esos tres datos deberán ser almacenados en una lista y mostrar en consola el mensaje:
“Los datos personales son: nombre apellido teléfono” (Se mostrarán los datos introducidos por teclado).'''

name = input("\nIngrese su nombre: ")
address = input("\nIngrese su dirección: ")
phoneNumber = input("\nIngrese se número de teléfono: ")

datosPersonales = [name, address, phoneNumber]

print("\nLos datos personales son: "+datosPersonales[0]+" "+datosPersonales[1]+" "+datosPersonales[2]+"\n")


'''Crea un programa que pida tres números por teclado.
El programa imprime en consola la media aritmética de los números introducidos.'''

num1 = int(input("\nIngrese el 1er numero: "))
num2 = int(input("\nIngrese el 2do numero: "))
num3 = int(input("\nIngrese el 3er numero: "))

print("\nLa media es "+str((num1+num2+num3)/3))