# programa para uso de listas

nombres = ['alicia', 'beto', 'carlos', 'diana', 100, [2,5,3]]
#longitud
print(len(nombres))
# son ordenadas
print(nombres)
# son indexadas 
print(nombres[3])
print(nombres[5][2])
# son mutables
nombres[2] = 'eva'
print(nombres)
#son dinamicas
nombres.append('fran')
print(nombres)
nombres.remove(100)
print(nombres)
#son iterables
for nombre in nombres:
    print(f'Nombre: {nombre}')