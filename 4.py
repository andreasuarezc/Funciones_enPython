def mostrar_mensaje(mensaje):
    print("************************************************************************")
    print(mensaje)
    print("************************************************************************")

def mayor(num1,num2,num3):
    if num1==num2 or num2==num3 or num1==num3:
       print("Error. Al menos dos de los números ingresados tienen el mismo valor") 
    else:
        if num1>num2 and num1>num3:
            print("El número mayor es: ", num1)
        else:
            if num2>num1 and num2>num3:
                print("El número mayor es: ", num2)
            else:
                print("El número mayor es: ", num3)
            
def cargar_num():
    print("Debes ingresar 3 números de diferente valor")
    num1=int(input("Ingresar el primer número"))
    num2=int(input("Ingresar el segundo número"))
    num3=int(input("Ingresar el tercer número"))
    mayor(num1,num2,num3)


#Programa principal

mostrar_mensaje("El programa muestra el número de mayor valor.")
cargar_num()
mostrar_mensaje("Gracias por utilizar este programa")
