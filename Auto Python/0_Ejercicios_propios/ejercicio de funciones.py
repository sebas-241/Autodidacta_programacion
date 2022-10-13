def joda(nombre, edad, equipo_favorito):
    if edad < 18:
        return (f"Mi nombre es {nombre}, soy menor de edad, tengo {edad} años y mi equipo favorito es {equipo_favorito}")
    return (f"Mi nombre es {nombre}, soy mayor de edad, tengo {edad} años y mi equipo favorito es {equipo_favorito}")


print(joda("Sebas", 18, "Real Madrid"))
print(joda("Alejandro", 8, "Brasil"))
print(joda("Juan", 50, "Barcelona"))
        