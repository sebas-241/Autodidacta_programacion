# CONDICIONALES 
numero1 = 4
numero2 = 3

if numero1 < numero2:
    print("El numero 1 es menor que el numero 2.")
else:
    print("El numero 1 es mayor que el numero 2.")
    
    
# CONDICIONALES EJEM 2
print("Programa de calificacion notas")
notas_alumno = (input("Ingrese su nota: "))

def evaluacion(nota):
    if nota < 5:
        valoracion = "Nota perdida"
    else:
        valoracion = "Nota aprobada"
    return valoracion
    
print(evaluacion (int(notas_alumno)))

    