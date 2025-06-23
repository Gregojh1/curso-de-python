###BUCLES CON FOR 
#Permiten ejecutar un bloque de codigo infitamente mientras itera un iterable o  una lista 

#iterar una lista 
frutas = ["manzana","pera","limon","durazno"]
for fruta in frutas:
    print(fruta)

#iterar sobre letras 
cadenas="gregorio"

for caracteres in cadenas:
    print(caracteres)

#enumerate se utiliza para enumerar las propiedades que tiene una lista
frutas = ["manzana","pera","limon","durazno"]
for index, value in enumerate(frutas):
    print(f"el indice es {index} y la fruta es {value}")

#anidar listas con bucles 

numeros=[1,2,3]
letras=["a","b","c"]

for letra in letras:
    for numero in numeros:
        print(f"{letra}*{numero}")

#para ver como funcionan los bucles o codigos entrar en python tutor 
# python tutor sirve para explicarte como funciona el codigo 

#bucles for con break

animales=["loro", "perro","gato", "raton","ballena"]
for animal in animales:
    print(animal)
    if animal == "raton":
        break
##tambien podemos enumerarlo 
for index, animal in enumerate(animales):
    if animal =="raton":
        print (f"el raton esta en la pocision numero {index}")
        break #cuando llega al raton se detiene el bucle

#bubles con continue 
animales=["loro","perro","gato","raton","ballena"]
for animal in animales:
    if animal == "raton":
        continue #nos saltaremos el raton y seguira al proximo animal
    print(animal)

