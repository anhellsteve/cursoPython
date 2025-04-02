'''Crea un programa que pida números infinitamente. Los números introducidos deben ser cada vez mayores
El programa finalizará cuando se introduce un número menor que el anterior.'''

print ("Número mayores consecutivos \n")
num = int(input("Ingresa un número: "))
num2 = int(input(f"Ingresa un número mayor a {num}: "))
while num2>num:
    num = num2
    num2 = int(input(f"Ingresa un número mayor a {num}: "))

print (f"{num2} No es mayor que {num}")

print("\n")

'''Crea un programa que pida números positivos indefinidamente. El programa termina cuando se introduce un número negativo.
Finalmente el programa muestras la suma de todos los números introducidos'''

print("Números positivos sumados\n")

positivo = int(input("Ingrese un numero positivo: "))
suma = 0

while positivo>0:
    suma += positivo
    positivo = int(input("Ingrese un numero positivo nuevamente: "))

if suma==0:
    print("\nNo ingresaste ningún número positivos\n")
else:
    print(f"\n La suma de los números positivos que ingresaste es {suma}\n")

