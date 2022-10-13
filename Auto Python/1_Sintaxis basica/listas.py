# LISTAS
miLista = ["Maria", "Pepe", "Marta", "Antonio"]
print(miLista[:]) #Imprimir todos los elementos de la lista.
print(miLista[2]) #Imprimir un solo elemento.
print(miLista[:3]) #Imprimir hasta cierto punto.
print(miLista[2:]) #Imprimir desde este punto.

# AGREGAR ELEMENTOS EN LISTAS 
miLista.append("Sandra")
miLista.insert(2, "Luis")
miLista.extend(["Juan", "Yohan", "Ruiz"])
print(miLista)

# MOSTRAR INDICE
print(miLista.index("Antonio"))

# MOSTRAR SI UN ELEMENTO ESTA EN UNA LISTA "TRUE AN FALSE"
print("Pepe" in miLista)

# ELIMINACION DE ELEMENTOS
miLista.remove("Yohan")
print(miLista)

# ELIMINAR ULTIMO ELEMENTO AGREGADO
miLista.pop()
print(miLista)

# SUMAR LISTAS
miLista1 = ["Maria", "Pepe", "Marta", "Antonio"]
miLista2 = [2, 3, 4, 5, 6, 7, 8, 9]
miLista3 = miLista1 + miLista2
print(miLista3[:])

# REPETIR TANTAS VECES UNA LISTA 
miLista2 = [2, 3, 4, 5, 6, 7, 8, 9] * 3
print(miLista2[:])