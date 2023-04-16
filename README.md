# TAREA-2

MI REPOSITORIO:
https://github.com/AlejandroIlgesias/TAREA-2.git

Las funciones pedidas son:
(1)Una funcion que reciba el fichero de calificaciones y devuelva una lista de diccionarios,donde cada diccionario contiene la informacion de los exámenes y la asistencia de un alumno.La lista tiene que estar ordenada por apellidos.

La fucion que resuelve este problema se encuentra en el archivo funciones.py,llamada ordenar.Esta funcion toma un solo parametro ,el cual es una lista de listas.Lo primero que hace es ordenar los elementos de esta lista por orden alfabetico.En este caso ,el primer elemento de cada lista es una cadena de caracteres la caul contiene el apellido de cada alumno.
El bucle for utiliza el objeto iterable creado por la funcion range.Los valores que toma la variable indice coinciden  con los indices de los elementos de la lista metida como parametro de la funcion.Dentro de este bucle,a la lista vacia creada que he llamado letras le añado a traves del metodo append una lista de dos elementos,el primero es una cadena de caracteres que se corresponde con la primera letra del apellido que se encuentra en la lista cuya posicion viene dada por la variable indice del bucle for y el segundo elemento es un numero entero el cual está alamcenado en dicha variable.
Es decir , un elemento de la lista llamada letras tiene esta forma:
[letra,indice de la lista a la que pertenece dicha letra]

Una vez tengo la lista letras completa,quito el primer elemento,debido a que este se refiere a la primera linea del archivo calificaciones.csv,y dicha linea simplemente sirve para identificar los elementos de las restantes lineas,no contiene informacion alguna de ningun alumno.

Despues procedo a ordenar la lista usando un algortimo de ordenacion conocido como insert sort.Este algoritmo separa la lista en dos partes, ordenadas y no ordenadas. También supone que el primer elemento está ordenado, luego pasa al siguiente elemento que lo voy a llamar Y por ejemplo; comparamos Y con el primero, si es mayor, se queda como está pero si es más pequeño, copia el primer elemento en la segunda posición e inserta Y como primero.

Una vez ordenadas las letras,coloco sus indices en el mismo orden en el que se encuentran.Los almaceno en una lista vacia que he creado previamente llamada indice_para_cambiar.

Lo último que queda es ordenar la lista original,la que he pasado como argumento a la funcion,usando la lista indice_para_cambiar.

Para eso creo una lista vacia,lista_ordenada, donde almaceno los elementos de la lista original ordenados.

Una vez tengo la lista ordenada,creo un diccionario con los datos de la linea 1 del archivo calificaciones.csv como claves  igualadas a una cadena vacía.

Usando un bucle for para acceder a cada elemento de cada lista declaro los valores de cada clave y el diccionario resultante lo copio y lo almaceno en la variable z.Por último el diccionario lo almaceno en la lista vacia que creé previamente llamada final.

Esta lista es la que devuelve la función.


(2)Una función que reciba una lista de diccionarios como la que devuelve la función anterior y añada a cada diccionario un nuevo par con la nota final del curso. El peso de cada parcial de teoría en la nota final es de un 30% mientras que el peso del examen de prácticas es de un 40%.

La funcion tambien se encuentra en el archivo funciones.py.Se llama añadir y toma como parametro una lista de diccionarios.

Lo primero que hace es obtener las claves comunes a todos los diccionarios de la lista a traves del metodo keys() aplicado a uno de los diccionarios que la integran y las almacena en forma de lista en la variablie que declaré con el nombre de claves.

Despues cambio las cadenas vacias de las claves por ceros y las  comas por puntos,ayudandome con las funciones replace(), que reemplaza una subcadena de una cadena por otra, y isinstance() que indica si el dato pasado como primer parametro es una clase hija del dato/objeto pasado como segundo parametro.

Una vez hecho eso,simplemente queda calcular la nota final de cada alumno usando un bucle for y las funciones int() y float() aplicadas a las cadenas de caracteres almacenadas en las claves Parcial1,Parcial2 y Practicas.
Por último añado una nueva clave a cada diccionario llamada NotaFinal y el valor que le doy es el almacenado en la variable nota_final.

Finalmente la funcion devuelve la lista de diccionarios con el nuevo par NotaFinal:numero(float).

(3)Una función que reciba una lista de diccionarios como la que devuelve la función anterior y devuelva dos listas, una con los alumnos aprobados y otra con los alumnos suspensos. Para aprobar el curso, la asistencia tiene que ser mayor o igual que el 75%, la nota de los exámenes parciales y de prácticas mayor o igual que 4 y la nota final mayor o igual que 5.

Esta funcion tambien se encuentra en el archivo funcion.py
Se llama clasificar.
Tiene un solo argumento,el cual es una lista de diccionarios.
Lo primero que hace es obtener las claves del diccionario y las almacena en la variable claves en forma de lista.

Despues usando un bucle for y la funcion replace() cambio el caracter % de la cadena almacenada en la clave Asistencia de cada diccionario por una cadena vacia,para mas adelante a la hora de realizar las comparaciones poder aplicar la funcion int() sin que salte una excepcion.

Por último a través de un bucle for compruebo que se cumplen todas las condiciones pedidas en el apartado (3) del ejercicio ,para saber si meter el diccionario en la lista declarada previamente almacenada en la variable llamada aprobados o en la llamada suspensos.

Por último,una vez repartidos todos los diccionarios entre las dos listas,las devuelvo en una tupla,donde la primera tupla es la lista de alumnos aprobados y la segunda es la lista de los alumnos suspensos.





