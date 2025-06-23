import os
os.system("clear")
#condicionales if elif else
edad1 = 80
if edad1 >=18:
    print("puedes pasar al casino")
if edad1 <=17:
    print("no puedes pasar")
#else se usa para imprimir una sola opcion entre dos
if edad1>= 60:
    print("descuento en el casino")
else:
    print("no tienes el descuento")

#elif para hacer bifurcaciones 
nota = 9
if nota >= 5 and nota <= 7:
    print("aprobado")
elif nota >= 8:
    print("sobresaliente")
elif nota <= 4:
    print("desaprobado")
#operadores logicos or and 

dni=False
edad=80
if edad >= 20 and dni:
    print("puedes manejar")
else:
    print("NO PUEDES MANEJAR ")

#or and not
if edad <= 60 or dni:
    print("puede trabajar")
else:
    print("no puede trabajar")

dinero=100
cuenta=True
if dinero>= 300:
    if cuenta:
        print("prestamo aprobado")
else:
     print("rechazado")

#operadores de comparadores

## = asignacion
## == comparacion / igualdad 
## => igual o mayor
## <= igual o menor 
## != desigualdad  

#ternario if-else
##codigo si cumple la condicion {if} condicion {else} sino cumple
edad2= 60
mensaje = "es tercera edad" if edad2 >= 60 else "es laburante"
print(mensaje)