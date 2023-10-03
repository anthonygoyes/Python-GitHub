from InterfazMenu import menu
import  DefAritmeticas as df


while True:
    opcion = menu()
    if opcion==1:
        num1=int(input("Primer numero "))
        num2=int(input("Segundo numero "))
        print("El resultado es ", df.suma(num1, num2))
    elif opcion==8:
        break #Salir del while
    else:
        print("Opcion no valida")
        

