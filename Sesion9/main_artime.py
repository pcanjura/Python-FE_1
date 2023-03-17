import mate.aritme

print(mate.aritme.suma(10,5))

from mate import aritme

print(aritme.resta(10,5))

from mate.aritme import *

print(suma(10,5))
print(resta(10,5))
print(multi(10,5))
print(divi(10,5))

input()

import os

os.system('clear')

print('pantalla limpiada')