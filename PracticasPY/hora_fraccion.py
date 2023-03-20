print('Total a pagar por estacionamiento, precio $1.50 hora o fraccion')
print(" ")

horas = int(input('Ingrese las horas que utilizo el estacionamiento: '))
minutos = int(input('Ingrese los minutos que estuvo estacionado: '))
print(" ")

pago = (horas * 1.50) + 1.50

print(f'El tiempo de parqueo utilizado es de: {horas} horas con {minutos} minutos')
print(f"El pago por uso del parqueo es: ${pago}")

print(" ")























#if hora_in<=hora_out and minut_out>=minut_in:
#    tiempo1 = hora_out - hora_in
#    tiempo2 = minut_out - minut_in
#    print(f'El tiempo de parqueo utilizado es de: {tiempo1}:{tiempo2}')
#elif hora_in<=hora_out and minut_out<=minut_in:
#    tiempo1 = hora_out - hora_in
#    tiempo2 = minut_in - minut_out
#    print(f'El tiempo de parqueo utilizado es de: {tiempo1}:{tiempo2}')