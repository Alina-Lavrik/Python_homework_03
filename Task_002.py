# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] =>[12,15,16]      ([2*6, 3*5, 4*4]);
# [2, 3, 5, 6] => [12,15]   ( [2*6, 3*5]) 

spisok = list(map(int, input('Введите числа через пробел: ').split()))
print(f'Список: {spisok}')

long = 0
new_spisok = 0
if len(spisok) % 2 != 0:
    long = len(spisok)//2 + 1
else:
    long = len(spisok)//2

new_spisok = [spisok[i]*spisok[len(spisok)-i-1] for i in range(long)]

print(f'Новый список: {new_spisok}')

