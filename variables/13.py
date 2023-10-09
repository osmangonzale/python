tiempo_segundos = int(input("Ingrese una cantidad de tiempo en segundos: "))

horas = tiempo_segundos // 3600 

segundos_restantes = tiempo_segundos % 3600
minutos = segundos_restantes // 60  

print("Tiempo en horas:", horas)
print("Tiempo en minutos:", minutos)
