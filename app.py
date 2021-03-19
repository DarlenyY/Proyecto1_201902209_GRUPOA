from tkinter import filedialog 
import os

tablaSimbolos = []
tablaAtributos = []
fila = 0
columna = 0
flagExpresionId = False
flagExpresionCadena = False
flagExpresionNumero = False
valor = ""
estado = 0
temp = None
flagAutomataObjeto = False
pos = 0
posi = 0
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

def error(simbolo,expectativa,linea,columna):
    print("Error, no se reconoce el simbolo: " + simbolo + ", se esperaba: " + expectativa + " linea: " + str(linea) + ", columna: " + str(columna) )

def identificador(cad):
    global valor, pos, columna
    encontrado = False
    while pos != len(cad):
        if valor == "":
            if min(cad[pos]):
                valor = valor + str(cad[pos])
                columna = columna + 1
                pos = pos + 1
                while pos != len(cad):
                    if min(cad[pos]) or numero(cad[pos]) or guionB(cad[pos]):
                        valor = valor + str(cad[pos])
                        columna = columna + 1
                        pos = pos + 1 
                    elif puntoY(cad[pos]):
                    #tengo que añadir a la lista de id
                        print("*Id: "+valor)
                        columna = columna + 1
                        pos = pos + 1 
                        valor = ""
                        encontrado = True
                        break
                    else:
                        pos = pos + 1
                        columna = columna + 1
            else:
                    pos = pos + 1
                    columna = columna + 1
        if encontrado:
            break

def titulo(cad):
    global valor, pos, columna
    encontrado = False
    while pos != len(cad):
        if valor == "":
            if igual(cad[pos]):
                pos = pos + 1
                while pos != len(cad) and encontrado == False:
                    if Comilla(cad[pos]):
                        pos = pos + 1
                        while pos != len(cad):
                            if Comilla(cad[pos]):
                                print(valor)
                                pos = pos + 1
                                columna = columna + 1
                                valor=""
                                encontrado = True
                                break
                            else:
                                valor = valor + str(cad[pos])
                                pos = pos + 1
                                columna = columna + 1
                    else:
                        pos = pos + 1
                        columna = columna + 1 
            else:
                    pos = pos + 1
                    columna = columna + 1
        if encontrado:
            break

def cadena(cad):
    global valor, pos, columna
    encontrado = False
    while pos != len(cad):
        if Comilla(cad[pos]):
            while pos != len(cad):
                pos = pos + 1
                columna = columna + 1
                if puntoY(cad[pos]):
                    print("**nombreProd: "+valor)
                    encontrado = True
                    break
                elif dosP(cad[pos]):
                    print("Sección: "+valor)
                    encontrado = True
                    break
                elif corcheteC(cad[pos]):
                    print("****descripcion: "+valor)
                    encontrado = True
                    break
                else:
                    pos = pos + 1
                    columna = columna + 1
        else:
            valor = valor + str(cad[pos])
            columna = columna + 1
            pos = pos + 1
        if encontrado:
            valor = ""
            break

def precio(cad):
    global valor, pos, columna
    encontrado = False
    while pos != len(cad):
        if Punto(cad[pos]):
            valor = valor + str(cad[pos])
            pos = pos + 1
            if numero(cad[pos]) == False:
                valor = valor + "00"
                print("***Precio: "+valor)
                encontrado = True
                pos = pos + 1
                valor = ""
                break
            elif numero(cad[pos]):
                valor = valor + str(cad[pos])
                pos = pos + 1
                columna = columna + 1
                if numero(cad[pos]):
                    valor = valor + str(cad[pos])
                    pos = pos + 1
                    columna = columna + 1
                else:
                   valor = valor + "0" 
                while pos != len(cad):
                    if puntoY(cad[pos]):
                        print("***Precio: "+valor)
                        encontrado = True
                        valor = ""
                        pos = pos + 1 
                        break 
                    else:
                        pos = pos + 1              
        elif numero(cad[pos]):
            valor = valor + str(cad[pos])
            pos = pos + 1
            columna = columna + 1
        else:
            valor = valor + ".00"
            while pos != len(cad):
                    if puntoY(cad[pos]):
                        print("***Precio: "+valor)
                        encontrado = True
                        valor = ""
                        pos = pos + 1 
                        break 
                    else:
                        pos = pos + 1  
        if encontrado:
            encontrado = False
            break

def leerMenu(cad):
    global pos, valor,columna, Menu
    Rep = 0
    while pos!=(len(cad)):
        if corcheteA(cad[pos]):
            pos = pos + 1
            columna = columna + 1
            while pos!=(len(cad)):
                if min(cad[pos]):
                    identificador(cad)
                    break
                else:
                    pos = pos + 1  
        elif Rep == 0:
            if (str(cad[0])=="R" or str(cad[0])=="r"):
                pos = pos + 1
                columna = columna + 1
                titulo(cad)
                Rep = 1
        elif Comilla(cad[pos]):
            pos = pos + 1
            columna = columna + 1
            cadena(cad)
        elif numero(cad[pos]):
            precio(cad)
        elif Espacio(cad[pos]):
            pos = pos + 1
            columna = columna + 1
        else:
            pos = pos + 1
            columna = columna + 1
    Menu = True

def cantidad(cad):
    global valor, posi
    while posi != len(cad):
        if numero(cad[posi]):
            valor = valor + str(cad[posi])
            posi = posi + 1
        elif Coma(cad[posi]):
            print("cant: "+valor,end=" ")
            valor = ""
            break
        elif posi+1 == len(cad):
            break
        else:
           posi = posi + 1  
            
def venta(cad):
    global valor, posi
    valor = valor + str(cad[posi])
    posi = posi + 1
    while posi != len(cad):
        if min(cad[posi]) or guionB(cad[posi]) or numero(cad[posi]):
            valor = valor + str(cad[posi])
            posi = posi + 1
        elif salto(cad[posi]) or posi == len(cad):
            print("Id: "+valor)
            valor = ""
            break
        else:
            posi = posi + 1

def porcentaje(cad):
    global valor, posi
    while posi != len(cad):
        if numero(cad[posi]):
            valor = valor + str(cad[posi])
            posi = posi + 1
        elif Punto(cad[posi]):
            valor = valor + str(cad[posi])
            posi = posi + 1
        elif Porcen(cad[posi]):
            if float(valor) <= 100.00:
                print("Porcentaje: "+valor)
                posi = posi + 1
                break
            else:
                print("el porcentaje  no es valido")
                posi = posi + 1
                break
        else:
           posi = posi + 1 

def datos(cad):
    global valor, posi, cont
    encontrado = False
    while posi != len(cad):
        if Comilla(cad[posi]):
            if cont == 0:
                print("Nombre: "+valor)
                valor = ""
                encontrado = True
                posi = posi + 1
                break 
            elif cont == 1:
                print("Nit: "+valor)
                valor = ""
                encontrado = True
                posi = posi + 1
                break 
            elif cont == 2:
                while posi != len(cad):
                    if Coma(cad[posi]):
                        print("Direccion: "+valor)
                        valor = ""
                        posi = posi + 1
                        cont = 0
                        while posi != len(cad):
                            if numero(cad[posi]):
                                porcentaje(cad)
                                encontrado = True
                                break
                            else:
                                posi = posi + 1
                    else:
                        posi = posi + 1 
                    if encontrado:
                        break 
        else:
            valor = valor + str(cad[posi])
            posi = posi + 1
        if encontrado:
            break
        

def leerOrden(cad):
    global posi, valor,columna,cont
    uno = False
    while posi!=(len(cad)):
        if Comilla(cad[posi]):
            posi = posi + 1   
            datos(cad)
            cont = cont + 1
        elif salto(cad[posi]):
            posi = posi + 1
            cantidad(cad)
            if Coma(cad[posi]):
                posi = posi + 1 
                while posi!=(len(cad)):
                    if min(cad[posi]):
                        venta(cad)
                        uno = True
                    else:
                        posi = posi + 1 
                    if uno:
                        break
            else:
                posi = posi + 1
        else:
            posi = posi + 1 

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
    except:
        print("Ocurrio un error, cage el archivo de nuevo")
    finally:
        fic.close()
    #Se hace una lista con todos los caracteres delarchivo
    caracteres = list(lineas)
    return caracteres

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
    input("")