def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        yield from elemento   # Devuelve subelementos de lo que se ponga en los parametros de la funcion "letras en str"
        
devuelve = devuelve_ciudades("Bogota", "Madrid", "Paris", "Lima", "Berlin", "Hokkaido")

print(next(devuelve))
print(next(devuelve))
print(next(devuelve))
print(next(devuelve))
print(next(devuelve))