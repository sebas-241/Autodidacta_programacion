"""
MURCIELAGO
0123456789
"""

claves = {
    "m": "0",
    "u": "1",
    "r": "2",
    "c": "3",
    "i": "4",
    "e": "5",
    "l": "6",
    "a": "7",
    "g": "8",
    "o": "9"
}

def encriptar(string):
    datos = list(string.lower())
    for i in datos:
        if i in claves.keys():
            indice = datos.index(i)
            datos[indice] = claves[i]
            cadena_resultante = ""
            for i in datos:
                cadena_resultante += i
    return cadena_resultante

def desencriptar(string):
    cadena_resultante = ""
    for i in string:
        try:
            letra = claves[i]
        except KeyError:
            letra = i
        cadena_resultante = cadena_resultante + str(letra)
    return cadena_resultante

        
print("Encriptar")
entrada = input()
print(encriptar(entrada))

print("Desencriptar")
entrada2 = input()
print(desencriptar(entrada2))