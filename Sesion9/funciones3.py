# retornos multiples
def dias_mes(mes):
    if mes in [12,7,8,10,1,5,3]:
        return 31
    elif mes in [4,6,11]:
        return 30
    elif mes == 2:
        return 28
    else:
        return 0
print(dias_mes(12))
# multiples valores de retorno
def aritme(a,b):
    return a+b,a-b,a*b,a/b
print(aritme(10,5))
w,x,y,z = aritme(10,4) # unpack
print(w,x,y,z)
# parametros opcionales
def suma(a,b,c=0,d=0):
    return a+b+c+d
print(suma(10,5))
print(suma(10,5,3))
print(suma(10,5,3,7))
print(suma(10,5,d=10))