print('Programa para determinar el promedio de calificaciones')
print(" ")
cal1 = int(input('Ingrese la primera calificacion: '))
cal2 = int(input('Ingrese la segunda calificacion: '))
cal3 = int(input('Ingrese la tercera calificacion: '))
cal4 = int(input('Ingrese la cuarta calificacion: '))

nota_min = min(cal1,cal2,cal3,cal4)
promedio = (cal1 + cal2 + cal3 + cal4 - nota_min ) / 3

print(" ")
print(f'La nota minima de la practica fue: {nota_min}')
print(" ")
print(f'El promedio de notas de las practicas es: {promedio}')
print(" ")