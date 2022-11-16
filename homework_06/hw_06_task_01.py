# Дан словарь, создать новый словарь, поменяв местами ключ и значение

user_dict = {'name': 'Jane', 'age': 28, 'child': 'Anny', 'pets': 'dog'}
new_dict = {}


def change_key_value():
    for key, value in user_dict.items():
        new_dict.setdefault(value, key)
    print(new_dict)


change_key_value()
