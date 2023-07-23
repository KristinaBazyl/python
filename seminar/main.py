# По данному целому неотрицательному n вычислите значение n!.
# N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1
# Решить задачу используя цикл while

# n = int(input("Введите число"))
# factorial_n = 1
# i = 1
# while i <= n:
#     factorial_n = factorial_n*i
#     i += 1
# print(factorial_n)



# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является,
# то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи,
# выведите число -1.

# n = 3
# f1 = 1
# f2 = 2
# fn = 0
# count = 4
# # if n == 0:
# #     print("1")
# # elif n == 1:
# #     print("2")
# while n > f2:
#     fn = f1 + f2
#     f1 = f2
#     f2 = fn
#     count += 1
#     # print(f2)
# if f2 == n:
#     print(count)
#
# else:
#     print("-1")
#
# import random
#
# amount = int(input("Введите количество арбузов: "))
# min_weight = 30
# max_weight = 0
# for i in range(amount):
#     melon = random.randint(1, 30)
#     print(melon)
#     if melon < min_weight:
#         min_weight = melon
#     if melon > max_weight:
#         max_weight = melon
# print(min_weight, max_weight)

# Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю наблюдений за погодой.
# Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые годы.
# Их интересует, сколько дней длилась самая длинная оттепель. Оттепелью они называют период,
# в который среднесуточная температура ежедневно превышала 0 градусов Цельсия. Напишите программу,
# помогающую синоптикам в работе.

# import random
# days = 30
# temper = 0
# counter = 0
# max_warmdays = 0
# for i in range(days):
#     temper = random.randint(-10, 10)
#     print(temper, end=" ")
#     if temper > 0:
#         counter += 1
#         if counter > max_warmdays:
#             max_warmdays = counter
#     else:
#         counter = 0
# print()
# print(max_warmdays)
n = int(input("Введите число: "))
i = 0

while 2**i <= n:
    print(2**i, end=" ")
    i += 1
