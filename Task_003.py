# 3'. Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19



spisok = list(map(float, input("Введите числа через пробел: ").split()))

new_spisok = [round(i % 1, 2) for i in spisok if i % 1 != 0]
print(f'Новый список: {new_spisok}')
print(f'Разница: ', max(new_spisok) - min(new_spisok))

