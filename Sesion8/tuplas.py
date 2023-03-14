# Programa para uso de tuplas

lenguajes = ('Python','C++','PHP','Perl',100,(2,3,4))
print(len(lenguajes))
print(lenguajes)
print(lenguajes[0])
# NO SON MUTABLES, NO SE PUEDEN MODIFICAR
# lenguajes[2] = 'C#' ---> esto brindaria error
# son estaticas
# lenguajes.append(1) ----> esto brincaria error

for lenguaje in lenguajes:
    print(f'Lenguajes: {lenguaje}')