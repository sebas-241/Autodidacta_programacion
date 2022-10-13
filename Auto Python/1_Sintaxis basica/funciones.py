# FUNCIONES 
def primera_funcion():
    print("1. Estamos aprendiendo Python.")
    print("2. Estamos desarrollando habilidades")
    print("3. Python es un lenguaje muy conocido.")

print("Aqui se muestra, pero no se imprme en pantalla la primera funcion:")
primera_funcion()


# FUNCIONES "PARAMETROS"
def suma(num1, num2):
    print(num1+num2)
    
suma(5,7)
suma(2,3)
suma(35,358)


# FUNCIONES "RETURN"
def suma(num1, num2):
    resultado = num1+num2
    return resultado
almacena_resultado = suma(8,5)
print("Primera funcion con return")
print(almacena_resultado)
