"""
    AND / OR:
    Programa verificador de becas
    Requisitos:
    - distancia > 40km
    - numero_hermanos > 2
    - salario_anual_padres < 12000000
"""

print("Programa verficador de Becas")
distancia = int(input("Ingrese  la distancia de su casa a la universidad en kilometros: "))
hermanos = int(input("Ingrese el numero de hermanos que tiene: "))
salario = int(input("Ingrese el salario anual que ganan sus padres: "))

if distancia > 40 and hermanos > 2 or salario < 9000000:
    print("Eres un estudiante que merece una beca")
else:
    print("No cumples los requisitos para obtener una beca")







"""
  IN / lower / upper 
"""

print("Eleccion de asignaturas 2022")
print("Las asignaturas disponibles hasta el momento: Matematicas, Biologia, Tecnologia, Ingles")
opcion = input("Escoge tu asignatura: ")

variable = opcion.lower()

if variable in ("matematicas", "biologia", "tecnologia", "ingles"):
    print(f"La aignatura escogida es {variable}")
else:
    print("La asignatura escogida no esta disponible")