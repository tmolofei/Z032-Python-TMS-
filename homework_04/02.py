# Создайте скрипт который запрашивает у пользователя двузначное число,
# а затем выводит сумму цифр данного числа, например:
# «Введите число: »  24
# Сумма чисел → 6

user_num = int(input('Enter any number: '))
count = 0

while user_num > 0:
    count += user_num % 10
    user_num //= 10

print(f'Sum of digits of entered number is {count}')
