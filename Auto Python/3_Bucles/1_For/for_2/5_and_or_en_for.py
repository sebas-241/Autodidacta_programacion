contador = 0
miemail = input("Escribe tu email: ")

for i in miemail:
    if i == "@" or i == ".":
        contador = contador+1
        
if contador == 2:
    print(f"El email {miemail} es valido") 
else:
    print(f"El email {miemail} no es valido") 