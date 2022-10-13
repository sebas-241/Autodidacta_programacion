class Coche():
    
    def __init__(self):             
        self.__largo_chasis = 250
        self.__ancho_chasis = 120     
        self.__ruedas = 4
        self.__en_marcha = False
        
    def arrancar(self, arrancamos):         
        self.__en_marcha = arrancamos
        
        if self.__en_marcha == True:
            chequeo = self.__chequeo_interno()
            
        if self.__en_marcha == True and chequeo == True:
            return "El coche esta andando"
        elif self.__en_marcha == True and chequeo == False:
            return "Ha sucedido un problema. No puede arrancar el coche"
        else:
            return "El coche esta quieto"
        
        
    def estado (self):
        return(f"El coche tiene {self.__ruedas} ruedas, un ancho de {self.__ancho_chasis} y un largo de {self.__largo_chasis}.")
        

    def __chequeo_interno (self):                          # Encapsulacion de un metodo
        print("Realizando chequeo interno....")
        self.gasolina = "OK"
        self.puertas = "CERRADAS"
        self.aceite = "OK"
        
        if self.gasolina == "OK" and self.puertas == "CERRADAS" and self.aceite == "OK":
            return (True)
        else:
            return (False)


mi_coche = Coche()          
print(mi_coche.arrancar(True))     
print(mi_coche.estado())  

print("-------------------Segundo Objeto--------------------")

miCoche2 = Coche()
print(miCoche2.arrancar(False))
print(miCoche2.estado())