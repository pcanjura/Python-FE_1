# programa para uso de diccionarios
# nombre: alicia
user = {
    'usuario': 'alicia',
    'correo': 'alicia@gmail.com',
    'token': 'driqoierdjakdlladfa45s6d42cs5r'
}
# acceso por llaves
print('Usuario: ',user['usuario'])
print('Correo: ',user['correo'])
print('Token: ',user['token'])
print(user)
user['usuario'] = 'alicia123'
print(user)
user['telefono'] = '123456789'
print(user)
user.pop('token')
print(user)
for valor in user.values():
    print(f'valor: {valor}')
for llave in user.keys():
    print(f'llave: {llave}')
for k,v in user.items():
    print(f'llave: {k}, valor: {v}')