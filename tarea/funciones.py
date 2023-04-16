#FUNCIONES AUXILIARES

def ordenar(lista):
    #OBTENER LAS PRIMERAS LETRAS DE LOS APELLIDOS DE LAS 17 LISTAS Y LOS INDICES DE LAS LISTAS A LAS QUE 
    #PERTENECEN

    #ALAMACENA UNA LISTA DE LISTAS;CADA LISTA DENTRO DE letras TIENE DOS ELEMENTOS,EL PRIMERO ES LA PRIMERA LETRA DEL APELLIDO Y
    #EL SEGUNDO ES EL INDICE DE LA LISTA DE 9 ELEMENTOS QUE SE ENCUENTRA DENTRO DE LA VARIABLE LLAMADA LISTA EN LA LINEA 9.
    letras=[]
    for indice in range(len(lista)):
        letras.append([(lista[indice][0][0]),indice])
        

    #EL PRIMER ELEMENTO EN LETRAS ES LA PRIMERA LETRE DE LA LISTA QUE REALIZA DESCRIPCION DE LO QUE HAY EN CADA POSICION 
    # DE LAS RESTANTES LISTAS,NO CONTIENE LA INFORMACION DE NINGUN ALUMNO.ES LA LINEA UNO DEL ARCHIVO calificaciones.csv.
    #POR ESO LO QUITO.
    del letras[0]


    #ORDENO LOS ELEMNTOS DE LA LISTA letras BASANDOME EN EL ORDEN DE LAS LETRAS.

    for i in range(1,len(letras)):
        letra=letras[i][0]
        if (i-1)<=(len(letras)-1):
            elemento=letras[i]
        #Se guarda el índice del elemento anterior en j
        j=i-1
        #Muevo todos los elementos de la lista hacia la 
        #derecha si son mayores que el elemento almacenado
        #en letra

        while j>=0 and letras[j][0]>letra:
            letras[j+1]=letras[j]
            j=j-1

        #Inserto el elemento

        letras[j+1]=elemento

    #ALMACENAMOS EN ESTA LISTA LOS INDICES EN EL MISMO ORDEN EN EL QUE HEMOS ORDENADO LOS ELEMENTOS DE letras
    indice_para_cambiar=[]
    for p in range(len(letras)):
        indice_para_cambiar.append(letras[p][1])

    #UNA VEZ ALMACENADOS DE ESTA FORMA,LO ÚNICO QUE QUEDA ES ORDENAR LA LISTA ORIGINAL,letras ,EN BASE AL APELLIDO.
    #PARA ESO CREO UNA LISTA VACIA,lista_ordenada, DONDE ALMACENAMOS LOS ELEMENTOS DE LA LISTA letras PERO ORDENADOS
    
    lista_ordenada=[]
    for k in indice_para_cambiar:
        lista_ordenada.append(lista[k])

    #OBTENEMOS EL DICCIONARIO
    
    diccionario={"Apellidos":"","Nombre":"","Asistencia":"","Parcial1":"","Parcial2":"","Ordinario1":"",
             "Ordinario2":"","Practicas":"","OrdinarioPracticas":""}
    final=[]
    
    for o in lista_ordenada:
        diccionario["Apellidos"]=o[0]
        diccionario["Nombre"]=o[1]
        diccionario["Asistencia"]=o[2]
        diccionario["Parcial1"]=o[3]
        diccionario["Parcial2"]=o[4]
        diccionario["Ordinario1"]=o[5]
        diccionario["Ordinario2"]=o[6]
        diccionario["Practicas"]=o[7]
        diccionario["OrdinarioPracticas"]=o[8]
        z=diccionario.copy()
        final.append(z)
    
    return final

'''FUNCION QUE AÑADE Y CALCULA LA NOTA FINAL'''

def añadir(list_ordenada):
    #OBTENEMOS LAS CLAVES DEL DICCIONARIO Y LA METEMOS EN UNA LISTA
    claves=list(list_ordenada[2].keys())
    '''> ['Apellidos','Nombre','Asistencia', 'Parcial1', 'Parcial2', 'Ordinario1', 'Ordinario2', 'Practicas', 'OrdinarioPracticas']'''


    #CAMBIO LAS CADENAS VACIAS DE LAS CLAVES POR CEROS Y LAS COMAS POR PUNTOS

    claves=list(list_ordenada[0].keys()) #LISTA CON LAS CLAVES DEL DICCIONARIO

    for indice in range(len(list_ordenada)):
        for elemento in claves:

            if list_ordenada[indice][elemento]=="":
                list_ordenada[indice][elemento]=0
            
            if (isinstance((list_ordenada[indice][elemento]),str)) and ("," in list_ordenada[indice][elemento]):
                list_ordenada[indice][elemento]=list_ordenada[indice][elemento].replace(",",".")

    #UNA VEZ CAMBIADOS ESOS VALORES PUEDO CALCULAR LAS NOTAS
    for f in range(len(list_ordenada)):
        nota_final=(0.3*(float(list_ordenada[f][claves[3]])))+(0.3*(float(list_ordenada[f][claves[4]])))+(0.4*(float(list_ordenada[f][claves[7]])))

        #AÑADO UNA NUEVA CLAVE A CADA DICCIONARIO: SU NOTA FINAL
        list_ordenada[f]["NotaFinal"]=round(nota_final,2)

    return list_ordenada

'''FUNCION PARA CLASIFICAR LOS ALUMNOS EN APROBADOS Y SUSPENSOS '''

def clasificar(lista_diccionarios):
    #OBTENEMOS LAS CLAVES DE LOS DICCIONARIOS
    claves=list(lista_diccionarios[0].keys())
    '''['Apellidos', 'Nombre', 'Asistencia', 'Parcial1', 'Parcial2', 'Ordinario1', 'Ordinario2', 'Practicas', 'OrdinarioPracticas', 'NotaFinal']'''

    #PASO LOS PORCENTAJES DE ASISTENCIA A CADENAS TRANSFORMABLES POR LA FUCION int() PARA PODER COMPARARLOS DESPUES
    for indice in range(len(lista_diccionarios)):
            for elemento in claves:
                
                if (isinstance((lista_diccionarios[indice][elemento]),str)) and ("%" in lista_diccionarios[indice][elemento]):
                    lista_diccionarios[indice][elemento]=lista_diccionarios[indice][elemento].replace("%","")
                    

    #QUEDA PARTIR LA LISTA
    aprobados=[]
    suspensos=[]

    for l in range(len(lista_diccionarios)):
        
        if ((int(lista_diccionarios[l][claves[2]])>=75)and((float(lista_diccionarios[l][claves[3]])>=4)and(float(lista_diccionarios[l][claves[4]])>=4)and
                                                        (float(lista_diccionarios[l][claves[7]])>=4))) and(float(lista_diccionarios[l][claves[9]])>=5):
            
            aprobados.append(lista_diccionarios[l])
        else:
            suspensos.append(lista_diccionarios[l])

    #DEVUELVO LAS LISTAS EN UNA TUPLA DE DOS ELEMENTOS

    return(aprobados,suspensos)
    