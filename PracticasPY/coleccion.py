dEmpleados = {}
id = 0
while True:
    print('1. Agregar empleado')
    print('2. Imprimir lista')
    print('3. Salir')

    opcion = int(input('Seleccione una opcion: '))

    if opcion == 1:
        nombre = input('Nombre del empleado: ')
        cargo = input('Cargo del empleado: ')
        sueldo = float(input('Sueldo del empleado: '))

        dEmpleados[id] = [nombre, cargo, sueldo]
        id = id + 1
    if opcion == 2:
        for k, v in dEmpleados.items():
            print(k, v)
    elif opcion == 3:
        print('Fin de la prueba...')
        break
    else:
        print('Opcion incorrecta...')


