"""
Найдите сумму цифр трехзначного числа n.
Результат сохраните в перменную res.

При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значение `n`
При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения `n` для проверки
"""

n = 100

# Введите ваше решение ниже

n1 = n // 100 # Нахождение первой цифры числа
n2 = (n % 100) // 10 # Нахождение второй цифры числа
n3 = n % 10 # Нахождение третьей цифры числа
res = n1 + n2 + n3

# res = (n // 100) + (n % 100 ) // 10 + (n % 10)

print(res)
