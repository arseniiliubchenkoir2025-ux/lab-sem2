import math
#-----------Variabels-----------#

a = 7.5
b = 10
h = 0.2
x = a

while x <= b + 1e-9:
    if x <= 8:
        f = ((a ** 2) -1) ** (a - 1)
    elif 8 < x <= 9:
        f = (1 / (math.sin(a) + math.cos(a)))
    else:
        f = math.log(math.exp(a) + 4)
    print(f'f = {f}')
    x += h