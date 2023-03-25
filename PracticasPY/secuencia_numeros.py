numeros = []
rango = int(input("Ingrese la cantidad de números que desea procesar: "))

for i in range(rango):
    numero = int(input("Ingrese un número: "))
    numeros.append(numero)

for i in range(len(numeros)):
    for j in range(i+1, len(numeros)):
        if numeros[i] > numeros[j]:
            numeros[i], numeros[j] = numeros[j], numeros[i]

# Imprimir el mayor y el menor
print("El número mayor es:", numeros[-1])
print("El número menor es:", numeros[0])

# Calcular la sumatoria y el promedio
sumatoria = sum(numeros)
promedio = sumatoria / len(numeros)

# Sumatoria y el promedio
print("La suma es:", sumatoria)
print("El promedio es:", promedio)