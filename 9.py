"""Elaborar una función que reciba tres enteros
y nos retorne el valor promedio de los mismos"""

def promedio(suma):
    return suma/3

#Bloque principal
num1=int(input("Ingresar el primer valor"))
num2=int(input("Ingresar el segundo valor"))
num3=int(input("Ingresar el tercer valor"))
suma=num1+num2+num3
print("El promedio de los valores ingresados es: ")
print(promedio(suma))


def retornar_promedio(num1,num2,num3):
    return (num1+num2+num3)/3

#Bloque principal
num1=int(input("Ingresar el primer valor"))
num2=int(input("Ingresar el segundo valor"))
num3=int(input("Ingresar el tercer valor"))
print("El promedio de los valores ingresados es: ")
print(retornar_promedio(num1,num2,num3))
