"""5. Создайте скрипт, который ожидает от пользователя ввода двух слов
и в результате работы выводит результат следующих операций:
1. В каждом слове удаляет первую букву и последнюю
2. После этого меняет порядок букв второго слова на противоположный («привет» → «тевирп»)
3. Объединяет данные строки
например

Введите первое слово: привет
Введите второе слово: Python
итоговая строка: ривеohty"""

user_word_1 = input('Enter first word: ')
user_word_2 = input('Enter second word: ')

user_word_1_del_letters = user_word_1[1:-1]
user_word_2_del_letters = user_word_2[1:-1]
USER_WORD_2_REVERSED = "".join(reversed(user_word_2_del_letters))

joined_strings = user_word_1_del_letters + USER_WORD_2_REVERSED

print(joined_strings)
