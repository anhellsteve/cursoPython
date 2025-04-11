class Carro():
    def desplazamiento(self):
        print("Me desplazo utilizando 4 ruedas")
    

class Moto():
    def desplazamiento(self):
        print("Me desplazo utilizando 2 ruedas")
    

class Camion():
    def desplazamiento(self):
        print("Me desplazo utilizando 6 ruedas")
    

# sin el uso de polimorfismo
miVehiculo1 = Moto()
miVehiculo1.desplazamiento()
miVehiculo2 = Carro()
miVehiculo2.desplazamiento()
miVehiculo3 = Camion()
miVehiculo3.desplazamiento()

print("")

# con el uso de polimorfismo
def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()

vehiculo = Carro()
desplazamientoVehiculo(vehiculo)