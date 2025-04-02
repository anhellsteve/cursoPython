import math
#Loop while ejemplo de uso con ejecución determinada
i=1

while i<=10:
    print(f"Ejecución {i}")
    i+=1

print("\nTermina ejecución\n")

#Loop while ejemplo de uso con ejecución indeterminada
edad = int(input("Ingrese su edad: "))

while edad<0:
    print("La edad no debe ser negativa\n")
    edad = int(input("Ingrese su edad: "))

print("\nGracias. Puede continuar")
print(f"Edad del aspirante {edad}")

print("\n")

#loop while se puede combinar en su validación
edad = int(input("Ingrese su edad: "))

while edad<5 or edad>100:
    print("Edad Incorrecta\n")
    edad = int(input("Ingrese su edad: "))

print("\nGracias. Puede continuar")
print(f"Edad del aspirante {edad}")

print("\n")

#loop while se puede hacer para que no sea infinito
print("Programa de calculo de raíz cuadrada")

numRaiz = int(input("Ingrese el numero a calcular raiz: "))
intento = 0

while numRaiz < 0:
    print("numero no puede ser negativo")
    
    if intento == 2:
        print("Muchos intentos incorrectos")
        break;
    intento+=1
    numRaiz = int(input("Ingrese el numero a calcular raiz: "))

if intento<2:
    solucion = math.sqrt(numRaiz)
    print(f"la raíz cuadrada de {numRaiz} es {solucion}")