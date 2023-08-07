# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint

def index_element_list(lst, minim = 5, maxim = 15):
    index = []
    for i in range(len(lst)):
        if 5 <= lst[i] <= 15:
            index.append(i)
      
    return index
 
lst = [randint(-5, 25) for i in range(10)]  
print(f"Заданный массив: {lst} ")  
res = index_element_list(lst, minim = 5, maxim = 15)
if res:
    print(f"индексы элементов массива, значения которых принадлежат заданному диапазону: {res}")
else:
    print(" нет элементов, удовлетворяющих условию")