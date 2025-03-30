#Se muestra como se concatenan condiciones en un IF

edad=7

if 0 < edad < 100:
    print ("Edad correcta\n")
else:
    print ("Edad incorrecta\n")


#Segundo Ejemplo de concatenación de condiciones

salarioPresidente = int(input("Ingresar salario presidente "))
print("Salario Presidente: $"+str(salarioPresidente)+"\n")

salarioDirector = int(input("Ingresar salario director "))
print("Salario Director: $"+str(salarioDirector)+"\n")

salarioJefeArea = int(input("Ingresar salario jefe area "))
print("Salario Jefe Area: $"+str(salarioJefeArea)+"\n")

salarioAdministrativo = int(input("Ingresar salario administrativo "))
print("Salario Administrativo: $"+str(salarioAdministrativo)+"\n")

if salarioAdministrativo<salarioJefeArea<salarioDirector<salarioPresidente:
    print("Salarios correctos\n")
else:
    print("Salarios Incorrectos\n")


#Se verifica el uso de condicionales con operadores lógicos AND y OR
'''Ejemplo Se otorgara una beca estudiantil al alumno que cumpla con todos los requisitos
   * que viva a una distancia mayor de 40km de la institución
   * que el numero de hermanos incluyendo sea mayor a 2
   * que el salario familiar anual sea menor o igual a $20000'''

print("\nPrograma de becas\n")

distanciaEscuela = int(input("Ingrese la distancia a la escuela en Km "))
print(str(distanciaEscuela)+"\n")

cantidadHermanos = int(input("Ingrese cuantos hermanos son "))
print(str(cantidadHermanos)+"\n")

salarioFamilia = int(input("Ingrese salario familia anual "))
print(str(salarioFamilia)+"\n")

if distanciaEscuela>40 and cantidadHermanos>2 and salarioFamilia<=20000:
    print("Tienes derecho a beca\n")
else:
    print("No tiene derecho a beca\n")

#Si usamos OR podemos hacer que no sea tan estricto en cumplir ciertas condiciones

if distanciaEscuela>40 and cantidadHermanos>2 or salarioFamilia<=20000: #cambiamos el ultimo and por un or
    print("Tienes derecho a beca\n")
else:
    print("No tiene derecho a beca\n")


#Uso del operador in en las condicionales

print("\nElección de signaturas optativas\n")

print("Asignaturas optativas: Informática Gráfica - Pruebas de Software - Usabilidad y Accesibilidad\n")

asignatura = input("Escribe la asignatura elegida: ")

if asignatura.lower() in ("informática gráfica","pruebas de software","usabilidad y accesibilidad"):
    print ("\nAsignatura elegida: "+asignatura.upper()+"\n")
else:
    print ("\n"+asignatura.upper()+" no esta contemplada\n")


