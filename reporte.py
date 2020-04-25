from AFD import lista
from gramatica import lista2
import graph
Alfabeto=''
Estado=''
Inicial=''
Aceptacion='' 
Transicion= ''
Nt=''
terminales=''
inition=''
Producciones=''
def menu():
    import menu 
    
    nombre= str(input("Ingrese el nombre de la gramatica o AFD\n ")) 
    op = 0
    while op != 4:
        print("=========================================================")
        print("=\t\t 1.   Ver Detalles\t\t\t=") 
        print("=\t\t 2.   Reporte general \t\t\t=") 
        print("=\t\t 3.   Menu Principal\t\t\t=") 
        print("=========================================================")
        op = str(input("Elige una opcion:\n"))       

        if op == '1' :

            detalles(nombre)
            break
        elif op == '2' :
            graph.Pdf()
            break 
        elif op == '3':  
            menu.prueba()
        else:
            menu()
def detalles(nombre): 
    global lista2,lista,Alfabeto,Estado,Inicial,Aceptacion,Transicion,Nt,terminales,inition,Producciones
    for busca in lista:
        if busca[0]== nombre:
            Alfabeto='\tAFD\nALfabeto: {'
            Estado='Estados: {'
            Inicial='Estado Inicial: {'
            Aceptacion='Estado de Aceptacion: {' 
            Transicion= 'Transiciones:\n'            
            Afd(nombre) 
    for busca1 in lista2:
        if busca1[0]== nombre:
           Nt='\tGramatica:\n\nNo Terminales: {'
           terminales='Terminales: {'
           inition='Inicio: {' 
           Producciones='Produccion: '
           gramatica(nombre) 
            
def Afd(nombre2):
    global lista,Alfabeto,Estado,Inicial, Aceptacion, Transicion
    for busca in lista: 
        if busca[0]== nombre2:
            x=0
            for buscas in busca[2]:
                if x==0:
                    Alfabeto+=buscas
                else:    
                    Alfabeto+=','+buscas
                x+=1    
            y=0
            for buscas in busca[1]:
                if y==0:
                    Estado+=buscas
                else:    
                   Estado+=','+buscas
                y+=1   
            
            for buscas in busca[3]:
                Inicial+=buscas+"}"
            z=0   
            for buscas in busca[4]:
                if z==0:
                    Aceptacion+=buscas
                else:    
                   Aceptacion+=','+buscas
                z+=1
            g=0     
            for buscas in busca[5]:
                if g==0:
                    Transicion+=buscas+'\n'
                else:    
                  Transicion+=buscas+'\n'
                g+=1   
    unir=Alfabeto+'}\n'+Estado+'}\n'+Inicial+'\n'+Aceptacion+'}\n'+Transicion     
    graph.registro(unir)
def gramatica(nombre2): 
    global lista2,Nt,terminales,inition,Producciones   
    for busca in lista2: 
        if busca[0]== nombre2:
            x=0 
            for ini in busca[1]:
               if x==0:
                   Nt+=ini
               else:
                   Nt+=','+ini   
               x+=1
            y=0   
            for bsd in busca[2]:
                if y==0:
                    terminales+=bsd
                else:
                    terminales+=','+bsd
              
            for bsd in busca[3]:
                inition=bsd+'}'
            z=0   
            for bsd in busca[2]:
                if z==0:
                    Producciones+=bsd+'\n'
                else:
                    Producciones+=bsd+'\n'
    unir=Nt+'}\n'+terminales+'}\n'+inition+'\n'+Producciones+''                
    graph.registro(unir)                  