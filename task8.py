# Задача 8: Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).

print("Введите размер шоколоадки")
x = int(input("n= "))
y = int(input("y= "))
result = "No"
n = int(input("Сколько плиток надо отломить?: "))
if n % x == 0 or n % y == 0:
    result = "Yes"
print(result)
