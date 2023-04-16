import csv
from funciones import ordenar,añadir,clasificar

fichero=open("calificaciones.csv",newline="")
leer_fichero=csv.reader(fichero,delimiter=";")

lista1=[]
for x in leer_fichero:
    lista1.append(x)
fichero.close()

#DICCIONARIOS
lista_ord=ordenar(lista1)

#AÑADIMOS NOTA FINAL

lista_2=añadir(lista_ord)

#CLASIFICAMOS LA LISTA EN APROBADOS Y SUSPENSOS

aprobados,suspensos=clasificar(lista_2)




