# Напишите программу для подсчета количества символов (частоты символов)
# в строке (игнорируя регистр букв).
# Пример:
# Input: 'Oh, it is Python'
# Output: {',': 1, ' ': 3, 'o': 2, 'h': 2, 'i': 2, 't': 2, 's': 1, 'p': 1, 'y': 1, 'n': 1}

user_text = input('Enter any text: ')

user_dict = {}

for i in user_text:
    if i in user_dict:
        user_dict[i] += 1
    else:
        user_dict[i] = 1
print(user_dict)
