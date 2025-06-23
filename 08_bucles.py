import os
os.system("clear")
#bubles se utilizan para generar procesos repetidamente de codigo si se culple una condicion. 
##"while"se utiliza para crear un buble 
##"break" para detener un bucle

###bucle con una condicion
contador=0
while contador <= 10:
    print(contador)
    contador+=1

##buble while y brek
contador2= 1
while contador2 <= 100:
    print(contador2)
    contador2+=1
    if contador2 % 5 == 0:
        print("divisible entre 5")
        break

## bucle con continum 
#continue sirve para saltar ese bucle y que el sistema siga al siguiente 
contador3=2
while contador3 <20:
    contador3+=1
    
    if contador3 %2==0:
        continue
    print(contador3)

##bucle con else 
#sirve para asegurarte de que se ha revisado todo y se sale del bublr
#esto con break no siempre pasa por eso esta else 
contador4=0
while contador4 <=5:
    print(contador4)
    contador4 +=1
    
else:
    print("el bucle ha terminado")

#try excep funciona para prevenir errores cuando se introducen datos incorrectos
numero = -1
while numero <0:
    try:
        numero=int(input("introduce un numero"))
        if numero <0:
            print("el numero debe ser POSITIVO. Intenta otra vez")
    except:
        print("el elemento debe ser un numero")
print(f"el numero que has introducido es el {numero}")