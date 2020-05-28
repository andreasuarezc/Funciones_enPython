"""Crear una lista de enteros. Definir una función que reciba una lista de enteros
y un segundo parámetro de tipo entero. Dentro de la función mostrar cada elemento
de la lista multiplicado por el valor entero enviado. """

def multiplicar(lista,num):
    multiplicar_lista=[]
    for x in range (len(lista)):
        elemento=lista[x]*num
        multiplicar_lista.append(elemento)
    return(multiplicar_lista)
    

lista=[]
print("Debes crear una lista de 5 número enteros")
for x in range(5):
    entero=int(input("Ingresar un número entero: "))
    lista.append(entero)
num=int(input("Ahora debes ingresar otro número entero para multiplicarlo con los números ingresados anteriormente: "))
print("La multiplicación del último número ingresado con los números de la lista es: ")
print(multiplicar(lista,num))
        
