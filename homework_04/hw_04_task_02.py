# Создайте скрипт который запрашивает у пользователя двузначное число,
# а затем выводит сумму цифр данного числа, например:
# «Введите число: »  24
# Сумма чисел → 6

"""version_1"""
user_num = int(input('Enter any number: '))
COUNT = 0
while user_num > 0:
    COUNT += user_num % 10
    user_num //= 10
print(f'Sum of digits of entered number is {COUNT}')

"""version_2"""
user_num = input('Enter any number: ')
COUNT = 0

for i in user_num:
    COUNT += int(i)
print(f'Sum of digits of entered number is {COUNT}')
