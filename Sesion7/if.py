# programa para uso de condiciones simples y anidadas
# captura de datos por teclado
# conversion de cadena a entero
edad = input('Digite su edad: ')
print('Su edad es:', edad)
print('Tipo de dato:', type(edad)) #el tipo de dato de Edad se muestra como un Str

aux_edad = int(edad) # se asigna edad a una nueva variable para convertir a entero. 
print('Tipo de aux_edad:', type(aux_edad)) # muestra el tipo de dato de edad ya con el cambio

if aux_edad>18:
    print('Es adulto')
    print('Es mayor de edad')
    if aux_edad>60:
        print('y es de la tercera edad')
else:
    print('Es menor de edad')

print('Fin del programa....adios')