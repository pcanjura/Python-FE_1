año = int(input('Ingrese el año: '))

if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
    print(año, 'Es año bisiesto')
else:
    print(año, 'No es año bisiesto')
