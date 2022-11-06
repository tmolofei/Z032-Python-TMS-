"""Создайте скрипт который возможно запустить из консоли (терминала),
который ожидает от пользователя ввода двух действительных чисел x и y, а затем в консоль выводит
результат выражения
| x | - | y |
______________
1 + | x * y |"""

num_x = float(input("Enter first number: "))
num_y = float(input("Enter second number: "))

result = (abs(num_x) - abs(num_y)) / (1 + abs(num_x * num_y))

print(result)
