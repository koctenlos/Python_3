# Напишите программу, которая будет преобразовывать 
# десятичное число в двоичное. Подумайте, 
# как это можно решить с помощью рекурсии.

# print(bin(5))

a = int(input("Введите число: "))
b = ""

while a>0:
    b = str (a % 2) + b
    a = a // 2

print(b)