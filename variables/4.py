from datetime import datetime
año_actual = datetime.now().year

año_nacimiento = int(input("Ingrese su año de nacimiento: "))

edad = año_actual - año_nacimiento

print("Usted tiene", edad, "años de edad.")
