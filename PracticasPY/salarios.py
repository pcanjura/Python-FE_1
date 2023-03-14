nombre = input('Escriba un nombre y un apellido: ')
dui = input('Digite su numero de DUI: ')
thoras = int(input('Digite el total de horas trabajadas: '))

hnormal = 10
hextra = 20

horasextras = thoras - 40


if thoras <= 40:
    sueldo = hnormal * thoras
    print(f'Empleado: {nombre}')
    print(f'DUI: {dui}')
    print(f'Su salario es: {sueldo}')
elif thoras > 40:
    sueldo = hnormal * (thoras - horasextras) + hextra * horasextras
    print(f'Su salario con horas extras es: {sueldo}')
