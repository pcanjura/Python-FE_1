#lista = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]
lista = ['Pedro','Juan','Jose','Carlos','Andres','Pedro','Andres','Noe']

sin_duplicados = []

for elemento in lista:
    if elemento not in sin_duplicados:
        sin_duplicados.append(elemento)

print(sin_duplicados)