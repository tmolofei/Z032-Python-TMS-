# Создайте программу которая генерирует случайное число в интервале от 1 до 100
# и предлагает пользователю угадать это число. В случает ввода от пользователя
# инструкции «stop», завершает работу и выводит загаданное число
# для генерации случайного числа используйте метод randint модуля random

import random

num = random.randint(1, 5)
user_num = input('Try to guess a number and enter it or enter "stop": ')

if user_num == 'stop':
    print(f'Hidden number is {num}')
else:
    while int(user_num) != num:
        user_num = input('Try again to guess a number and enter it or enter "stop": ')
        if user_num == 'stop':
            print(f'Hidden number is {num}')
            break
        if int(user_num) == num:
            print(f"You guessed a number, it's {num}")
        continue
