#Tuplas
miTupla=("Steve",13,1,2015,13)

print(str(miTupla[1])+"\n")

#Convierte una tupla en lista
miLista = list(miTupla)

print(str(miLista)+"\n")
print(str(miTupla)+"\n")

#Convierte una lista es tupla
miTupla1=tuple(miLista)
print(str(miTupla1)+"\n")

#Valida con True o False si un elemento esta en la tupla
print("Steve" in miTupla)

#Muestra el indice de un elemento en la tupla
print("\n"+str(miTupla.index("Steve")))

#Muestra cuantas veces se encuentra un elemento en la tupla
print(str(miTupla.count(13))+"\n")

#Muestra la longitud de la tupla
print(str(len(miTupla))+"\n")

#Para crear una tupla unitaria se debe poner una coma "," al final del elemento
miTuplaUnitaria=("Steve",)
print(str(len(miTuplaUnitaria))+"\n")

'''No es necesario poner paréntesis para crear una tupla
Esto se conoce como empaquetado de tupla'''
miTuplaSinParent = "Steve",13,1,2015
print(str(miTuplaSinParent)+"\n")

name, day, month, year = miTuplaSinParent
print(name)
print(year)
print(month)
print(day)