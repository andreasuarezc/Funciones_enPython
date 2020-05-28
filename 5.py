def perimetro(lado):
    return lado*4

def superficie(lado):
    return lado*lado

def lado():
    lado=float(input("Ingresa el lado del cuadrado: "))
    respuesta=input("Si deseas calcular el perimetro del cuadrado escribe p \n O si deseas calcular su superficie escribe s: ")
    if respuesta=="p":
        print("El perimetro del cuadro es: ", perimetro(lado))
    else:
        if respuesta=="s":
            print("La superficie del cuadrado es: ",superficie(lado))

#Programa principal

lado()
