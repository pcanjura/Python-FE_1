agenda = []

while True:
    print('1. Registrar cliente')
    print('2. Modificar cliente')
    print('3. Mostrar agenda')
    print('4. Precione "*" para salir')

    opcion = int(input('Seleccione una opcion: '))

    if opcion == 1:
        nombre = input('Nombre del cliente: ')
        telefono = int(input('Numero de telefono: '))

        cliente = {
            'nombre': nombre,
            'telefono': telefono
        }

        agenda.append(cliente)

    if opcion == 2:
        input('Ingrese el nombre del contacto a modificar: ')

    if opcion == 3:
        for lista in agenda:
            print(f"Nombre: {lista['nombre']}, Telefono: {lista['telefono']}")
    
    if opcion == '*':
        print('Fin del programa')
        break