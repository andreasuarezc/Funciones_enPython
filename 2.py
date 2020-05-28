def introduccion():
    print("Vamos a cargar valores enteros y a mostrar su suma")
    print("**************************************************")
    
def suma():
    num1=int(input("Ingresar el primer valor"))
    num2=int(input("Ingresar el segundo valor"))
    suma=num1+num2
    print("La suma de los valores ingresados es: ", suma)
def separador():
    print("**************************************************")

#Programa principal

introduccion()

for x in range (5):
    suma()
    separador()
