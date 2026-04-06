import  math

a = 0.1
b = 0.5
h = 0.05
d = 0.001
x = a

while x <= b + d:
    m = 3
    n = 1
    total = 1
    while True:
        temp = 1
        for k in range(n):
            temp *= m + k
        math_fun = (temp / math.factorial(n) * (x ** n))
        total += math_fun

        if abs(math_fun) < d:
            break
        n += 1

    print(f'x = {round(x ,1)}  , suma = {round(total , 1)}')
    x += h
