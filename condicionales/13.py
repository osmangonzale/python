P = float(input("Ingrese el peso en kilogramos: "))
E = float(input("Ingrese la estatura en metros: "))

IMC = P / (E * E)

estado = ""
if IMC < 18.5:
    estado = "Desnutrido"
elif 18.5 <= IMC < 25:
    estado = "Normal"
elif 25 <= IMC < 30:
    estado = "Sobrepeso"
elif 30 <= IMC < 35:
    estado = "Obesidad Grado 1"
elif 35 <= IMC < 40:
    estado = "Obesidad Grado 2"
else:
    estado = "Obesidad Grado 3"

print(f"Su IMC es {IMC:.2f}, lo que se clasifica como: {estado}")
