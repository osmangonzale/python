import math

a = float(input("Ingrese la longitud del cateto a: "))
b = float(input("Ingrese la longitud del cateto b: "))

c = math.sqrt(a ** 2 + b ** 2)

print("La longitud de la hipotenusa es:", c)
