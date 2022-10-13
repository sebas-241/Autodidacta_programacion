def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion (num1, num2):
    return num1 * num2

def division(num1, num2):
    try:   # Intenta hacer esta division, si no puede pasa al except
        return num1 / num2        
    except ZeroDivisionError:       # Aqui se coloca el nombre del error y se le pone que hacer cuando se presente este
        print("No se puede dividir por cero")
        return ("Operacion erronea")

inicio1 = int(input("Ingresa el primer valor numerico: "))
inicio2 = int(input("Ingresa el segundo valor numerico: "))

opcion = input("Que desea hacer con los valores ingresados: (suma, resta, multiplicacion, division): ")

if opcion == "suma":
    print(suma(inicio1, inicio2))
elif opcion == "resta":
    print(resta(inicio1, inicio2))
elif opcion == "multiplicacion":
    print(multiplicacion(inicio1, inicio2))
elif opcion == "division":
    print(division(inicio1, inicio2))
else:
    print("El valor no es valido.")
    
    
print("Operación ejecutada. Continuación de ejecúción del programa ")    