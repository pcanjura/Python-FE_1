#programa para uso de operadores logicos y de comparación
# asociatividad de izquierda a derecha
a = 10
b = 5
c = 15
print(a<b and c>=a or a!=b)
# 0 and 1 or 1
# 0 or 1
# 1
print(a<b and (c>=a or a!=b))
# 0 and (1 or 1)
# 0 or 1
# 0
print(not False)