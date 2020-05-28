"""
Desarrollar una aplicación que permita ingresar por teclado los nombres de 5 artículos y sus precios.
Definir las siguientes funciones:
1) Cargar los nombres de articulos y sus precios.
2) Imprimir los nombres y precios.
3) Imprimir el nombre de artículo con un precio mayor
4) Ingresar por teclado un importe y luego mostrar todos los artículos con un precio menor igual al valor ingresado. 
"""

def articulos():
    lista_articulo=[]
    lista_precio=[]
    for x in range (5):
        articulo=input("Ingresar el nombre del artículo: ")
        lista_articulo.append(articulo)
        precio=int(input("Ingresar el precio del artículo: "))
        lista_precio.append(precio)
    return[lista_articulo, lista_precio]
        
def imprimir(listas):
    print("La lista de artículos ingresados es: ")
    print(listas[0])
    print("La lista de precios ingresados es: ")
    print(listas[1])

def mayor(listas):
    may=0
    articulo_mayor=" "
    for x in range(5):
        if listas[1][x]>may:
            may=listas[1][x]
            articulo_mayor=listas[0][x]
    return articulo_mayor

def ingresar_precio(listas):
    precio_comparacion=int(input("ingrese el valor de uno de los últimos artículos que usted compró: "))
    articulos_menor=[]
    for x in range (5):
        if listas[1][x]>=precio_comparacion:
            articulos_menor.append(listas[0][x])
    print("los artículos con un precio menor o igual al valor ingresado son: ")
    return articulos_menor
    

#Bloque principal
listas=articulos()
imprimir(listas)
print("El artículo con un precio mayor es: ")
print(mayor(listas))
print(ingresar_precio(listas))

