nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

if edad < 0 or edad > 100:
    print("Por favor, ingrese una edad válida (entre 0 y 100 años).")
else:
    if edad >= 18:
        print("Hola,", nombre + ". Usted es mayor de edad.")
    else:
        print("Hola,", nombre + ". Usted es menor de edad.")
