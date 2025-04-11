class Persona():
    def __init__(self, nombre, edad, residencia):
        self.nombre = nombre
        self.edad = edad
        self.residencia = residencia
    
    def descripcion(self):
        print(f"Nombre: {self.nombre} \nEdad: {self.edad} \nResidencia: {self.residencia}")
    

class Empleado(Persona):
    def __init__(self, salario, antiguedad, nombre, edad, residencia):
        super().__init__(nombre, edad, residencia)
        self.salario = salario
        self.antiguedad = antiguedad
    
    def descripcion(self):
        super().descripcion()
        print(f"Salario: {self.salario} \nAntigüedad: {self.antiguedad} años")

persona1 = Persona("Bryan", 35, "Colombia")
persona1.descripcion()
print("")

empleado1 = Empleado(2000, 10, "Bryan", 35, "Colombia")
empleado1.descripcion()
print("")

# isinstance() es una función que nos dice si un objeto es una instancia de una clase o de una subclase de esa clase.
# En este caso, empleado1 es una instancia de la clase Empleado, que es una subclase de Persona.
print(isinstance(empleado1, Persona)) # True
print(isinstance(empleado1, Empleado)) # True
print(isinstance(persona1, Persona)) # True
print(isinstance(persona1, Empleado)) # False
