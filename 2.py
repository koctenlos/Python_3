# Напишите программу, которая определит позицию 
# второго вхождения строки в списке либо сообщит, что её нет.
# Пример:

# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], 
# ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], 
# ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], 
# ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], 
# ищем: "123", ответ: -1
# список: [], 
# ищем: "123", ответ: -1

new_list = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
find = "йцу"
def func(new_list, find):
    n = -1
    count = 0
    for i in range(0, len(new_list)): 
        a = new_list[i] == find
        if a:
            count+=1
        if count == 2:
            return i
    return n
print(func(new_list, find))