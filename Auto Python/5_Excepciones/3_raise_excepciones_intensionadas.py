import math 

def raiz(num1):
    if num1 < 0:
        raise ValueError("El numero no puede ser negativo")  # Generamos un error con un str para explicar el problema
    else:
        return math.sqrt(num1)
    
op1 = int(input("Ingresa un numero: "))


print(raiz(op1))

print("Fin del programa")