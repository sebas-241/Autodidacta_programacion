edad = int(input("Ingresa tu edad: "))

while edad <= 0:
    print("Has ingresado una edad negativa. Vuelve a intentarlo.")
    int(input("Ingresa tu edad: "))

print("Gracias por ingresar tu edad.")
print(f"Tienes {edad} de edad.")