# Создайте скрипт который запрашивает у пользователя его вес и рост,
# и в результате работы выводит индекс массы тела

user_weight = float(input('Enter your weight in kg in x.xx format: '))
user_growth = float(input('Enter your growth in metres in x.xx format: '))

body_mass_index = user_weight / pow(user_growth, 2)
print(f'Your body mass index is {round(body_mass_index, 2)} kg/m2')
