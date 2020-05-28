"""
En una empresa se almacenaron los sueldos de 10 personas.
Desarrollar las siguientes funciones y llamarlas desde el bloque principal:
1) Carga de los sueldos en una lista.
2) Impresión de todos los sueldos.
3) Cuántos tienen un sueldo superior a $4000.
4) Retornar el promedio de los sueldos.
5) Mostrar todos los sueldos que están por debajo del promedio
"""

def cargar_sueldo():
    lista=[]
    for x in range(10):
        sueldo=int(input("Ingresar el salario de un empleado: "))
        lista.append(sueldo)
    return lista

def imprimir_sueldos(lista):
    print(lista)
    
def sueldo_superior(lista):
    sup=[]
    cantidad=0
    for x in range (10):
        if lista[x]>4000:
            sup.append(lista[x])
            cantidad=cantidad+1
    return [sup, cantidad]

def promedio(lista):
     suma=0
     for x in range(10):
         suma=suma+lista[x]
     promedio=suma/10
     return promedio
    
def inferior_promedio(lista,promedio):
    count=[]
    for x in range(10):
        if lista[x]<promedio:
            count.append(lista[x])
    return count

#Bloque Principal
lista=cargar_sueldo()
print("La lista de salarios ingresados es: ")
imprimir_sueldos(lista)
variable=sueldo_superior(lista)
print("La cantidad de sueldos superiores a 4000 es: ",variable[1])
print("La lista de sueldos superiores a 4000 es: ",variable[0])
print("El promedio de los sueldos es: ")
promedio=promedio(lista)
print(promedio)
print("La lista de sueldos por debajo del promedio es: ")
print(inferior_promedio(lista,promedio))


