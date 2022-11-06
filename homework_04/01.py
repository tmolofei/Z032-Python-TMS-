# Создайте скрипт который запрашивает у пользователя 2 значения для переменных,
# а затем меняет эти значения для переменных

var_1 = input('Enter the first variable: ')
var_2 = input('Enter the second variable: ')

var_1, var_2 = var_2, var_1

print(f'Enter the first variable: {var_1}')
print(f'Enter the second variable: {var_2}')
