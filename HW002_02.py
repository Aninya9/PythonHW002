s = int(input("Введите сумму чисел, s: "))
p = int(input("Введите произведение, p: "))

import math

D = s**2 - 4*p
if (D >= 0):
    D = math.sqrt(D)
    D1 = D*10
    if (D1 % 10 == 0):
        x = int((s - D) / 2)
        y = int((s + D) / 2)
        print(x, y)
    else:
        print('Попробуйте другие числа')
else:
    print('Нет таких чисел')