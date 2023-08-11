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
    
