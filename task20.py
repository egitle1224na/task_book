# from random import randint
# N = int(input('Введите натуральное число: '))
# numbers = []
# for _ in range(N):
#     numbers.append(randint(1, N))
# print(numbers)
# X = int(input('Введите число X: '))
# c = numbers.count(X)
# print(c)

scrabble = {
    'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1, 'А': 1, 'В': 1, 'Е': 1, 'И': 1,
    'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1, 'D': 2, 'G': 2, 'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2,
    'B': 3, 'C': 3, 'M': 3, 'P': 3, 'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3, 'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
    'Й': 4, 'Ы': 4, 'K': 5, 'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5, 'J': 8, 'X': 8, 'Ш': 8, 'Э': 8, 'Ю': 8,
    'Q': 10, 'Z': 10, 'Ф': 10, 'Щ': 10, 'Ъ': 10}
string_user = input('Введите слово для игры в Скрабл: ')
string_user = string_user.upper()
count = 0
for i in string_user:
    for k in scrabble.keys():
        if i == k:
            count += scrabble[k]
print(count)