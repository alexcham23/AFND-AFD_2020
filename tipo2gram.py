import os 
import menu as R
lista=[]
Nombre=""
terminales=[]
noterminales=[]
producion=[] 
banderaestado=False

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