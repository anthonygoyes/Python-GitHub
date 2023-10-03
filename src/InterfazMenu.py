def menu():
    while True:
        print("=====Menu=====")
        print("1) Suma")
        print("2) Resta")
        print("3) Multiplicacion")
        print("4) Divicion")
        print("5) Potencia")
        print("6) Raiz Cuadrada")
        print("7) Factorial")
        print("8) Salir")
        
        opcion = input("Opcion: ")
        
        if opcion.isdigit():  # Verifica si la entrada es un número
            return int(opcion)  # Convierte la entrada a un entero y lo retorna
        else:
            print("Entrada no válida. Por favor, ingrese un número válido.")
            


