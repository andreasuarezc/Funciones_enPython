def string (cadena):
    y=len(cadena)
    vocales=0
    x=0           
    for x in range (y):        
        if (cadena[x])=="a" or (cadena[x])=="e" or (cadena[x])=="i" or (cadena[x])=="o" or (cadena[x])=="u" or (cadena[x])=="á" or (cadena[x])=="é" or (cadena[x])=="í" or (cadena[x])=="ó" or (cadena[x])=="ú" or (cadena[x])=="A" or (cadena[x])=="E" or (cadena[x])=="I" or (cadena[x])=="O" or (cadena[x])=="U":
            vocales=vocales+1
    print(vocales)

def mensaje():
    cadena=input("Ingresa una frase corta. ")
    print("La cantidad de vocales que contiene la frase es: ")
    string(cadena)


#Programa principal

for x in range (3):
    mensaje()
