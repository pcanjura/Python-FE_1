# Programa para uso de sets

equipos = {'Barcelona','Real Madrir','Manchester City','Juventus','Munich'}
print(len(equipos))
# Son desordenados
print(equipos)
# No son indexadas
# print(equipos[0])
# Son inmutables
# equipos[0] = 'Dortmund' ----> esto brinda error
# Si son dinamicos

equipos.add('Aguila')
print(equipos)
equipos.discard('Juventus')
print(equipos)

for equipo in equipos:
    print(f'Equipo: {equipo}')

# No acepta repetidos
equipos.add('Munich') # lo ejecuta pero no lo agrega, pero si diferencia entre minusculas y mayusculas
equipos.add('munich') # aqui se agrega como un elemento mas 
print(equipos)