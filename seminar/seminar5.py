# def degree(a, b):
    
#     if b == 0:
#         return 1
#     else:
#         return a * degree(a, b - 1)
    
# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.


# from random import randint
# lst = [randint(1, 5) for i in range(5)]
# print(lst)

# min_el = min(lst)
# max_el = max(lst)
# print(min_el, max_el)

# out = [min_el if i == max_el else i for i in lst] 
# print(out)

# Задача №35. 
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым

# # def eyse_num(n):
# #     if n == 1:
# #         return ("no")
# #     for i in range(2, n // 2 + 1):
# #         if n % i == 0:
# #             return("no")
# #     return("yes")
# # n = int(input("введите число: "))
# # print(eyse_num(n))

# def eyse_num(n: int) -> bool:
#     if n == 2:
#         True
#     if n % 2 == 0:
#         False
#     for i in range(3, n // 2 + 1, 2):
#         if n % i == 0:
#             False
#     return True
# n = int(input("введите число: "))
# print(eyse_num(n))


# Задача №37. 
# Дано натуральное число N и последовательность из N элементов.Требуется вывести эту последовательность в обратном порядке.


# def revers_num(n):
#     if n == 0:
#         return ""
#     num = int(input())
#     return revers_num(n -1) + f"{num}"
#     # revers_num(n - 1)
#     # print(num, end=" ")
# n = int(input("введите число n:"))
# # print(f'введите последовательно {n} элементов:', end=" ")
# print(revers_num(n))
    
# Задача №39. Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. 

from random import randint
emount_arr1 = int(input("введите количество элементов первого списка: "))
emount_arr2 = int(input("введите количество элементов второго списка: "))

list1 = [randint(0, 20) for _ in range(emount_arr1)]
list2 = [randint(0, 20) for _ in range(emount_arr2)]

list3 = [item for item in list1 if item not in list2]

print(list1)
print(list2)
print(list3)

# Задача №41. Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного.
