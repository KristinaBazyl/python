# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно
# ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.


def ar_progression (first_el, diff, amount_el):
    for i in range(amount_el):
        element = first_el + (i * diff)
        progression.append(element)
    return progression
    
    
first_el = int(input("Введите первый элемент прогрессии: "))
diff = int(input("Введите разность прогрессии: "))
amount_el = int(input("Введите количество элементов: "))
progression = []


print(ar_progression(first_el, diff, amount_el))