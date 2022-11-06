# 4. Напишите скрипт, который принимает на вход три слова произвольной
# длины и выводит следующую информацию:
# 1) буквы которые встречаются во всех словах
# 2) все буквы, которые хотя бы раз встречаются в слове
# 3) буквы в каждом слове которые не встречаются в других словах

user_word_1 = input()
user_word_2 = input()
user_word_3 = input()

repeated_letters = []
for i in user_word_1:
    if i in user_word_2 and i in user_word_3:
        repeated_letters.append(i)

unique_letters = list(set(user_word_2 + user_word_3 + user_word_1))

unique_letters_word_1 = []
unique_letters_word_2 = []
unique_letters_word_3 = []

for i in user_word_1:
    if i not in user_word_2 and i not in user_word_3:
        unique_letters_word_1.append(i)
for i in user_word_2:
    if i not in user_word_1 and i not in user_word_3:
        unique_letters_word_2.append(i)
for i in user_word_3:
    if i not in user_word_2 and i not in user_word_1:
        unique_letters_word_3.append(i)

print(f'Repeated letters in every word: {repeated_letters}')
print(f'All letters in every word: {unique_letters}')
print(f'Unique letters in the first word: {unique_letters_word_1}')
print(f'Unique letters in the second word: {unique_letters_word_2}')
print(f'Unique letters in the third word: {unique_letters_word_3}')
