import pickle

class Persona:
    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print(f'Se ha creado la persona con nombre {self.nombre}')
    
    def __str__(self):
        return f"{self.nombre} - {self.genero} - {self.edad}"
    

class listaPersona:
    def __init__(self):
        self.personas = []
        listaDePersonas = open('FicheroExterno', 'ab+')
        listaDePersonas.seek(0)
        try:
            self.personas = pickle.load(listaDePersonas)
            print(f'Se cargaron {len(self.personas)} personas')
        except:
            print("No hay personas para cargar")
        finally:
            listaDePersonas.close()
    
    
    def agregarPersona(self, persona):
        self.personas.append(persona)
        self.guardarPersonasEnFichero()
    
    def mostrarPersonas(self):
        for persona in self.personas:
            print(persona)
    
    def guardarPersonasEnFichero(self):
        listaDePersonas = open('FicheroExterno', 'wb')
        pickle.dump(self.personas, listaDePersonas)
        listaDePersonas.close()
    
    def mostrarInfoFichero(self):
        print("Mostrando información del fichero")
        for p in self.personas:
            print(p)
    

miLista = listaPersona()
persona = Persona("Maria", "Femenino", 19)
miLista.agregarPersona(persona)
miLista.mostrarInfoFichero()