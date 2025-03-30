#Diccionarios
miDiccionario = {"Colombia":"Bogota","Ecuador":"Quito","Brasil":"Brasilia","Peru":"Lima"}

print(miDiccionario["Colombia"])
print(str(miDiccionario)+"\n")

#Se agrega y se corrigen valores de esta forma
miDiccionario["Chile"] = "Asuncion"
print(str(miDiccionario)+"\n")

miDiccionario["Chile"] = "Santiago"
print(str(miDiccionario)+"\n")

#Se eliminan valores de la siguiente forma
del miDiccionario["Brasil"]
print(str(miDiccionario)+"\n")

#Los diccionarios pueden tener diferentes valores
miDiccionarioMix = {"Colombia":"Bogota",10:"Messi","Mosqueteros":3}
print(str(miDiccionarioMix)+"\n")

#Otra forma de llenar un diccionario con Listas
miLista = ["Colombia","Argentina","Mexico","Venezuela"]
miDiccionarioLista = {miLista[0]:"Bogota",miLista[1]:"Buenos Aires",miLista[2]:"Mexico DF",miLista[3]:"Caracas"}
print(miDiccionarioLista)
print(miDiccionarioLista[miLista[1]])
print(miDiccionarioLista["Argentina"]+"\n")

miDiccioLista={23:"Jordan","Nombre":"Michael","Equipo":"Chicago","Anillos":[1991,1992,1993,1996,1997,1998]}
print(miDiccioLista)
print(miDiccioLista["Equipo"])
print(str(miDiccioLista["Anillos"])+"\n")

#Se puede poner un diccionario dentro de otro
miDiccionarioDoble={23:"Jordan","Nombre":"Michael","Equipo":"Chicago","Anillos":{"Temporadas":[1991,1992,1993,1996,1997,1998]}}
print(miDiccionarioDoble)
print(str(miDiccionarioDoble["Anillos"])+"\n")

#Funciones que trae las claves=Keys y los valores=Values de un Diccionario
print(miDiccionario.keys())
print(str(miDiccionario.values())+"\n")

#Función que trae la longitud de un Diccionario
print(len(miDiccionario))