# Задача 2
# Найдите сумму цифр трехзначного числа.

# Пример:

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

n = 123
sum = 0
while n > 0:
    a = n % 10
    sum = sum + a
    n = n // 10

print(sum)