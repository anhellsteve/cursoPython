#Condicional IF

def evaluar(nota):
    valoracion="\naprobado\n"
    if nota<5:
        valoracion="\nreprobado\n"
    return valoracion

print(evaluar(4))
print(evaluar(5))

'''Con el método input se debe ingresar un valor por teclado después continuara con el programa
a tener en cuenta lo que se pasa por input se tomo como string asi se escriban números'''

print("programa de evaluación de notas para alumnos")

notaAlumno=input("\nIngresa la nota del alumno ")

print(evaluar(int(notaAlumno)))
