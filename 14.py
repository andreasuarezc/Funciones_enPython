"""
Confeccionar un programa que permita:
1) Cargar una lista de 10 elementos enteros.
2) Generar dos listas a partir de la primera. En una guardar los valores positivos y en otra los negativos.
3) Imprimir las dos listas generadas. 
"""

def lista_enteros():
    lista=[]
    for x in range(10):
        num=int(input("Ingresar un número entero,  puede ser positivo o negativo: "))
        lista.append(num)
    return lista

def dos_listas(lista):
    positivos=[]
    negativos=[]
    for x in range(10):
        if lista[x]>0:
            positivos.append(lista[x])
        else:
            if lista[x]<0:
                negativos.append(lista[x])
    return[positivos, negativos]

def imprimir_listas(listas):
    print("La listas de los valores positivos ingresados es: ")
    print(listas[0])
    print("La listas de los valores positivos ingresados es: ")
    print(listas[1])

    
#Bloque principal

lista=lista_enteros()
listas=dos_listas(lista)
imprimir_listas(listas)

