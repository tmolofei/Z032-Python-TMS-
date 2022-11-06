"""1. Создайте скрипт который возможно запустить из консоли (терминала), который ожидает
от пользователя ввода двух действительных чисел a и b, а затем в консоль
отдельными строками выводит информацию об их
1) Сумме
2) Разности
3) Произведении
4) Результате целочисленного деления
5) Делении по модулю
6) Результате возведения числа а в степень b"""

num_a = float(input("Enter first number: "))
num_b = float(input("Enter second number: "))

sum_numbers = num_a + num_b
dif_numbers = num_a - num_b
mult_numbers = num_a * num_b
integer_division = num_a // num_b
modul_division = num_a % num_b
numbers_exponen = num_a ** num_b  # we can use function pow()

print(f'Summ of entered numbers is {sum_numbers}')
print(f'Difference between first and second number is {dif_numbers}')
print(f'Multiplication of entered numbers is {mult_numbers}')
print(f'Result of integer division is of the first number by the second is {integer_division}')
print(f'Result of module division is {modul_division}')
print(f'Result of exponentiation the first number to the power of the second is {numbers_exponen}')
