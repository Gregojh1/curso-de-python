# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
print("\nEjercicio 1:")
contador=10
while contador>1:
    print(contador)
    contador -= 1

    # Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
numero=1
suma = 0
while numero <=20:
    if numero  % 2 == 0:
        suma + numero
        print(f"el numero{numero} es par")
    numero +=1       

# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 12

numerob = int(input("introduce un numero del 1 al 5"))
factorial = numero * 1
while numerob <=5:
    numerob *= contador
    contador+= 1 

print(f"el factorial es {factorial}")

 #Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida"

contraseña ="" 

while len(contraseña)<8:
    mensaje= (input("introduce una contraseña")
              if len(contraseña) <8:
                print("la contraseña debe tener 8 elementos")
              if len(continue) => 8:
                print("contraseña aceptada")
                


    
