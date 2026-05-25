def numPar(num):
    if num % 2 == 0:
        return True
    else:
        return False

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(filter(numPar, numeros)))
print("")
print(list(filter(lambda numeroPar: numeroPar%2 == 0, numeros)))
print("")

class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
    
    def __str__(self):
        return f"{self.nombre} Trabaja como {self.cargo} y tiene un salario de {self.salario} $"
    

listaEmpleados = [
    Empleado("Juan", "Programador", 5000),
    Empleado("Maria", "Diseñadora", 4000),
    Empleado("Pedro", "Programador", 4500),
    Empleado("Ana", "Gerente", 6000)
]

salarioMayor = filter(lambda empleado: empleado.salario > 4500, listaEmpleados)

for empleado in salarioMayor:
    print(empleado)