def oferta(precio, porcentaje_descuento):
    valor_descontado = precio * porcentaje_descuento / 100
    precio_descuento = precio - valor_descontado
    return precio_descuento

def impuesto_iva(precio):
    valor_impuesto = precio * 0.13
    total_impuesto = precio + valor_impuesto
    return total_impuesto

def total_compras(carrito):
    compras = 0
    for producto, item_producto in carrito.items():
        precio = item_producto['precio']
        porcentaje_descuento = item_producto.get('descuento', 0)
        total_impuesto = impuesto_iva(precio)
        precio_descuento = oferta(total_impuesto, porcentaje_descuento)
        compras += precio_descuento * item_producto['cantidad']
    return compras


carrito = {
    'manzanas': {'precio': 1.5, 'cantidad': 3, 'descuento': 15},
    'leche': {'precio': 3, 'cantidad': 6, 'descuento': 15},
    'pan': {'precio': 2.5, 'cantidad': 5},
}

total = total_compras(carrito)
print(f"Total a pagar: {total}")




#porcentaje_descuento = 10
#impuesto = 0.13

#print(oferta(100, porcentaje_descuento))
#print(impuesto_iva(100))


