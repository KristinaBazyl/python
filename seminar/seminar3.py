# добавить _n если буква встречается нескольько раз, т.е каждой букве приписывать который повтор

# lst = 'a a a b b a a d d c c'.split()
# lst_2 = []
# count_let = 0
#
# for i in range(len(lst)):
#     if lst[i] in lst_2:
#         count_let = lst_2.count(lst[i])
#         lst_2 += lst[i] + "_" + str(count_let)
#     else:
#         lst_2 += lst[i]
# print(*lst_2)
#
# main_string = input("введите строку: ")
# cnt_dickt = {}
# for ch in main_string:
#     cnt_dickt[ch] = cnt_dickt.get(ch, -1) + 1
# #     if ch in cnt_dickt:
# #         cnt_dickt[ch] += 1
# #     else:
# #         cnt_dickt[ch] = 0
#     print(ch if cnt_dickt[ch] < 1 else f'{ch}_{cnt_dickt[ch]}', end=' ')
#

# задача 27. Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов или символами конца строки.Определите,
# сколько различных слов содержится в этом тексте.
# from string import punctuation
# text = '''She sells sea shells on the sea shore;The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore,I'm sure that the shells are sea shore shells.'''
#
# for ch in punctuation.replace("'", ''):
#     text = text.replace(ch, ' ')
# print(len(set(text.lower().split())))

# задача 29 “Задана последовательность неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в последовательность)”.

n = int(input("введите число: "))
max_number = n
while n != 0:
    n = int(input("введите число: "))
    if max_number < n:
        max_number = n
print(max_number)