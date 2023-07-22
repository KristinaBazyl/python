# Задача 10:

n = int(input())
o = 0
r = 0
for i in range(n):
    m = int(input())
    if m == 0:
        o += 1
    else:
        r += 1
print(min(o, r))
