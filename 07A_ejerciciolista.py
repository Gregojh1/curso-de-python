import os 
os.system("clear")

#Ejercicio 1: El mensaje secreto
# Dada la siguiente lista:
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".

mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]

filtrado = (mensaje [7:])
print(filtrado[0:])

# Dada la siguiente lista:
# numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.

numeros =[10, 20, 30, 40, 50, 60]
numeros[0], numeros[5] = numeros[5], numeros[0]

print(numeros)

#Ejercicio 3: El sándwich de listas
# Dadas las siguientes listas:
pan = ["pan arriba"]
ingredientes = ["jamón", "queso", "tomate"]
pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.

sandwich=(pan[0], ingredientes[0:], pan_abajo[0])
print(sandwich)

#ejercicio 4
#dada una lista, crea una lista que contenga los elementos de la lista original duplicados 
lista2= ["cocina", 1, 2, 3, 4]

duplicada= [lista2 + lista2]
print(duplicada)

# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30

lista3=[99, 69, 45, 234, 657]
medio= (lista3[2])
print(medio)

# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]

 

vsl= [23,33,43,53,63,73]
final=(vsl[3:])
princiṕio=(vsl[0:3])
princiṕio[0], princiṕio[2]=princiṕio[2],princiṕio[0]
invert=(princiṕio + final)
print(invert)