num1=float(input("introduzca un numero"))
num2=float(input("introduzca otro numero"))

if num1>num2:
    print("{num1} es mayor a{num2}")
elif num2>num2:
    print("{num2}es mayor a{num1}")

oper=input("elige una operacion(+,-,*,/)")

if oper=="+":
    total_a= num1 + num2
    print(f"el resultado es: {total_a}")
elif oper=="-":
    total_b= num1 - num2
    print(f"el resultado es: {total_b}")
elif oper=="*":
    total_c = num1*num2
    print(f"el resultado es: {total_c}")
if num1==0:
    print("error")
elif oper=="/":
    total_d= num1 / num2
    print(f"el resultado es: {total_d}")   

#ejercicio 3
anio = int(input("Introduce un año: "))

if anio / 4 == 0 or anio / 100 != 0:
    print(f"{anio} es un año bisiesto.")
if anio / 400 == 0:
    print(f"{anio} no es un año bisiesto.")
   #ejercicio 4

age= int(input("introduzca su edad"))
if age >= 0 and age <=12:
    print("nino")
elif age >= 13 and age <=18:
    print("adolescente")
elif age >=19 and age <=60:
    print("adulto")
elif age >=61 and age <=90:
    print("anciano")