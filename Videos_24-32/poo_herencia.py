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

class Furgoneta(Vehiculos):
    
    def carga(self,cargar):
        self.cargado = cargar
        if (self.cargado):
            return "La furgoneta esta cargada\n"
        else:
            return "La furgoneta no esta cargada\n"
    

class Moto (Vehiculos):
    hCaballito = ""
    def caballito(self):
        self.hCaballito = "Voy haciendo el caballito"
    
    def estado (self):
        print ("Marca: ",self.marca,"\nModelo: ",self.modelo,"\nEn Marcha: ",self.enMarcha,
               "\nAcelerando: ",self.acelera,"\nFrenado: ",self.frena,"\n",self.hCaballito,"\n")
    

class VElectricos(Vehiculos):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.autonomia = 100
    
    def cargaEnergia (self):
        self.cargando = True
    

class BiciElectrica (VElectricos,Vehiculos):
    
    pass

miMoto = Moto("Honda", "CBR")
miMoto.caballito()
miMoto.estado()

miFurgoneta = Furgoneta("Renault","Kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
print (miFurgoneta.carga(True))

miBici = BiciElectrica("Orbea", "BMX")