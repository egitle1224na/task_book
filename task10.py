# Задача 10
# На столе лежат n монеток. Некоторые из них лежат вверх решкой,
#  а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной.
#  Выведите минимальное количество монет, которые нужно перевернуть.

# Пример:

# 5 -> 1 0 1 1 0
# 2

from random import randint
n = int(input("Введите количество монеток: "))
list = []
i = 0
count_zero = 0
count_one = 0
while i < n:
    list.append(randint(0, 1))
    if list[i] == 0:
        count_zero += 1
    if list[i] == 1:
        count_one += 1
    i += 1
print(f'{n} -> {list}')
if count_zero > count_one:

    print(count_zero)
else:
    print(count_one)

