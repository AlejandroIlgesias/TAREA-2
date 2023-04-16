#FUNCINES AUXILIARES

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

    #UNA VEZ OBTENIDA LA LISTA ORDENADA Y AKMACENADA EN UNA VARIABLE SOLO QUEDA FABRICAR EL DICCIONARIO
    diccionario={"Asistencia":"","Parcial1":"","Parcial2":"","Ordinario1":"",
             "Ordinario2":"","Practicas":"","OrdinarioPracticas":""}
    
    lista_final=[]
    for o in lista_ordenada:
        
        diccionario["Asistencia"]=o[2]
        diccionario["Parcial1"]=o[3]
        diccionario["Parcial2"]=o[4]
        diccionario["Ordinario1"]=o[5]
        diccionario["Ordinario2"]=o[6]
        diccionario["Practicas"]=o[7]
        diccionario["OrdinarioPracticas"]=o[8]
        copia=diccionario.copy()
        lista_final.append(copia)

    return lista_final




