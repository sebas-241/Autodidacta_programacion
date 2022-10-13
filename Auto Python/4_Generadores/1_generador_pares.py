# Devuelve valores uno por uno sin necesidad de gastar demaciados recursos

def generadorpares(limite):
    num = 1
    
    while num < limite:
        yield num*2
        num = num + 1 

devuelvepares = generadorpares(10)

print(next(devuelvepares))
print("Codigo que llena")
print(next(devuelvepares))
print("Codigo que llena")
print(next(devuelvepares))
print("Codigo que llena")
