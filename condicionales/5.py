nota1 = float(input("Ingrese la primera nota (0.0 - 5.0): "))
nota2 = float(input("Ingrese la segunda nota (0.0 - 5.0): "))
nota3 = float(input("Ingrese la tercera nota (0.0 - 5.0): "))
nota4 = float(input("Ingrese la cuarta nota (0.0 - 5.0): "))
nota5 = float(input("Ingrese la quinta nota (0.0 - 5.0): "))

promedio = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

if promedio >= 3.0:
    print("Aprobó con un promedio de", promedio)
else:
    print("No aprobó con un promedio de", promedio)
