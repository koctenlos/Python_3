# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной 
# части элементов.

# Пример:

# [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
# [4.07, 5.1, 8.2444, 6.9814] - 0.9114 или 9114

import random
n = int(input('Размер массива: '))
alist = []
new_alist = []

for i in range(n):
     alist.append(round(random.uniform(1.1, 9.9), 2))
print(alist)


            
for i in range(n):
    new_alist.append(round(alist[i]%1, 2))

alist_max = new_alist[0]
alist_min = new_alist[0]

for i in range(n):
    if new_alist[i] > alist_max: alist_max = new_alist[i]
    if new_alist[i] < alist_min: alist_min = new_alist[i]

print(f'{alist_max} - {alist_min} = {"%.2f" % (alist_max- alist_min)}')