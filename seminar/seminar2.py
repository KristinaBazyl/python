# # задача 17:
# # дан список. найти сколько в нем уникальных чисел
#
# lst = [1, 1, 2, 0, -1, 3, 4, 4]
# # lst = len(sen(lst)) создание множества длинной списка, во множестве не повторяются элементы
# # print(len(lst))
# unico_item = []
# for i in range(len(lst)):
#     if lst[i] not in unico_item:
#         unico_item.append(lst[i])
#
# print(len(unico_item))


# задача сдвинуть список из n элементов на K значений
# import random
# # array = []
# # len_ar = int(input("введите длинну списка: "))
# # for i in range(len_ar):
# #     array[i] = random.randint(0, 20)
# #     print(array)
#
# len_ar = int(input("введите длинну списка: "))
# array = [random.randint(0, 20) for i in range(len_ar)]
# print(array)
# #
# # k = 3
# # # new_list = array[3:] + array[:3]
# # # print(new_list)
# # for i in range(1, k+1):
# #     array = array[-1:] + array[:-1]
# # print(array)
#
#
# # циклически запускать и повторять список можно
#
#
# shift = int(input("введите сдвиг: "))
# for i in range(len(array)):
#     print(array[(i - shift) % len(array)], end=" ")
#


# задача  написать программу печати уникальных слов в словаре

lst = [{"v": "fjgk"}, {"vr": "ffgjgk"}]
val = set()
for d in lst:
    for k, v in d.items():
        val.add(v)
print(val)
