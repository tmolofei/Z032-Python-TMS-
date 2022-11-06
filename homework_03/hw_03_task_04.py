"""4. Создайте скрипт, который ожидает от пользователя ввода предложения, затем символа,
и в результате работы вывести сколько раз искомый символ встречается в предложении
 Например,
Введите предложение: Learning Python is great!
Введите символ: a
Символ а встречается 2 раза"""

user_text = input('Enter any text: ')
user_symbol = input('Enter any symbol: ')

symbol_count = user_text.count(user_symbol)
print(f'The symbol {user_symbol} appears in the text {symbol_count} times')
