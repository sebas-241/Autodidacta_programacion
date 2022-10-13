import random 
while True:
      try:
            bienvenida = int(input("Ingrese la opcion que desee realizar: [1] Iniciar el juego. [2] Salir el juego.\n"))
            break
      except ValueError:
            print("Valor incorrecto. Ingrese algun de los dos valores mostrados en pantalla.")
            bienvenida = int(input("[1] Iniciar el juego. [2] Salir el juego.\n"))
            

      

while bienvenida == 2:
      print("Gracias por intentarlo...")
      break
while bienvenida > 2:
      print("Haz ingresado un valor erroneo. Vuelve a intentarlo.")
      bienvenida = int(input("Ingrese la opcion que desee realizar: [1] Iniciar el juego. [2] Salir el juego.\n"))
                
def probabilidades (eleccion, eleccion_pc):
      if eleccion == 0 and eleccion_pc == 0:
            return("El pc ha ganado")
      elif eleccion == 0 and eleccion_pc == 1:
            return ("Has ganado")
      elif eleccion == 0 and eleccion_pc == 2:
            return("Empate")
      elif eleccion == 1 and eleccion_pc == 0:
            return("Has ganado")
      elif eleccion == 1 and eleccion_pc == 1:
            return("Empate")
      elif eleccion == 1 and eleccion_pc == 2:
            return("El pc ha ganado")
      elif eleccion == 2 and eleccion_pc == 0:
            return("Empate")
      elif eleccion == 2 and eleccion_pc == 1:
            return("El pc ha ganado")
      elif eleccion == 2 and eleccion_pc == 2:
            return("Has ganado")
            

if bienvenida == 1: 
      while True:
            try:
                  eleccion = (int(input("Bien, ahora elige tu arma: [0] Tijeras [1] Papel [2] Piedra \n")))
                  
            except ValueError:
                  print("Valor no valido. Vuelva a intentarlo")
                  eleccion = (int(input("Elige tu arma: [0] Tijeras [1] Papel [2] Piedra \n")))
                  
                  
while eleccion >=3:
      print("No es un valor valido. Vuelve a intentarlo.")
      eleccion = (int(input("Vuelve a elegir tu arma: [0] Tijeras [1] Papel [2] Piedra \n")))
            
      if eleccion == 0:
            veredicto = print("Has elegido Tijeras")
      elif eleccion == 1:
            veredicto = print("Has elegido Papel")
      elif eleccion == 2:
            veredicto = print("Has elegido Piedra")
 


      decision = input("Si estas listo presiona y: ")
      yes_not = decision.lower()
      while decision != "y":
            print("Valor incorrecto.")
            decision = input("Si estas listo presiona y: ")
            yes_not = decision.lower()
            
      if yes_not == "y":
            pc = ["Piedra", "Papel", "Tijera"]
            eleccion_pc = pc_game = random.randint(0,2)
      print(f"El Pc ha elegido {pc[pc_game]}")
      print(probabilidades(eleccion, eleccion_pc))


          
            



      
