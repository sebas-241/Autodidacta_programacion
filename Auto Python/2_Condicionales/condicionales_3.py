print("Verificador de salarios")

salario_presidente = int(input("Ingrese el salario del presidente: "))
print(f"El salario del presidente es de: {salario_presidente}")

salario_director = int(input("Ingrese el salario del director: "))
print(f"El salario del director es de: {salario_director}")

salario_jefe_area = int(input("Ingrese el salario del jefe area: "))
print(f"El salario del jefe area es de: {salario_jefe_area}")

salario_empleado = int(input("Ingrese el salario del empleado: "))
print(f"El salario del empleado es de: {salario_empleado}")

if salario_empleado < salario_jefe_area < salario_director < salario_presidente:
    print("En esta empresa esta bien dstribuidos los salarios")
else:
    print("Esta empresa necesita ser investigada por mal distribucion de salarios")

