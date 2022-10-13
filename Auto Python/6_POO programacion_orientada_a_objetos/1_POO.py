class Coche():
    largo_chasis = 250
    ancho_chasis = 120
    ruedas = 4
    en_marcha = False
    
    def arrancar(self):         # El self se refiere al objeto, en este caso, Coche
        self.en_marcha = True
        
    def estado (self):
        if self.en_marcha == True:
            return "El coche esta andando"
        else:
            return "El coche esta quieto"
        

mi_coche = Coche()          # Crea un objeto, asignandole una variable a la class

print(f"El largo de chasis del coche es de {mi_coche.largo_chasis} cm")    # Se envocan el objeto y propiedad
print(f"El coche tiene {mi_coche.ruedas} ruedas")

mi_coche.arrancar()     # Se cambia la propiedad en marcha con el modulo arrancar

print(mi_coche.estado())  # Se envoca el objeto y el metodo estado, como anterior mente se puso el arrancar true da el primer estado