# Задача 12:

S = int(input())
P = int(input())
D = S ** 2 - 4 * P
Flag = True
if D > 0:
    x = int((S - D ** 0.5) / 2)
elif D == 0:
    x = S // 2
else:
    Flag = False


if Flag:
    y = S - x
    print(x, y)
else:
    print('введите другие значения')