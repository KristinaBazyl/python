# Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.

list_1 = [1, 2, 3, 4, 5]
k = 6
x = k
y = k
while not (x in list_1 or y in list_1):
    x -= 1
    y += 1
print(x if x in list_1 else y)
# m = abs(k - list_1[0])  # модуль числа
# number = list_1[0]
# for i in range(1, len(list_1)):
#     if m > abs(list_1[i] - k):
#         m = abs(list_1[i] - k)
#         number = list_1[i]
# print(number)