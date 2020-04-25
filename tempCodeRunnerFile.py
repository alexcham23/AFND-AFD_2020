def menudiv():
    op = 0
    while op !=7:
        print("*************************************************")
        print("*\t 1. INGRESAR/MODIFICAR GRAMATICA \t\t\t\t*")
        print("*\t 2. GENERAR AUTOMATA DE PILA \t\t*")
        print("*\t 3. VIZUALIZAR AUTOMATA \t\t*")
        print("*\t 4. VALIDAR CADENA \t\t\t*")
        print("*\t 5. REGRESAR A LA CARATULA\t\t*")
        print("*\t 6. Salir \t\t\t\t*")
        print("*************************************************")
        op = str(input("Elige una opcion:\n"))

        if op == '1':
            os.system("cls")
            prueba()
            break
        elif op == '2':
            os.system("cls")
            #gramatica.pedirnombre()
            print("Bienvenido Amigo")
            break
        elif op == '3':
            os.system("cls")
            #gramatica.pedirnombre()
            print("Bienvenido Amigo")
            break
        elif op == '4':
            os.system("cls")
            #gramatica.pedirnombre()
            print("Bienvenido Amigo")
            break
        elif op == '5':
            os.system("cls")
            #gramatica.pedirnombre()
            retorno()
            break
        elif op == '6':
            os.system("cls")
            sys.exit()
            break
        else:
            os.system("cls")
            menudiv()
menudiv()