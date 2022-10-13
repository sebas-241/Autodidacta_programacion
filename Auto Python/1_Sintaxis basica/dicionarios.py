# DICCIONARIOS 
mi_diccionario = {"Japon":"Tokyo", "Colombia": "Bogota", "España": "Madrid", "Alemania":"Berlin"}

# ACCEDER A UN VALOR 
mi_diccionario = {"Japon":"Tokyo", "Colombia": "Bogota", "España": "Madrid", "Alemania":"Berlin"}
print(mi_diccionario["Japon"])

# AGREGAR ELEMENTOS 
mi_diccionario = {"Japon":"Tokyo", "Colombia": "Bogota", "España": "Madrid", "Alemania":"Berlin"}
mi_diccionario ["Italia"] = "Lisboa"
print(mi_diccionario)

# MODIFICAR VALORES
mi_diccionario = {"Japon":"Tokyo", "Colombia": "Bogota", "España": "Madrid", "Alemania": "Berlin"}
print(mi_diccionario)
mi_diccionario ["Italia"] = "Roma"
print(mi_diccionario)

# ELIMINAR VALORES ELEMENTO
mi_diccionario = {"Japon":"Tokyo", "Colombia": "Bogota", "España": "Madrid", "Alemania":"Berlin"}
del mi_diccionario ["España"]
print(mi_diccionario)

# DICCIONARIO DE DIFERENTES TIPOS 
midiccionariov = {"Alemania":"Berlin", 2:"Numero", "Japoneses": 45}
print(midiccionariov)

# DICCIONARIO CON TUPLAS
mituplad = ("Japon", "Kiev", "Paris", "") 
midiccionariotupla = {mituplad[0] : "Tokyo",  mituplad[1] : "Ucrania", mituplad[2] : "Francia", mitupla[3] : "San Andreas"}
print(midiccionariotupla)

# DICCIONARIO ALMACENA UNA TUPLAS
midic = {23:"Luis", "Titulos":[2004, 2015, 2016, 2017, 2022]}
print(midic["Titulos"])
