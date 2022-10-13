class Vehiculo ():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.en_marcha = False
        self.acelera = False
        self.frena = False

    def arrancar (self):      # Propiedad que nos permite arrancar
        self.en_marcha = True
        
    def acelerar (self):
        self.acelera = True
    
    def frenar (self):
        self.frena = True
        
    def estado (self):
        return (f"Marca: {self.marca}\nModelo: {self.modelo}\nEn marcha: {self.en_marcha}\nAcelerando: {self.acelera}\nFrenando: {self.frena}")

class Moto(Vehiculo):
    pass

mi_Moto = Moto("Honda", "2482004")

print(mi_Moto.estado())