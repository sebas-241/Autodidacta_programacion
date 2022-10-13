# EJEMPLO DE STR Y ANIDACION DE IF Y FOR
print("Verificador de emails")

email = False
for i_1 in "sebgonrod@gmail.com":
    if i_1 == "@":
        email: True
    if email == True:
        print("El correo es correcto")
    else:
        print("El correo no es correcto")
        