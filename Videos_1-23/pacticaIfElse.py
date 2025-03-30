#Condicional IF ELSE

#SE muestra el uso de if else y elif con un acceso de mayoría de edad
print("Verificación de acceso\n")

edadUsuario = int(input("Ingresa tu edad "))

if edadUsuario<18:
    print("\nNo puedes pasar")
elif edadUsuario>100:
    print("\nEdad incorrecta")
else:
    print("\nPuedes pasar")

print("\nEl programa a finalizado\n")

#Ahora se validara con distintos niveles de calificaciones
print("\nVerificación Nota alumno\n")

notaAlumno=int(input("Ingrese la nota del alumno "))

if notaAlumno<4:
    print("\nF")
elif notaAlumno<5:
    print("\nE")
elif notaAlumno<6:
    print("\nD")
elif notaAlumno<7:
    print("\nC")
elif notaAlumno<8:
    print("\nB")
elif notaAlumno<9:
    print("\nA")
else:
    print("\nA+")