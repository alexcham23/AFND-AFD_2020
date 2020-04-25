
import sys
import os
import AFD
import gramatica
import Archivo
import reporte
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
            menudiv()
            break
        elif op == '7' :
            os.system("cls")
            sys.exit()
            
            break


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
