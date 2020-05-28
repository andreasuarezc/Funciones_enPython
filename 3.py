def mostrar_mensaje(mensaje):
    print("************************************************************************")
    print(mensaje)
    print("************************************************************************")

def cargar_suma():
    valor1=int(input("Ingresar el primer valor"))
    valor2=int(input("Ingresar el segundo valor"))
    suma=valor1+valor2
    print("La suma de los dos valores es: ", suma)

#Programa principal

mostrar_mensaje("El programa calcula la suma de dos valores ingresados por teclado.")
cargar_suma()
mostrar_mensaje("Gracias por utilizar este programa")
