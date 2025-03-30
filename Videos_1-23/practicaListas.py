#Listas
miLista=["Maria","Pepe","Martha","Antonio"]

#Imprime la lista
print(miLista[:])

print(miLista[0])
print(miLista[1])
print(miLista[2])
print(miLista[3])
print(miLista[-1])
print(miLista[-2])
print(miLista[-3])
print(miLista[-4])

#Imprime una sección de la lista
print(miLista[1:3])

#Agrega al final un elemento
miLista.append("Sandra")
print(miLista[:])

#Agrega en una posición especifica un elemento
miLista.insert(2,"Andrea")
print(miLista[:])

#Agrega una multiples elementos a una lista
miLista.extend(["Ana","Lucia","Monica"])
print(miLista[:])

#Muestra el indice del elemento
print(miLista.index("Ana"))

#Valida con true o false si se encuentra el elemento en la lista
print("Ana" in miLista)

#Las listas pueden tener valores diferentes
miLista2=["Mario",5,True,2.8]
print(miLista2)

#elimina el elemento seleccionado
miLista.remove("Pepe")
print(miLista[:])

#Elimina el ultimo elemento agregado
miLista.pop()
print(miLista[:])

#Combina o concatena varias listas
miLista3=miLista+miLista2
print(miLista3[:])

#Repita la lista x cantidad de veces
miLista2=["Mario",5,True,2.8] * 3
print(miLista2)