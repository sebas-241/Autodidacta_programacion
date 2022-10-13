
from math import sin, cos, tan #IMPORTAR DESDE MATH

def calculadora (f: str, n: int):  # FUNCION CON DICCIONARIO DEFINIENDO EN CLAVES Y VALORES LO QUE SE VA A USAR
    aritmetico={
        "seno": sin,
        "coseno": cos,
        "tangente": tan
    }
    
    resultado = dict()  # CREACION DE DICCIONARIO VACIO
    for valores in range(n,n+1): # MENCION DE UNA NUEVA VARIABLE PONIENDO UN RANGO ESPECIFICO +1 
        resultado[valores] = aritmetico[f](n) # DEFINIENDO UNA NUEVA VARIBLE TENIENDO EN CUENTA EL FOR DANDO LOS PARAMETROS DE LA FUNCION
    return (resultado) # RETORNANDO DATOS DE LA VARIABLE ESTABLECIDA ANTERIORMENTE

def main (): # CREACION DE UNA NUEVA VARIABLE
    a = input("Ingrese la funcion a utilizar: seno, coseno o tangente: ") 
    b = int(input("Ingrese un valor entero: "))
    print(calculadora(f=a, n=b)) # IMPRIMIR ASOCIANDO LA PRIMERA FUNCION CON SUS PARAMETROS Y ASOCIANDOLOS A LOS INPUTS
    
main() # MUESTRA DE RESULTADO
    