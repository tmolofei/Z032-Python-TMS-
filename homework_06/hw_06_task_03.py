# Реализуйте функцию get_digits(num: int) -> tuple, которая возвращает кортеж
# цифр заданного целого числа.

user_list = []


def num_in_tuple():
    user_num = input()
    for i in user_num:
        user_list.append(int(i))
    print(tuple(user_list))


num_in_tuple()
