#input introducir informacion
nombre= input("¿como te llamas?")
print(f"hola {nombre} encantado de conocerte")
age = input("que edad tienes?")
age=int(age)
print(f"tienes {age} de edad")
print(f"en 20 años tendras {age +20}")
#imprimir varios valores a la vez 
country, city= input("¿En que pais y ciudad te encuentras?").split()
print(f"vives en {country}, {city}")