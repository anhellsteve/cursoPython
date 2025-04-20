import pickle

lista_nombres = ['Pedro', 'Pablo', 'Martha', 'Angela', 'Jose']
# Serializar la lista de nombres

fichero_binario = open('lista_nombres', 'wb') # wb = write binary
pickle.dump(lista_nombres, fichero_binario) # Serializamos la lista de nombres
fichero_binario.close() # Cerramos el fichero binario

# Deserializar la lista de nombres

fichero_binario = open('lista_nombres', 'rb') # rb = read binary
lista = pickle.load(fichero_binario) # Deserializamos la lista de nombres
print(lista) # Imprimimos la lista de nombres
fichero_binario.close() # Cerramos el fichero binario
# El fichero binario se cierra automáticamente al salir del bloque with