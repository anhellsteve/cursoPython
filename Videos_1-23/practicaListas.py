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
print(str(miLista[-4])+"\n")

#Imprime una sección de la lista
print(str(miLista[1:3])+"\n")

#Agrega al final un elemento
miLista.append("Sandra")
print(str(miLista[:])+"\n")

#Agrega en una posición especifica un elemento
miLista.insert(2,"Andrea")
print(str(miLista[:])+"\n")

#Agrega una multiples elementos a una lista
miLista.extend(["Ana","Lucia","Monica"])
print(str(miLista[:])+"\n")

#Muestra el indice del elemento
print(str(miLista.index("Ana"))+"\n")

#Valida con true o false si se encuentra el elemento en la lista
print("Ana" in miLista)

#Las listas pueden tener valores diferentes
miLista2=["Mario",5,True,2.8]
print("\n"+str(miLista2))

#elimina el elemento seleccionado
miLista.remove("Pepe")
print("\n"+str(miLista[:])+"\n")

#Elimina el ultimo elemento agregado
miLista.pop()
print(str(miLista[:])+"\n")

#Combina o concatena varias listas
miLista3=miLista+miLista2
print(str(miLista3[:])+"\n")

#Repita la lista x cantidad de veces
miLista2=["Mario",5,True,2.8] * 3
print(miLista2)