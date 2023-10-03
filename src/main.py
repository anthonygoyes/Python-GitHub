from InterfazMenu import menu

def main():
    while True:
        opcion = menu()
        if opcion==1:
            #1
        elif opcion==2:
            #opcion2
        elif opcion==3:
            #opcion3
        elif opcion==4:
            #opcion4
        elif opcion==5:
            #opcion5
        elif opcion==6:
            #opcion6
        elif opcion==7:
            #opcion7
        elif opcion==8:
            break #Salir del while
        else:
            print("Opcion no valida")
            

if __name__ == "__main__":
    main()