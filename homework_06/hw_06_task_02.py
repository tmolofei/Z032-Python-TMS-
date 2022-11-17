# Создайте функцию которая получает в качестве аргумента произвольную строку
# и заменяет все символы " на ' и наоборот

user_list = []
user_text = input()


def change_user_text():
    for i in user_text:
        user_list.append(i)
    for index, item in enumerate(user_list):
        if item == '"':
            user_list[index] = "'"
        elif item == "'":
            user_list[index] = '"'
    new_text = "".join(user_list)
    return new_text


print(change_user_text())
