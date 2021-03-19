from tkinter import filedialog 
import os

valor = ""
estado = 0
posM = 0
posO = 0
Menu = False
cont = 0

def may(cad):
        return (ord(cad) >= 65 and ord(cad) <= 90)

def min(cad):
        return (ord(cad) >= 97 and ord(cad) <= 122)

def numero(cad):
    return (ord(cad) >= 48 and ord(cad) <= 57)
    
def guionB(cad):
    return (ord(cad) == 95) #_

def igual(cad):
    return (ord(cad) == 61) #=

def dosP(cad):
    return (ord(cad) == 58) #:

def corcheteA(cad):
    return (ord(cad) == 91) #[
    
def corcheteC(cad):
    return (ord(cad) == 93) #]

def puntoY(cad):
    return (ord(cad) == 59) #;

def Comilla(cad): #'
     return (ord(cad) == 39)

def Coma(cad): #,
     return (ord(cad) == 44)

def Punto(cad): #.
     return (ord(cad) == 46)

def Porcen(cad): #%
     return (ord(cad) == 37)

def Espacio(cad): #Espacio
     return (ord(cad) == 32)

def salto(cad): #Salto de linea
     return (cad == "\n" or ord(cad) == 10)

def CargarArchivo():
    global pos, posi
    pos = 0
    posi = 0
    lineas = ""
    #Se una ventana emergente para elegir el archivo
    raiz = filedialog.askopenfilename (title = "Abrir") 
    fic = open(raiz, "r")
    try:
        for linea in fic:
    #se guarda todo lo que contenga el acrchivo en la vaiable lineas
            lineas = lineas + linea
        fic.close() 
    except:
        print("Ocurrio un error, cage el archivo de nuevo")
        fic.close()
    #Se hace una lista con todos los caracteres delarchivo
    caracteres = list(lineas)
    return caracteres

def cadena(cad,pos):
    global valor
    while pos != len(cad):
        if salto(cad[pos]):
            print("cararcter no valido: Salto")
            pos = pos + 1
            break
        elif Comilla(cad[pos]):
            print("Cadena: "+cad[pos])
            pos = pos + 1
            valor = ""
            break
        else:
            valor = valor + str(cad[pos])
            pos = pos + 1
    return pos
        

def leerMenu(cad):
    global posM,estado, Menu
    if estado == 0:
        while posM != len(cad):
            if cad[0] == "R" or cad[0] == "r":
                posM = 11
                while posM != len(cad):
                    if igual(cad[posM]):
                        while posM != len(cad):
                            posM = posM + 1
                            if Comilla(cad[posM]):
                                posM = posM + 1
                                print(cad[posM])
                                #posM = cadena(cad,posM)
                                estado = 1
                                break
                            elif salto(cad[posM]):
                                print("el salto no va aqui")
                                break
                            elif Espacio(cad[posM]):
                                posM = posM + 1
                            else:
                                print("carcter no valido: "+str(cad[posM]))
                                break
                    elif salto(cad[posM]):
                        print("el salto no va aqui")
                        break
                    elif Espacio(cad[posM]): 
                        posM = posM + 1
                    else:
                        print("caracter no valido: "+str(cad[posM]))
                        break
            else:
                print("Este restaurante no tiene nombre")
                break
            posM = posM + 1
    Menu = True
    estado = 0


def leerOrden(cad):
    global estado, posO
    i = 0
    if estado == 0:
        while i <= 2:
            while posO != len(cad):
                if Comilla(cad[posO]):
                    posO + posO + 1
                    posO = cadena(cad,posO)
                    while posO != len(cad):
                        if Coma(cad):
                            i += 1
                            posO + posO + 1
                            break
                        elif Espacio(cad[posO]):
                            posO + posO + 1
                        elif salto(cad):
                            print("caracter no valido: Salto")
                            i = 3
                            break
                        else:
                           print("caracter no valido: "+str(cad[pos]))
                           i = 3
                           break 
                else:
                    posO + posO + 1
    estado = 0

def CargarMenu():
    global Menu
    Menu = False
    caracteres = CargarArchivo()
    leerMenu(caracteres)

def CargarOrden():
    global Menu
    if Menu:
        caracteres = CargarArchivo()
        leerOrden(caracteres)
    else:
        print("Debe cargar un menu para generar una orden")

def GenerarMenu():
    pass

def GenerarFactura():
    pass

def GenerarArbol():
    pass

def menu():
    print("MENÚ PRINCIPAL:")
    print("1 - Cargar Menú")
    print("2 - Cargar Orden")
    print("3 - Generar Menú")
    print("4 - Generar Factura")
    print("5 - Generar Árbol")
    print("6 - Salir")
    op = input("Elija una opcion:")
    return op

while True:
    op = menu()
    os.system("cls")
    if op == "1":
        CargarMenu()
    elif op == "2":
        CargarOrden()
    elif op == "3":
        GenerarMenu()  
    elif op == "4":
        GenerarFactura()
    elif op == "5":
        GenerarArbol()
    elif op == "6":
        break
    else:
        print("Opcion no valida")
    print("")
    input("Precione enter")