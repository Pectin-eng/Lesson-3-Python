print('Задача 4.')

x = int(input('Введите положительное число, x: '))
y = int(input('Введите отрицательное число, y: '))

r = 1
while abs(y) > 0:
    """Цикл умножает введенное число на него же согласно числу, введенному для степени"""
    r *= 1 / x
    y = abs(y) - 1
print("x^y=%.2f" % r)