import os
os.system("clear")
#listas: secuencias mutablesd de elementos se utilizan corchetes []
lista1= [1,2,3,4,5,6,7,8,9,10]
lista2:list[str, int,float]=["manzanas", "peras", "guisantes"]

#matricez 
lista_matriz=[2,"calcentin"],[5.7],[7,8]
lista_vacia=[]

#acceso por indice: se tiene que escribir el nombre de la lista y escribir la posicion que quieres agarrar 
##El cero es la primera posicion de izquierda a derecha

print(lista2[0])
print(lista_matriz[0][1])

print(lista1[1:4])#la ultima pocision(4) no la toma 
print(lista1[:3])# buscar las primeras 3 posicione 
print(lista2[:]) #copia las listas 
print(lista1[::2]) #pedir numeros salteados, dos en dos, tres en tres, etc
lista2[0]="rojo" #modificar datos de una lista 
print(lista2)
lista2+= [99,"rojo", 78]
print(lista2)