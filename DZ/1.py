# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.

# Пример:

# [2, 3, 5, 9, 3] -> на нечётных позициях 
# элементы 3 и 9, ответ: 12

# alist = [2, 3, 5, 9, 3]
# print(sum(alist[1:4:2]))


import random
n = int(input('Размер массива: '))
alist = []
sum = 0
for i in range(n):
    alist.append(random.randint(0, 10))
print(alist)

# print(len(alist))

for i in range(len(alist)):
    if i % 2 == 1:
        print(alist[i], end = "+" )
        sum += alist[i]
print('=', sum)