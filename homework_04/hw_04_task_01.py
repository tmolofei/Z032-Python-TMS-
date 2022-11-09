# Создайте скрипт который запрашивает у пользователя 2 значения для переменных,
# а затем меняет эти значения для переменных

VAR_1 = input('Enter the first variable: ')
VAR_2 = input('Enter the second variable: ')

VAR_1, VAR_2 = VAR_2, VAR_1

print(f'Enter the first variable: {VAR_1}')
print(f'Enter the second variable: {VAR_2}')
