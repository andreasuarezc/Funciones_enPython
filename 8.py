"""Confeccionar una función que le enviemos como parámetro un string y nos
retorne la cantidad de caracteres que tiene. En el bloque principal solicitar
la carga de dos nombres por teclado y llamar a la función dos veces. Imprimir
en el bloque principal cual de las dos palabras tiene más caracteres."""


def string(nombre1,nombre2):
    if len(nombre1)>len(nombre2):
        return (nombre1, " es la palabra con más caracteres")
    else:
        if len(nombre2)>len(nombre1):
            return (nombre2, "es la palabra con más caracteres")
        else:
            return("Los nombres ingresados tienen igual cantidad de caracteres")

def nombres():
    nombre1=input("Ingresar el primer nombre")    
    nombre2=input("Ingresar el segundo nombre")
    print(string(nombre1,nombre2))

#Bloque principal
nombres()
    
    
