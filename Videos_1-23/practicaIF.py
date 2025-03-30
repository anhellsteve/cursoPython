#Condicional IF

def evaluar(nota):
    valoracion="aprobado"
    if nota<5:
        valoracion="reprobado"
    return valoracion

print(evaluar(4))
print(evaluar(5))

'''Con el método input se debe ingresar un valor por teclado después continuara con el programa
a tener en cuenta lo que se pasa por input se tomo como string asi se escriban números'''

print("programa de evaluación de notas para alumnos")

notaAlumno=input("Ingresa la nota del alumno")

print(evaluar(int(notaAlumno)))
