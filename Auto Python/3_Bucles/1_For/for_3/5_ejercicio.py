valido = False
email = input("Introduce tu email: ")

for i in range(len(email)):
    if email [i] == "@":
        valido = True
        
if valido == True:
    print("Email correcto")
else:
    print("Email incorrecto")