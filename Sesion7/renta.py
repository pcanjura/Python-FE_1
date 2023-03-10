# Programa para calcular el impuesto sobre la renta.

salario = float(input('Digite su salario: '))

sg = salario - salario*0.03
sg2 = salario - salario*0.0725

salariog = sg + sg2

if salariog <= 472.00:
    print('No es sujeto a descuento de renta')
elif salariog >= 472.01 and salariog < 895.24:
    renta = (salariog-472.00)*0.1+17.67
    print('Su impuesto es:', renta)
elif salariog > 895.25 and salariog < 2038.10:
    renta = (salariog-895.24)*0.2+60.00
    print('Su impuesto es:', renta)
elif salariog >= 2038.11:
    renta = (salariog-2038.10)*0.3+288.57
    print('Su impuesto es:', renta)
else:
    print('Gracias por su colaboracion')
