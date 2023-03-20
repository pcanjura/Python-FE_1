dEmpleados = []
while True:
    print('1. Agregar empleado')
    print('2. Imprimir lista')
    print('3. Salir')

    opcion = int(input('Seleccione una opcion: '))

    if opcion == 1:
        nombre = input('Nombre del empleado: ')
        cargo = input('Cargo del empleado: ')
        sueldo = float(input('Sueldo del empleado: '))

        empleado = {
            "nombre": nombre,
            "cargo": cargo,
            "sueldo":sueldo
        }
        dEmpleados.append(empleado)

    if opcion == 2:
        #print(dEmpleados)
        for nomina in dEmpleados:
            print(f"Nombre: {nomina['nombre']}, Cargo: {nomina['cargo']}, Sueldo: {nomina['sueldo']}")
            #print(lista)

    elif opcion == 3:
        print('Fin de la prueba...')
        break