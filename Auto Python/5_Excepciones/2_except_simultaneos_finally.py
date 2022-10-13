def division ():
    try:
        num1 = float(input("Ingresa el primer valor: "))
        num2 = float(input("Ingresa el segundo valor: "))
            
        print("El resultado de la division es " + str(num1/num2))
      
        
    except ValueError:
        print("El valor ingresado no es valido.")
    except ZeroDivisionError:
        print("No puedes dividir por 0.")
    
    finally:
        print("Operacion finalizada.")

division()