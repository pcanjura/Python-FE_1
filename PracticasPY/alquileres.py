distancia = int(input('Ingreses los KM recorridos: '))

tarifa = 30
iva = 0.13

if distancia <= 300:
    subtotal = tarifa / 1.13
    impuesto = tarifa - subtotal
    total = subtotal + impuesto
    print('Subtotal: ', subtotal)
    print('IVA 13%: ', impuesto)
    print('Total a pagar: ', total)
elif distancia > 300 and distancia <= 1000:
    distancia2 = distancia - 300
    costo = distancia2 * 0.25 + tarifa
    subtotal = costo / 1.13
    impuesto = costo - subtotal
    total = subtotal + impuesto
    print('Subtotal: ', subtotal)
    print('IVA 13%: ', impuesto)
    print('Total a pagar: ', total)
elif distancia > 1000:
    distancia2 = distancia - 1000
    costo = distancia2 * 0.50 + tarifa
    subtotal = costo / 1.13
    impuesto = costo - subtotal
    total = subtotal + impuesto
    print('Subtotal: ', subtotal)
    print('IVA 13%: ', impuesto)
    print('Total a pagar: ', total)
else:
    print('Gracias por su preferencia...')
