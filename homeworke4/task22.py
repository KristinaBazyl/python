# задача 22. Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, 
# которые встречаются в обоих наборах.


import random


size_list_1 = int(input("введите размер первого набора чисел: "))
 # list_1 = [random.randint(0, 20) for i in range(size_list_1)]
list_1 = []
for i in range(size_list_1):
    list_1.append(random.randint(0, 20))
print(list_1)

size_list_2 = int(input("введите размер второго набора чисел: "))
list_2 = []

for i in range(size_list_2):
    list_2.append(random.randint(0, 20))
print(list_2)
list_1 = set(list_1)
list_2 = set(list_2)

intersection_list = list_1.intersection(list_2)
print(*sorted(intersection_list))