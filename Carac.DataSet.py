# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 16:18:42 2016

@author: josue
"""
#caracteristicas
#import matplotlib.pyplot as plt
import matplotlib.image as mpimg #importar una funcion de la libreria matplotlib y guardamos como mpimg
import csv#importamos libreria para archivos csv
import os#importamos librerias de sistema operativo

#inicio del programa
archivo= open('DataSetNew.csv', 'w', newline='') 
salida = csv.writer(archivo) #se transfiere el archivo a esta variable para poder escribir en el
 
def FilasEntreColumnas(tam):#Se declara la función Filas entre Columnas que recibe la variable tam
    FilasColumnas=tam[0]/tam[1] #FilasColumnas es una variable
    print("Procesando imagen: ",FilasColumnas)#Imprimimos la variable FilasColumnas para verificar el proceso
    return FilasColumnas#Devolvemos el valor de la variable como resultado de la operación
    #Segunda caracteristica
    #El area del caracter Número de Bits Blancos
def Area(tam, mat):#En esta función realizamos la busqueda de los Bits Blancos
    areaB=0 #Bits blancos
    areaN=0 #Bits negros
    for i in range(0,tam[0]): #for recorre las filas
        for j in range(0,tam[1]): #for recorre las columnas
            if(mat[i][j]!=0): #condicion para clasificar el valor del bits
                areaN=areaN+1 #si se cumple aumenta el contador de bits negros
            else:
                areaB=areaB+1 #si no cumple aumentan el contador de bits blancos
    print("Número de Blancos: " ,areaB)     
            #fin del for j
        #fin del for i  
    return areaB#Devolvemos el valor de Bits Blancos que es el resultado
        #Caracteristicas: CANTIDAD DE CORTES EN FILAS
#Tercer caracteristica número de cortes en la fila a un cuarto de la imagen 
def FilasDeCorteUnCuarto(tam,mat):#En esta caracteristica realizaremos la medida de un cuarto de la imagen
    cortes1=0#Iniciamos un contador
    CFuncuarto=int(tam[1]/4)#CFuncuarto en el resultado de nuestra operación de el tamaño de filas entre cuatro
    Aux1=mat[CFuncuarto][0]#Aux1 nos ayuda a inicializar nuestra matriz
    for i in range(0,tam[1]):#For para recorrer las filas 
        if(Aux1!=mat[CFuncuarto][i]):#Si Aux1 es diferente de a lo que contiene la matriz
            Aux1=mat[CFuncuarto][i]#Verificacion de existencia de cortes o cambios
            cortes1=cortes1+1#Entonces nuestro contador se incrementa
        #fin de condicion if
    #fin de ciclo for 
    print("Número de cortes en la fila a 1/4: ",cortes1)
    return cortes1#Retornamos el valor de nuestro contador
#Cuarta caracteristica número de cortes en la fila en medio de la imagen     
def FilasCorteEnMedio(tam,mat):#En esta caracteristica realizaremos la medida de en medio de la imagen en filas
    cortes2=0#Inicializamos nuestro contador
    CFenmedio=int(tam[0]/2)#CFenmedio es el resultado de la división de tamaño de filas entre dos
    Aux=mat[CFenmedio][0]#Aux es una variable que nos ayuda a inicializar nuestra matriz
    for i in range(0,tam[1]):#For para recorrer las filas 
        if(Aux!=mat[CFenmedio][i]):#Si Aux es diferente a lo que tenemos dentro de la matriz
            Aux=mat[CFenmedio][i]#Verificacion de existencia de cortes o cambios
            cortes2=cortes2+1#Entonces nuestro contador se incrementa
        #fin de condicion if
    #fin de ciclo for 
    print("Número de cortes en la fila de en medio: ",cortes2)
    return cortes2#Retornamos el valor de nuestro contador
#Quinta caracteristica número de cortes en la fila a tres cuartos de la imagen          
def FilasDeCorteTresCuartos(tam,mat):#En esta caracteristica realizaremos la medida a tres cuartos de la imagen en filas
    cortes3=0#Inicializamos el contador
    CFtrescuatro=int((tam[0]/4)*3)#CFtrescuartos es el resultado de nuestra operación de el tamaño de filas entre cuatro por tres
    Aux2=mat[CFtrescuatro][0]#Aux2 es una variable que nos ayuda a inicializar nuestra matriz
    for i in range(0,tam[1]):#for para poder recorrer las filas
        if(Aux2!=mat[CFtrescuatro][i]):#Si el Aux2 es diferente a lo que tenemos dentro de la matriz
            Aux2=mat[CFtrescuatro][i]#Verificación de existencia de cortes o cambios
            cortes3=cortes3+1#Entonces nuestro contador se incrementa
        #fin de condicion if
    #fin de ciclo for 
    print("Número de cortes en la fila a 3/4: ",cortes3)
    return cortes3#Retornamos el valor cortes3
        #Caracteristicas: CANTIDAD DE CORTES EN COLUMNAS
#Sexta caracteristica número de cortes en la columna a un cuartos de la imagen          
def ColumnasCortesAUnCuarto(tam,mat):#En esta caracteristica realizaremos la medida a un cuartos de la imagen en columnas
    cortes4=0#Inicializamos el contador
    CCuncuarto=int(tam[1]/4)#CCuncuarto el resultado de nuestra operación de el tamaño de columnas entre cuatro
    Aux4=mat[0][CCuncuarto]#Aux4 es una variable que nos ayuda a inicializar la matriz
    for i in range(0,tam[0]):#for para recorrer la columna
        if(Aux4!=mat[i][CCuncuarto]):#Si Aux4 es diferente a lo que tengamos en la matriz
            Aux4=mat[i][CCuncuarto]#Verificacion de existencia de cortes o cambios
            cortes4=cortes4+1#Entonces nuestro contador lo incrementamos
        #fin de condicion if
    #fin de ciclo for 
    print("Número de cortes en la columna a 1/4: ",cortes4)
    return cortes4#Retornamos el valor cortes4
#Septima caracteristica número de cortes en la columa en medio de la imagen              
def ColumnasCorteEnMedio(tam,mat):#En esta caracteristica realizaremos la medida de en medio de la imagen en columnas
    cortes5=0#Iniciaizamos nuestro contador 
    CCenmedio=int(tam[1]/2)#CCenmedio es nuestro resultado de la operacion del ancho entre dos
    Aux3=mat[0][CCenmedio]#Aux3 es una variable que nos ayuda a inicializar la matriz
    for i in range(0,tam[0]):#for para recorrer la columna
        if(Aux3!=mat[i][CCenmedio]):#Si Aux3 es diferente a lo que tengamos en la matriz
            Aux3=mat[i][CCenmedio]#Verificacion de existencia de cortes o cambios
            cortes5=cortes5+1#Entonces nuestro contador lo incrementamos
        #fin de condicion if
    #fin de ciclo for 
    print("Número de cortes en la columna de en medio: ",cortes5)
    return cortes5#Retornamos el valor cortes5
#Octava caracteristica número de cortes en la columa a tres cuartos de la imagen                  
def ColumnasCortesATresCuartos(tam,mat):#En esta caracteristica realizaremos la medida a tres cuartos de la imagen en columnas
    cortes6=0#Inicializamos un contador
    CCtrescuartos=int((tam[1]/4)*3)#CCtrescuartos es el resultado de nuestra operación de el tamaño de columnas entre cuatro por tres
    Aux5=mat[0][CCtrescuartos]#Aux5 es una variable que nos ayuda a inicializar la matriz
    for i in range(0,tam[0]):#for para recorrer la columna
        if(Aux5!=mat[i][CCtrescuartos]):##Si Aux5 es diferente a lo que tengamos en la matriz
            Aux5=mat[i][CCtrescuartos]#Verificacion de existencia de cortes o cambios
            cortes6=cortes6+1#Entonces nuestro contador lo incrementamos
        #fin de condicion if
    #fin de ciclo for 
    print("Número de cortes en la columna a 3/4: ",cortes6)
    return cortes6#Retornamos el valor de nuestro contador cortes6
        #Caracteristicas: RELACION DE AREAS EN FILAS
#Novena caracteristica la relación de pixeles blancos en la fila a un cuarto de la imagen              
def AreaDeFilasAUnCuarto(tam,mat):#En esta función encontramos el número de píxeles en la fila 1/4
    cont1=0#contador de píxeles
    uncuarto=int(tam[0]/4)#la variable uncuarto la obtenemos de la division entre cuatro para obtener un cuarto
    mat[uncuarto][0]#inicializamos la matriz
    for i in range(0,tam[1]):#for para recorrer la fila que esta a un cuarto de la imagen
        if (mat[uncuarto][i]==1):#condicion para contar píxeles
            cont1=cont1+1#si se cumple la condicion if incrementa nuestro contador 
        #fin de condicion if
    #fin de ciclo for
    print("Número de píxeles en la fila a 1/4: ",cont1)
    return cont1#retornamos el valor de nuestro contador 
#Decima caracteristica la relación de pixeles blancos en la fila de en medio de la imagen
def AreaDeFilasEnMedio(tam,mat):#En esta funcion buscamos encontrar el nùmero de pìxeles en la fila de en medio 
    cont2=0#contador de píxeles
    enmedio=int(tam[0]/2)#la variable enmedio es el resultado de la matriz entre dos en filas
    mat[enmedio][0]#inicializamos nuestra matriz
    for i in range(0,tam[1]):#For para recorrer las filas
        if (mat[enmedio][i]==1):#If es la condicion para contar los píxeles
            cont2=cont2+1#si se cumple aumenta el contador de píxeles
        #fin de condicion if    
    #fin de ciclo for
    print("Número de píxeles en la fila de en medio: ",cont2)
    return cont2 #retornamos el valor de cuestro contador
#Onceava caracteristica la relación de pixeles blancos en la fila a tres cuarto de la imagen    
def AreaDeFilasTresCuartos(tam,mat):#En esta función enconmtramos el número de píxeles en la fila 3/4
    cont3=0#Inicializamos un contador
    trescuatro=int((tam[0]/4)*3)#Para obtener tres cuartos de la imagen hacemos la division entre cuatro y la multiplicamos por tres
    mat[trescuatro][0]#inicializamos la matriz
    for i in range(0,tam[1]):##for para recorrer la fila que esta a tres cuartos de la imagen
        if (mat[trescuatro][i]==1):##condicion para contar píxeles
            cont3=cont3+1##si se cumple la condicion if incrementa nuestro contador 
        #fin de condicion if
    #fin de ciclo for            
    print("Número de píxeles en la fila a 3/4: ",cont3)
    return cont3#retornamos el valor de nuestro contador         
        #Caracteristicas RELACION DE AREAS EN COLUMNAS
#Doceava caracteristica la relación de pixeles blancos en la columna a un cuarto de la imagen    
def AreadeColumnasAUnCuarto(tam,mat):#esta funcion buscamos encontrar el nùmero de pìxeles en la columna a 1/4 de la imagen 
    cont4=0#inicializamos un contador
    Cuncuarto=int(tam[1]/4)#La variable Cuncuarto es el resultado de el nùmero de columnas entre cuatro
    mat[Cuncuarto][0]#inicializamos la matriz
    for i in range(0,tam[0]):#For para recorrer las columnas
        if (mat[i][Cuncuarto]==1):#If es la condicion para contar los píxeles
            cont4=cont4+1#si se cumple aumenta nuestro contador
        #fin de condicion if
    #fin de ciclo for 
    print("Número de píxeles en la columna a 1/4: ",cont4)
    return cont4#retornamos el valor de nuestro contador 
#Treceava caracteristica la relación de pixeles blancos en la columna de en medio de la imagen    
def AreaDeColumnasEnMedio(tam,mat):#En esta funcion buscamos encontrar el nùmero de pìxeles en la columna de en medio 
    cont5=0#inicializamo un contador 
    Cenmedio=int(tam[1]/2)#La variable Cenmedio es el resultado de la matriz entre dos en Columnas
    mat[Cenmedio][0]#Inicializamos la matriz 
    for i in range(0,tam[0]):#For para recorrer las columnas
        if (mat[i][Cenmedio]==1):#If es la condicion para contar los píxeles
            cont5=cont5+1#si se cumple aumenta nuestro contador
        #fin de condicion if
    #fin de ciclo for 
    print("Número de píxeles en la columna de en medio: ",cont5)
    return cont5#retornamos el valor de nuestro contador
#Catorceava caracteristica la relación de pixeles blancos en la columna a tres cuarto de la imagen        
def AreaDeColumnasTresCuartos(tam,mat):#esta funcion buscamos encontrar el nùmero de pìxeles en la columna a 3/4 de la imagen 
    cont6=0#inicializamos el contador
    Ctrescuatro=int((tam[1]/4)*3)#La variable Ctrescuartos hacemos la division del nùmero de columnas entre cuatro y lo multiplicamos por tres
    mat[Ctrescuatro][0]#Inicializamos la matriz
    for i in range(0,tam[0]):#for para poder recorrer las columnas 
        if (mat[i][Ctrescuatro]==1):#If si la condicion se cumple se cuentan los píxeles
            cont6=cont6+1#Se incrementa nuestro contador
        #fin de condicion if
    #fin de ciclo for 
    print("Número de píxeles en la columna a 3/4: ",cont6)
    return cont6#Retornamos el valor de nuestro contador

clase=-1 #Creamos la variable clase que servira para indicara a que numero pertenecen las caracteristicas obtenidas
root='arialSegmented' #nombre de la carpeta que contiene las imagenes
#inicia for
#dirName que indica el nombre del directorio principal y subcarpetas
#subdirList que indica las subcarpetas de cada carpeta
#fileList que proporciona una lista con los nombres de los archivos de cada carpeta
for dirName, subdirList, fileList in os.walk(root): #for para recorer los archivos de la carpeta principal
    #for para recorer las subcarpetas. fname es para obtener el nombre de cada imagen
    for fname in fileList: #for para obtener los nombre de las imagenes
        nameima=dirName+'/'+fname #obtengo la ruta de la imagen
        img=mpimg.imread(nameima) #se obtienen los datos de la imagen en una variable
        #imgplot = plt.imshow(img)
        mat=img #copio los datos de la imagen en la variable mat (es una matriz) para procesarla
        tam=mat.shape #obtengo las dimenciones de la matriz mat
        Razon=FilasEntreColumnas(tam)#Primera caracteristica Filas entre Columnas
        area=Area(tam,mat)#Segunda caracteristica El Ârea de la Imagen
        FCorteC=FilasDeCorteUnCuarto(tam,mat)#Tercer caracteristica
        FCorteM=FilasCorteEnMedio(tam,mat)#Cuarta caracteristica
        FCorteTC=FilasDeCorteTresCuartos(tam,mat)#Quinta Caracteristica
        CCortesC=ColumnasCortesAUnCuarto(tam,mat)#Sexta Caracteristica
        CCortesM=ColumnasCorteEnMedio(tam,mat)#Septima Caracteristica
        CCortesTC=ColumnasCortesATresCuartos(tam,mat)#Octava Caracteristica
        AFilasC=AreaDeFilasAUnCuarto(tam,mat)#Novena Caracteristica
        AFilasM=AreaDeFilasEnMedio(tam,mat)#Decima Caracteristica
        AFilasTC=AreaDeFilasTresCuartos(tam,mat)#DecimaPrimera Caracteristica
        AColumnasC=AreadeColumnasAUnCuarto(tam,mat)#DecimaSegunda Caracteristica
        AColumnasM=AreaDeColumnasEnMedio(tam,mat)#DecimaTercera Caracteristiva
        AColumnasTC=AreaDeColumnasTresCuartos(tam,mat)#DecimaCuarta Caracteristica
        #escribo las caracteristicas en el archivo csv
        salida.writerow([Razon,area,FCorteC,FCorteM,FCorteTC,CCortesC,CCortesM,CCortesTC,AFilasC,AFilasM,AFilasTC,AColumnasC,AColumnasM,AColumnasTC,clase])
        #Fin del segundo for
    clase=clase+1 #aumento la clase en uno cuando termine de leer una subcarpeta
    #fin del primer for
archivo.close() #Se cierra el archivo
#fin del programa 