import sys
import os
import AFD
import gramatica
import Archivo
import reporte
import tipo2gram as tip
banderamenu=0
def retorno():
    os.system("cls")
    prueba()
def prueba():
    op = 0
    while op != 7:
        print ("*************************************************")
        print("*\t 1. Crear AFD \t\t\t\t*")
        print("*\t 2. Crear Gramatica     \t\t*")
        print("*\t 3. Evaluar Cadenas     \t\t*")
        print("*\t 4. Reportes \t\t\t\t*")
        print("*\t 5. Cargar Archivo de Entrada   \t*")
        print("*\t 6. Gramatica Tipo2 y AP\t*")
        print("*\t 7. Salir \t\t\t\t*")
        print("*************************************************")
        op = str(input("Elige una opcion:\n"))       

        if op == '1' :
            os.system("cls")
            AFD.pedirnombre()
            break
        elif op == '2' :
            os.system("cls")
            gramatica.pedirnombre()
            break
        elif op == '3' :
            os.system("cls")
            gramatica.valinombre()
            break
        elif op == '4' :
            os.system("cls")
            reporte.menu()
            break
        elif op == '5' :
            os.system("cls")
            Archivo.menuarchivo()
            break
        elif op == '6' :
            os.system("cls")
            tip.pedirnombre()
            break
        elif op == '7' :
            
            sys.exit()
            
            break

def menudiv():
    op = 0
    while op !=6:
        print("*************************************************")
        print("*\t 1. INGRESAR/MODIFICAR GRAMATICA \t*")
        print("*\t 2. GENERAR AUTOMATA DE PILA \t\t*")
        print("*\t 3. VIZUALIZAR AUTOMATA \t\t*")
        print("*\t 4. VALIDAR CADENA \t\t\t*")
        print("*\t 5. REGRESAR A LA CARATULA\t\t*")
        print("*\t 6. Salir \t\t\t\t*")
        print("*************************************************")
        op = str(input("Elige una opcion:\n"))

        if op == '1':
            os.system("cls")
            menugrab2()
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
            sys.exit()
            break
        else:
            os.system("cls")
            menudiv()
def menugrab2():
    global banderamenu
    op = 0
    while op !=6:
        print("*************************************************")
        print("*\t 1. Ingresar terminales \t*")
        print("*\t 2. Ingresar no Terminales \t\t*")
        print("*\t 3. Ingresar Producciones\t\t*")
        print("*\t 4. Borrar Producciones \t\t\t*")
        print("*\t 5. No terminal Inicial\t\t*")
        print("*\t 6. Regresar al Menu Principal \t\t\t\t*")
        print("*************************************************")
        op = str(input("Elige una opcion:\n"))

        if op == '1':
            banderamenu=1
            os.system("cls")
            tip.terminal()
            break
        elif op == '2':
            banderamenu=2
            os.system("cls")
            #gramatica.pedirnombre()
            print("Bienvenido Amigo")
            break
        elif op == '3':
            banderamenu=3
            os.system("cls")
            #gramatica.pedirnombre()
            print("Bienvenido Amigo")
            break
        elif op == '4':
            banderamenu=4
            os.system("cls")
            #gramatica.pedirnombre()
            print("Bienvenido Amigo")
            break
        elif op == '5':
            banderamenu=5
            os.system("cls")
            #gramatica.pedirnombre()
            retorno()
            break
        elif op == '6':
            sys.exit()
            break
        else:
            os.system("cls")
            menudiv()               
retorno()
