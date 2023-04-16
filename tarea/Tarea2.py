import csv



fichero=open("calificaciones.csv",newline="")
leer_fichero=csv.reader(fichero,delimiter=";")


lista1=[]
for x in leer_fichero:
    lista1.append(x)
fichero.close()

#LISTA ORDENADA


#OBTENEMOS LOS DICCIONARIOS






