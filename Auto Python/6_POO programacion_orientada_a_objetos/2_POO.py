class Coche():
    
    def __init__(self):             # Constructor que indica los atributos inicialesde un objeto, punto de partida
        self.__largo_chasis = 250
        self.__ancho_chasis = 120      # __ encapsulacion de una propiedad del objeto y no puede ser cambiada
        self.__ruedas = 4
        self.__en_marcha = False
        
    def arrancar(self, arrancamos):         
        self.__en_marcha = arrancamos
        
        if self.__en_marcha == True:
            return "El coche esta andando"
        else:
            return "El coche esta quieto"
        
        
    def estado (self):
        return(f"El coche tiene {self.__ruedas} ruedas, un ancho de {self.__ancho_chasis} y un largo de {self.__largo_chasis}.")
        

mi_coche = Coche()          
print(mi_coche.arrancar(True))     
print(mi_coche.estado())  

print("-------------------Segundo Objeto--------------------")

miCoche2 = Coche()      # Creacion de un segundo objeto con la misma clase, class
print(miCoche2.arrancar(False))
print(miCoche2.estado())