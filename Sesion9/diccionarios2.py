u1 = {
    'id': 1,
    'usuario': 'alicia',
    'correo': 'alicia@gmail.com',
    'token': 'dsfyiwyrewtruewygcvxcvssadfgyq',
    'rol': {1: 'admin', 2: 'gerente',}
}
u2 = {
    'id': 2,
    'usuario': 'beto',
    'correo': 'beto@gmail.com',
    'token': 'qwwerrfgdgbbmnuyitrwqszcxcvcbe',
    'rol': {3: 'ventas', 4: 'user', 5: 'rrhh'},
}
lista_usuarios = []
lista_usuarios.append(u1)
lista_usuarios.append(u2)
# como imprimo el correo de beto a partir de la lista?
print(lista_usuarios[1]['correo'])
# como imprimo el rol admin de alicia?
print(lista_usuarios[0]['rol'][1])
# como imprimir todos los roles de beto con un for?
for k, v in lista_usuarios[1]['rol'].items():
    print(k, v)
