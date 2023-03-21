print(" ")

dia = int(input('Ingrese el día del mes: '))
mes = int(input('Ingrese el mes: '))
año = int(input('Ingrese el año: '))

print(" ")
diasMas = int(input('Ingrese los días adicionales: '))

while diasMas > 0:    
    if mes == 2:
        if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
            dias_mes = 29
        else:
            dias_mes = 28
    elif mes in [4, 6, 9, 11]:
        dias_mes = 30
    else:
        dias_mes = 31

    dFaltantes = dias_mes - dia

    if diasMas > dFaltantes:
        # Agregando los días restantes al mes actual
        dia = 0
        diasMas -= dFaltantes
        mes += 1
        if mes > 12:
            mes = 1
            año += 1
    else:
        # Agregando los días que quedan a la fecha actual
        dia += diasMas
        diasMas = 0
print(" ")
print(f'La nueva fecha es: {dia}/{mes}/{año}')
