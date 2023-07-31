# Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.\
list_1 = [1, 2, 3, 4, 5, 3]
k = 3
count = 0
for i in list_1:
    if k == i:
        count += 1
print(count)
# print(list_1.count(k) if k in list_1 else 0)