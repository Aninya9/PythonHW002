n = int(input("Введите число n: "))

i = 1
while 2**i < n:
    print(2**i)
    i+=1
    if 2**i >= n:
        break
