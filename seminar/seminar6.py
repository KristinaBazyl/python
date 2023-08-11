# Задача №39. Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. 

from random import randint
# emount_arr1 = int(input("введите количество элементов первого списка: "))
# emount_arr2 = int(input("введите количество элементов второго списка: "))

# list1 = [randint(0, 20) for _ in range(emount_arr1)]
# list2 = [randint(0, 20) for _ in range(emount_arr2)]

# list3 = [item for item in list1 if item not in list2]

# print(list1)
# print(list2)
# print(list3)

# Задача №41. Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного.

# lst1 = [randint(1, 10) for _ in range(10)]
# print(lst1)
# counter = 0

# for i in range(1, len(lst1) - 1):
#     if lst1[i -1] < lst1[i] > lst1[i +1]:
#         counter += 1
# print(counter)



# print( lst1 := [randint(0, 10) for _ in range(10)])
# print(sum([1 for i in range(1, len(lst1) - 1) if lst1[i -1] < lst1[i] > lst1[i + 1]]))

# Задача №43. Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару, которую необходимо посчитать

# lst = [1, 2, 3, 2, 3, 3]
# print(sum([lst.count(item) // 2 for item in set(lst)]))

lst = [1, 2, 3, 2, 3, 3]
counter =0
for item in set(lst):
    counter += lst.count(item) // 2
print(counter)