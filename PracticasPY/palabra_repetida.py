
def palabra_repetida(frase):

    palabras = frase.lower().split()

    diccionario = {}

    for palabra in palabras:
        if palabra in diccionario:
            diccionario[palabra] += 1
        else:
            diccionario[palabra] = 1
    # Devolver el diccionario resultante
    return diccionario

frase = input('Ingrese la frase deseada: ')

print(palabra_repetida(frase))


