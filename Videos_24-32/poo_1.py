class Carro():
    def __init__(self):
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__rueda = 4
        self.__movimiento = False
    
    def arrancar(self,moverse):
        self.__movimiento = moverse
        if (self.__movimiento):
            checking = self.__check()
        if (self.__movimiento and checking):
            return "El carro esta en movimiento"
        elif (self.__movimiento and checking==False):
            return "Falla interna no es posible arrancar"
        else:
            return "El carro esta en quieto"
    
    def estado(self):
        print (f"El carro tiene {self.__rueda} ruedas. Un largo de {self.__largoChasis} y un ancho de {self.__anchoChasis}.")
    
    def __check(self):
        print ("Iniciando chequeo...")
        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"
        
        if (self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas"):
            return True
        else:
            return False

miCarro = Carro()

'''print (f"El largo del carro es: {miCarro.__largoChasis}")
print (f"El carro tiene {miCarro.__rueda} ruedas\n")'''
print (miCarro.arrancar (True))
miCarro.estado()

print ("\n ------------------------ Segunda instancia del objeto ------------------------ \n")

miCarro2 = Carro()

'''print (f"El largo del carro es: {miCarro2.__largoChasis}")
print (f"El carro tiene {miCarro2.__rueda} ruedas\n")'''
print (miCarro2.arrancar (False))
miCarro2.estado()
