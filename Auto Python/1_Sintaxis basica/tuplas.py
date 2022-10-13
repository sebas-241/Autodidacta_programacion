# TUPLAS
mitupla=("Sebastian", 9, 10, 2004)

# ACCEDER A UN ELEMENTO EN CONCRETO 
mitupla=("Sebastian", 9, 10, 2004)
print(mitupla[2])

# CONVERTIR TUPLAS A LISTAS 
mitupla=("Sebastian", 9, 10, 2004)
miListaTp = list(mitupla)
print(miListaTp)

# CONVERTIR LISTAS A TUPLAS
milistac = ["Sebastian", 9, 10, 2004]
mituplalist = tuple(milistac)
print(mituplalist)

# VERIFICAR ELEMENTOS EN UNA TUPLA
mitupla = ("Sebastian", 9, 10, 2004)
print("Sebastian" in mitupla)

# CUANTAS VECES SE ENCUENTRA UN ELEMENTOS
mitupla = ("Sebastian", 9, 10, 2004)
print(mitupla.count(10))

# LONGITUD DE UNA TUPLA
mitupla = ("Sebastian", 9, 10, 2004)
print(len(mitupla))

# TUPLA UNITARIA
mituplauni = ("Sebastian",)
print(mituplauni)
print(len(mituplauni))

# DESEMPAQUETADO DE TUPLAS 
tuplacumple= ("Sebastian", 9, 10, 2004, "Noche")
Nombre, Dia, Mes, Agno, Tiempo = tuplacumple
print(Nombre)
print(Dia)
print(Mes)
print(Agno)
print(Tiempo)

# INDEX EN TUPLAS
index_en_tuplas = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(index_en_tuplas.index(5))
