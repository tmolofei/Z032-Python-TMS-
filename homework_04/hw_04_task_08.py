# 7. Написать программу используя функции input() и print().
# Программа запрашивает ввести произвольную строку, произвольный символ Х
# и однозначное число N. В результате работы программа выведет
# 1) введенную строку
# 2) строку состоящую из четных символов разделенную N  символами Х с нечетными символами строки
# 3) N восклицательных знаков (с новой строки)

user_text = input('Enter any text: ')
X = input('Enter any symbol: ')
N = int(input('Enter a number from 0 to 9: '))

text_even_symbol = user_text[1::2]
text_odd_symbol = user_text[::2]
separator = X * N
separated_text = f'{text_even_symbol}{separator}{text_odd_symbol}'

print(user_text, separated_text, '!'*N, sep="\n")


