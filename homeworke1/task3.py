# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет
# с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех
# цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета с номером n и выводит
# на экран yes или no.

print("Введите шестизначный номер билета:")
n = int(input())

n1 = n//1000
n1_str = str(n1)
sum_n1 = int(n1_str[0]) + int(n1_str[1]) + int(n1_str[2])

n2 = n % 1000
n2_str = str(n2)
sum_n2 = int(n2_str[0]) + int(n2_str[1]) + int(n2_str[2])

if sum_n1 == sum_n2:

    print("Yes")
else:
    print("No")
