email = False
miemail = input("Ingresa tu email: ")

for i in miemail:
    if i == "@":
        email = True
        
if email == True:
        print(f"El correo {miemail} es valido")
else:
        print(f"El correo {miemail} no es valido")