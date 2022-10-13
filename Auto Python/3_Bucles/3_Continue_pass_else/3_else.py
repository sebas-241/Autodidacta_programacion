email = input("Ingresa tu correo electronico: ")

for i in email:
    if i == "@":
        email = True
        break
else:
    email = False
    
print(email)