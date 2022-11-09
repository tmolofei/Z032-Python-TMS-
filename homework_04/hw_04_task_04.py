# Напишите скрипт, который принимает на вход последовательность слов,
# разделенных запятыми, и печатает уникальные слова в отсортированном виде.
# Примеры:
# Ввод: «красный,белый,черный,красный,зеленый,черный»
# Вывод: 'белый', 'зеленый', 'красный', 'черный'

user_words = input('Enter words separated by commas: ')
sorted_words = sorted(set(user_words.split(',')))
print(sorted_words)