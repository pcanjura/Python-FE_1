print("Aprovecha esta oportunidad de obtener un 15% de descuento en estos productos,")
print("Al comprar 3 docenas o más y 10% de descuento en menos de 3 docenas")

precio1 = 4.00
precio2 = 3.00
precio3 = 2.00

while True:
    print('1. Suavizante 500ml - $4.00 x Und')
    print('2. Desinfectante 500ml - $3.00 x Und')
    print('3. Limpiador 500ml - $2.00 x Und')
    print('4. Salir')

    opcion = int(input('Seleccione un producto: '))


    if opcion == 1: 
        cantidad = int(input('Digite la cantidad de docenas: '))
        if cantidad >= 3:
            mCompra = cantidad * 12 * precio1
            descuento1 = mCompra * 0.15
            total = mCompra - descuento1
            regalo = cantidad * 1
            print('El total de su compra es: ', mCompra)
            print('El su descuento es de: ', descuento1)
            print('El total de su compra con descuento es: ', total)
            print(f'Por su preferencia recibirá {regalo} articulos más a su pedido.')
        else:
            mCompra = cantidad * 12 * precio1
            descuento2 = mCompra * 0.10
            total = mCompra - descuento2
            print('El total de su compra es: ', mCompra)
            print('El su descuento es de: ', descuento2)
            print('El total de su compra con descuento es: ', total)
    if opcion == 2:
        cantidad = int(input('Digite la cantidad de docenas: '))
        if cantidad >= 3:
            mCompra = cantidad * 12 * precio1
            descuento1 = mCompra * 0.15
            total = mCompra - descuento1
            regalo = cantidad * 1
            print('El total de su compra es: ', mCompra)
            print('El su descuento es de: ', descuento1)
            print('El total de su compra con descuento es: ', total)
            print(f'Por su preferencia recibirá {regalo} articulos más a su pedido.')
        else:
            mCompra = cantidad * 12 * precio1
            descuento2 = mCompra * 0.10
            total = mCompra - descuento2
            print('El total de su compra es: ', mCompra)
            print('El su descuento es de: ', descuento2)
            print('El total de su compra con descuento es: ', total)
    if opcion == 3:
        cantidad = int(input('Digite la cantidad de docenas: ')) 
        if cantidad >= 3:
            mCompra = cantidad * 12 * precio1
            descuento1 = mCompra * 0.15
            total = mCompra - descuento1
            regalo = cantidad * 1
            print('El total de su compra es: ', mCompra)
            print('El su descuento es de: ', descuento1)
            print('El total de su compra con descuento es: ', total)
            print(f'Por su preferencia recibirá {regalo} articulos más a su pedido.')
        else:
            mCompra = cantidad * 12 * precio1
            descuento2 = mCompra * 0.10
            total = mCompra - descuento2
            print('El total de su compra es: ', mCompra)
            print('El su descuento es de: ', descuento2)
            print('El total de su compra con descuento es: ', total)
    elif opcion == 4:
        print('Fin de la prueba...')
        break
    else:
        print('Favor seleccione un producto valido...')