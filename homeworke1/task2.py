# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали n журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали
# одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# Выведите кортеж из количества журавликов, сделанных Петей, Катей и Сережей.

print("введите общее количество журавлей:")
n = int(input())
a = n//6
b = n//6
c = 2*n//3

if n % 6 == 0:
    print(a, c, b)
else:
    print("введите другое количество журавлей")
