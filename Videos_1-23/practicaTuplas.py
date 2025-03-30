#Tuplas
miTupla=("Steve",13,1,2015,13)

print(miTupla[1])

#Convierte una tupla en lista
miLista = list(miTupla)

print(miLista)
print(miTupla)

#Convierte una lista es tupla
miTupla1=tuple(miLista)
print(miTupla1)

#Valida con True o False si un elemento esta en la tupla
print("Steve" in miTupla)

#Muestra el indice de un elemento en la tupla
print(miTupla.index("Steve"))

#Muestra cuantas veces se encuentra un elemento en la tupla
print(miTupla.count(13))

#Muestra la longitud de la tupla
print(len(miTupla))

#Para crear una tupla unitaria se debe poner una coma "," al final del elemento
miTuplaUnitaria=("Steve",)
print(len(miTuplaUnitaria))

'''No es necesario poner paréntesis para crear una tupla
Esto se conoce como empaquetado de tupla'''
miTuplaSinParent = "Steve",13,1,2015
print(miTuplaSinParent)

name, day, month, year = miTuplaSinParent
print(name)
print(year)
print(month)
print(day)