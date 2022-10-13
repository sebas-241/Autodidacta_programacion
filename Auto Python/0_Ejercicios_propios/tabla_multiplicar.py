while True:
    
    num = int(input("Ingrese la tabla de multiplicar que desea ver: "))
    
    def multiplicar (numero, multiplicador):
        return (f"{numero} x {multiplicador} = {numero*multiplicador}")

    print(multiplicar(num, 1))
    print(multiplicar(num, 2))
    print(multiplicar(num, 3))
    print(multiplicar(num, 4))
    print(multiplicar(num, 5))
    print(multiplicar(num, 6))
    print(multiplicar(num, 7))
    print(multiplicar(num, 8))
    print(multiplicar(num, 9))
    print(multiplicar(num, 10))        