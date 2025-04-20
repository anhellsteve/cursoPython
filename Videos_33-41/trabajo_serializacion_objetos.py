import pickle

class Vehiculos ():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enMarcha = False
        self.acelera = False
        self.frena = False
    
    def arrancar (self):
        self.enMarcha = True
    
    def acelerar (self):
        self.acelera = True
    
    def frenar (self):
        self.frena = True
    
    def estado (self):
        print ("Marca: ",self.marca,"\nModelo: ",self.modelo,"\nEn Marcha: ",self.enMarcha,
               "\nAcelerando: ",self.acelera,"\nFrenado: ",self.frena)

carro = Vehiculos("Mazda", "MX-5")
carro2 = Vehiculos("Suzuki", "Swift")
carro3 = Vehiculos("Renault", "Clio")

carros = [carro, carro2, carro3]

# Serializar objetos
fichero = open('los_carros', 'wb') # 'wb' es para escribir en binario
pickle.dump(carros, fichero) # Serializa el objeto carro
fichero.close() # Cierra el fichero

# Deserializar objetos
ficherocarga = open('los_carros', 'rb') # 'rb' es para leer en binario
misCarros = pickle.load(ficherocarga) # Deserializa el objeto misCarros
ficherocarga.close() # Cierra el fichero

for i in misCarros:
    i.estado() # Muestra el estado de cada objeto
    print("")
# El resultado es el mismo que si hubiéramos hecho: misCarros[0].estado()
# El resultado es el mismo que si hubiéramos hecho: misCarros[1].estado()