# TAREA-2
Las funciones pedidas son:
1)Una funcion que reciba el fichero de calificaciones y devuelva una lista de diccionarios,donde cada diccionario contiene la informacion de los exámenes y la asistencia de un alumno.La lista tiene que estar ordenada por apellidos.

La fucion que resuelve este problema se encuentra en el archivo funciones.py,llamada ordenar.Esta funcion toma un solo parametro ,el cual es una lista de listas.Lo primero que hace es ordenar los elementos de esta lista por orden alfabetico.En este caso ,el primer elemento de cada lista es una cadena de caracteres la caul contiene el apellido de cada alumno.
El bucle for utiliza el objeto iterable creado por la funcion range.Los valores que toma la variable indice coinciden  con los indices de los elementos de la lista metida como parametro de la funcion.Dentro de este bucle,a la lista vacia creada que he llamado letras le añado a traves del metodo append una lista de dos elementos,el primero es una cadena de caracteres que se corresponde con la primera letra del apellido que se encuentra en la lista cuya posicion viene dada por la variable indice del bucle for y el segundo elemento es un numero entero el cual está alamcenado en dicha variable.
Es decir , un elemento de la lista llamada letras tiene esta forma:
[letra,indice de la lista a la que pertenece dicha letra]

Una vez tengo la lista letras completa,quito el primer elemento,debido a que este se refiere a la primera linea del archivo calificaciones.csv,y dicha linea simplemente sirve para identificar los elementos de las restantes lineas,no contiene informacion alguna de ningun alumno.

Despues procedo a ordenar la lista usando un algortimo de ordenacion conocido como insert sort.Este algoritmo separa la lista en dos partes, ordenadas y no ordenadas. También supone que el primer elemento está ordenado, luego pasa al siguiente elemento que lo voy a llamar Y por ejemplo; comparamos Y con el primero, si es mayor, se queda como está pero si es más pequeño, copia el primer elemento en la segunda posición e inserta Y como primero.

Una vez ordenadas las letras,coloco sus indices en el mismo orden en el que se encuentran.Los almaceno en una lista vacia que he creado previamente llamada indice_para_cambiar.

Lo último que queda es ordenar la lista original,la que he pasado como argumento a la funcion,usando la lista indice_para_cambiar.
