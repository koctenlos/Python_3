# Напишите программу, которая найдёт произведение 
# пар чисел списка. Парой считаем первый и последний 
# элемент, второй и предпоследний и т.д.

# Пример:

# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import random
n = int(input('Размер массива: '))
alist = []

for i in range(n):
    alist.append(random.randint(0, 10))
print(alist)

for i in range(len(alist)):
    if i >= len(alist)/2:
        break
    # print(alist[-1-i])
    print(alist[i] * alist[-1-i], end= " ")

print()