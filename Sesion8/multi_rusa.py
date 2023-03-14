a = int(input('digite un primer numero: ')) # multiplicador
b = int(input('digite un segundo numero: ')) # multiplicando

sum = 0

while a>=1:
    if a % 2 != 0:
        sum = sum + b
        a = a / 2
        b = b * 2
        
print(f'la multiplicacion es: {sum}')
