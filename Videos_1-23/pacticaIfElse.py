#Condicional IF ELSE

#SE muestra el uso de if else y elif con un acceso de mayoría de edad
print("Verificación de acceso")

edadUsuario = int(input("Ingresa tu edad "))

if edadUsuario<18:
    print("No puedes pasar")
elif edadUsuario>100:
    print("Edad incorrecta")
else:
    print("Puedes pasar")

print("El programa a finalizado")

#Ahora se validara con distintos niveles de calificaciones
print("Verificación Nota alumno")

notaAlumno=int(input("Ingrese la nota del alumno "))

if notaAlumno<4:
    print("F")
elif notaAlumno<5:
    print("E")
elif notaAlumno<6:
    print("D")
elif notaAlumno<7:
    print("C")
elif notaAlumno<8:
    print("B")
elif notaAlumno<9:
    print("A")
else:
    print("A+")