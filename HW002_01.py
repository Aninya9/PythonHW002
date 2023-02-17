n = int(input("Введите количество монет: "))

orel = 0
resh = 0

i=0

array = []

for i in range(n): 
    array[i] = int(input('Орел (0) или решка (1)?: ')) 
    if (array[i] == 0):
        orel += 1
    else:
        resh += 1
    i+=1


