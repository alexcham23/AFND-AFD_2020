import os 
import menu as R
from menu import banderamenu
from menu import menugrab2
auxiliar1=1
lista=[]
Nombre=""
terminales=[]
noterminales=[]
producion=[] 
banderaestado=False
banderatransi=False
def pedirnombre():
    global Nombre,terminales,lista,noterminales,producion
    Nombre=str(input('Ingrese el nombre de la gramatica:\n'))
    if Nombre=="" or Nombre==" " or Nombre=='\t' :
        print("por favor ingrese un nombre")
        Nombre=""
        pedirnombre()
    else:
        guardar=Nombre,terminales,noterminales,producion
        lista.append(guardar) 
    R.menugrab2()        
def terminal():
    global Nombre,lista,banderaestado
   
    estado= str(input("Ingrese el terminal:\n"))
    banderaestado=True
    bandera = False
    if estado=="" or estado=="\t" or estado.isupper():
        os.system("cls")
        terminal()
    else:   
        for busca in lista:
            if busca[0] == Nombre:
                x=0
                if not busca[1]:#verificamos si lista de estados esta vacia
                    busca[1].append(estado)
                
                elif busca[1]:# de caso contrario no esta vacia    
                    while x < int(len(busca[1])) and bandera ==False:# verificamos el tamaño de la lista estado
                        if busca[1][x] == estado:# verificamos si existe un estado repetido
                            print("este Terminal ya existe") 
                            bandera = True
                        x+=1    
                     
                    if bandera== False:#guardamos el estado si no se encuentra repetido
                        busca[1].append(estado)
def Nterminal():
    global Nombre,lista
    bandera1=False
    bandera2=False
    alfabeto=str(input("Ingrese el Terminal:\n"))
    if alfabeto=="" or alfabeto=="\t":
        os.system("cls")
        alfabeto()
    elif alfabeto.isupper():
        for busca in lista:
            if busca[0]==Nombre:
                if not busca[2]: #lista de la columna 2 esta vacia  
                    x=0
                    while x < int(len(busca[1])) and bandera1==False :
                        if busca[1][x]==alfabeto:
                            print("EL terminal "+alfabeto+" debe de ser diferente a los NO TERMINALES")
                            bandera1=True
                        x+=1
                    if bandera1== False:
                        busca[2].append(alfabeto)
                elif busca[2]:
                    if bool(alfabeto in busca[2])==False:
                        y=0
                        while y<int(len(busca[1])) and bandera2==False: 
                            if busca[1][y]==alfabeto:
                                bandera2=True
                            y+=1
                        if bandera2== False:
                            busca[2].append(alfabeto)
                        elif bandera2==True: 
                            print("EL terminal "+alfabeto+" debe de ser diferente a los NO TERMINALES")    
                    elif bool(alfabeto in busca[2])==True:
                        print("El terminal "+alfabeto+" ya existe en la Base de datos")
  
def menupreg():
    global auxiliar1,Nombre,banderamenu,banderatransi
    if banderamenu==1:
        pregunta= str(input("¿Deseas agregar un terminal? presiona (y) para continuar y (N) para regresar al menu AFD :\n"))
        if pregunta=='y' or pregunta =='Y':
            terminal()
        elif pregunta =='N' or pregunta =='n':
            os.system("cls")
            menugrab2()
        else:
            menupreg()    
    elif banderamenu==2:
        pregunta= str(input("¿Deseas agregar un No terminal? presiona (y) para continuar y (N) para regresar al menu AFD : \n"))
        if pregunta=='y' or pregunta =='Y':
            Nterminal()
        elif pregunta =='N' or pregunta =='n':
            os.system("cls")
            menugrab2()
        else:
            menupreg()
    elif banderamenu == 3:
        pregunta = str(input("¿Deseas modificar el NT Inicial ? presiona (y) para continuar y (N) para regresar al menu AFD : \n"))
        if pregunta=='y' or pregunta =='Y':
            print()
           # inicialstate()
        elif pregunta =='N' or pregunta =='n':
            if banderatransi==True:
                #unir=dfagraph+auxiliar1+auxdfagraph+'}'
               # graph.grafic(unir,nombre)
                os.system("cls")
                menugrab2()
            else:   
                os.system("cls")
                menugrab2()
        else:
            menupreg()    
    elif banderamenu==4:
        pregunta = str(input("¿Deseas ingresar mas producciones? presiona (y) para continuar y (N) para regresar al menu AFD : \n"))
        if pregunta=='y' or pregunta =='Y':
            producciones()
        elif pregunta =='N' or pregunta =='n':
            os.system("cls")
            menuAFD()
        else:
            menupreg()
    elif banderamenu== 5:  
        pregunta = str(input("¿Deseas ingresar mas transiciones? presiona (y) para continuar y (N) para regresar al menu AFD : \n"))
        if pregunta=='y' or pregunta =='Y':
           # modo1()
           mostrar()
        elif pregunta =='N' or pregunta =='n':
            if banderatransi==True:
               # unir=dfagraph+auxiliar1+auxdfagraph+'}'
               # graph.grafic(unir,nombre)
                os.system("cls")
                menuAFD()
            else:   
                os.system("cls")
                menuAFD()
        else:
            menupreg()      
    elif banderamenu==6:  
        print()
           
    else:
        menupreg()                         