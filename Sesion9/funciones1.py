# programa para uso de funciones

# sin valor de retorno
def mi_primera_funcion(nombre):
    print(f'Hola {nombre}, bienvenido a Python')

mi_primera_funcion('alicia')
mi_primera_funcion('alicia')
mi_primera_funcion('alicia')
mi_primera_funcion('alicia')

# con valor de retorno
def suma(a, b):
    c = a + b
    return c

x = suma(5, 20)
print(x)
print(suma(10, 5))

y = mi_primera_funcion('eva')
print(y)
suma(30,10)