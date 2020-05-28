"""Confeccionar una función que reciba tres enteros y los muestre ordenados
de menor a mayor. En otra función solicitar la carga de 3 enteros por teclado
y proceder a llamar a la primer función definida. """

def mayor(num1,num2,num3):
    if num1==num2 or num2==num3 or num1==num3:
        print("Error. Al menos dos de los números ingresados tienen el mismo valor:")
    else:
        if num1>num2 and num2>num3:
            print("A continuación se mostraran los números ordenados de menor a mayor:")
            print(num3, " ", num2, " ", num1)
        else:
            if num1>num3 and num3>num2:
                print("A continuación se mostraran los números ordenados de menor a mayor:")
                print(num2," ",num3," ",num1)
            else:
                if num3>num1 and num1>num2:
                    print("A continuación se mostraran los números ordenados de menor a mayor:")
                    print(num2," ",num1," ",num3)
                else:
                    if num3>num2 and num2>num1:
                        print("A continuación se mostraran los números ordenados de menor a mayor:")
                        print(num1," ",num2," ",num3)
                    else:
                        if num2>num1 and num1>num3:
                            print("A continuación se mostraran los números ordenados de menor a mayor:")
                            print(num3," ",num1," ",num2)
                        else:
                            if num2>num3 and num3>num1:
                                print("A continuación se mostraran los números ordenados de menor a mayor:")
                                print(num1," ",num3," ",num2)

def enteros():
    print("Ingresar tres número enteros de diferente valor")
    num1=int(input("Ingresar el primer valor"))
    num2=int(input("Ingresar el segundo valor"))
    num3=int(input("Ingresar el tercer valor"))
    mayor(num1,num2,num3)

#Programa principal


enteros()
             
    
                
