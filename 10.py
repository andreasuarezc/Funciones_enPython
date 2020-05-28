"""Cargar por teclado una lista de enteros en el bloque principal del programa.
Elaborar tres funciones, la primera recibe la lista y retorna la suma de todos sus
elementos, la segunda recibe la lista y retorna el mayor valor y la última recibe
la lista y retorna el menor"""

def suma(lista):
    suma=0
    for x in range(len(lista)):
        suma=suma+lista[x]
    return suma

def mayor(lista):
    mayor=lista[0]
    for x in range(1,len(lista)):
        if lista[x]>mayor:
            mayor=lista[x]
    return mayor


def menor(lista):
    menor=lista[0]
    for x in range(1,len(lista)):
        if lista[x]<menor:
            menor=lista[x]
    return menor

#Bloque principal
lista=[]
print("Debes ingresar el salario de cada uno de los mienbros de tu familia. ")
respuesta="si"
while respuesta=="si":
    salario=int(input("Ingresar el salario de un miembro de tu familia: "))
    lista.append(salario)
    print(lista)
    respuesta=input("¿Deseas ingresar otro salario?. Responde si / no. ")
print(lista)
print("La suma de todos los ingresos familiares es: ")
print(suma(lista))
print("El ingreso familiar de mayor valor es: ")
print(mayor(lista))
print("El ingreso familiar de menor valor es: ")
print(menor(lista))
    
    
    
