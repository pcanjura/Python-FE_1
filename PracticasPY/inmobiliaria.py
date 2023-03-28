
def buscar_inmuebles(inmuebles, presupuesto):
    lista_resultado = []
    for inmueble in inmuebles:
        zona = inmueble['zona']
        metros = inmueble['metros']
        habitaciones = inmueble['habitaciones']
        garaje = inmueble['garaje']
        antiguedad = 2023 - inmueble['año']
        if zona == 'A':
            precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1 - antiguedad/100)
        elif zona == 'B':
            precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1 - antiguedad/100) * 1.5
        if precio <= presupuesto:
            inmueble_con_precio = inmueble.copy()
            inmueble_con_precio['precio'] = precio
            lista_resultado.append(inmueble_con_precio)
    return lista_resultado


inmuebles = [{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
            {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
            {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
            {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
            {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}
            ]

resultado = buscar_inmuebles(inmuebles, 125000)

for inmueble in resultado:
    print(inmueble)