# Найдите сумму цифр трехзначного числа n.
print("Введите число")
n = int(input())
res =(n%10)+(n//100)+((n%100)//10)
print(res)
