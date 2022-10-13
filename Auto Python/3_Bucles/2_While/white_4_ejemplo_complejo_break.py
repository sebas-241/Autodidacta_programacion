import math

print("Programa que te da la raiz cuadrada de un valor")
numero = int(input("Ingresa el valor: "))  # Ingresa valor por teclado

contador = 0  # Contador para controlar el flujo

while numero < 0:  
    print("No se puede hallar la raiz cuadrada de un numero negativo. Vuelve a intentarlo.")
    numero = int(input("Ingresa el valor: "))  # Vuelve pedir el dato
    if numero < 0:       # Si el dato es nuevamente incorrecto, suma 1 al contador
        contador = contador + 1
    
    if contador == 2:     # Si se falla hasta que el contador llegue a 2, el programa termian con un break
        print("Has consumido todos tus intento. El programa ha finalizado.")
        break;
    
if contador < 2:  # Si el usuario no falla mas de 2 veces, le da la solucion a problema
    solucion = math.sqrt(numero)
    print(f"La raiz cuadrada de {numero} es: {solucion}.")