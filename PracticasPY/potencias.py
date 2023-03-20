print('Calculando potencias de un numero')

print("")

numero = int(input('Ingrese el numero deseado: '))
exponente = int(input('Ingrese el exponente que desea calcular: '))

print("")

contador = 1 
resultado = 1

for contador in range(exponente):
    resultado = resultado * numero
    contador = contador + 1
print(f'La potencia del {numero} es {resultado}')