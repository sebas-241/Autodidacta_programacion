print("Calculadora Simple")

num1 = int(input("Por favor ingrese el primer numero: "))
num2 = int(input("Por favor ingrese el segundo numero: "))

print(f"Elija la opcion que desea aplicar con los numeros {num1} y {num2} : \n"
    "1. Sumar los numeros. \n"
    "2. Restar los numeros. \n"
    "3. Multiplicar los numeros. \n" 
    "4. Dividir los numeros. \n"
    "5. Cerrar el programa.")

eleccion = int(input("Escoja su eleccion: "))

if eleccion == 1:
    print((num1)+(num2))
elif eleccion == 2:
    print((num1)-(num2))
elif eleccion == 3:
    print((num1)*(num2))
elif eleccion == 4:
    print((num1)/(num2))
else:
    None
    
    