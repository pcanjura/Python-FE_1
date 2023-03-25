
def validar(email):
    if "@" and ".com" in email:
        print('La direccion es correcta')
        return True
    else:
        print('Direccion incorrecta...')
        return False
    
email = input('Ingrese su direccion de correo: ')
print(validar(email))

