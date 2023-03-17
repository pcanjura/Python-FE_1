# paso de parametros por valor/referencia

# por copia
x = 2

def modificar_variable(x):
    x += 5
    return x

z = modificar_variable(x)
print(z)
print(x)

# paso por direccion de memoria
v = [2,8,1,5]
def modificar_vector(w):
    w.append(9)
    return w

t = modificar_vector(v)
print(t)
print(v)