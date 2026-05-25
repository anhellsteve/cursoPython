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

def calculoComision(empleado):
    if empleado.salario<5000:
        empleado.salario = empleado.salario * 1.03
    return empleado

listaEmpleadosComision = list(map(calculoComision, listaEmpleados)) #map es una función que recibe una función y un iterable, y devuelve un nuevo iterable con los resultados de aplicar la función a cada elemento del iterable original.

for empleado in listaEmpleadosComision:
    print(empleado)