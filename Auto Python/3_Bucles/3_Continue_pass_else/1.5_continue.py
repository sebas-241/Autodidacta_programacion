# Eliminador de espacion

nombre = "Visual Studo Code"
contador = 0 

for i in nombre:
    if i == " ":
        continue   # Cada vez que halla un espacio, omite el contador y reitera
    contador = contador + 1

print(contador)