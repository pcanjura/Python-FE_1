# Verificar si una palabra es Palindroma


def palabra(cadena):
    cadena_invertida = ""
    for letra in cadena:
        cadena_invertida = letra + cadena_invertida
    return cadena_invertida

print(palabra('anilina'))
print(palabra('anona'))

