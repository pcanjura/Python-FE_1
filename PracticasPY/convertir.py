convertir = float(input('Digite la cantidad a convertir: '))

pcolones = 8.75
pdolares = 0.11
pbitcoin = 24639.10
pEther = 1702.49
pDogecoin = 0.074

while True: 
    print('1. Colones')
    print('2. Dolares')
    print('3. Bitcoin')
    print('4. Ether')
    print('5. Dogecoin')
    print('6. Salir')

    opcion = int(input('Seleccione un tipo de moneda: '))

    if opcion == 1:
        convertir = convertir * pdolares
        print('El total en dolares es: ', convertir)
    elif opcion == 2:
        convertir = convertir * pcolones
        print('El total en colones es: ', convertir)
    elif opcion == 3:
        convertir = convertir / pbitcoin
        print('El total en Bitcoin es: ', convertir)
    elif opcion == 4:
        convertir = convertir / pEther
        print('El total en Ether es: ', convertir)
    elif opcion == 5:
        convertir = convertir / pDogecoin
        print('El total en Dogecoin es: ', convertir)
    elif opcion == 6:
        print('Fin de la prueba...')
        break
    else:
        print('Favor seleccione una opcion valida...')