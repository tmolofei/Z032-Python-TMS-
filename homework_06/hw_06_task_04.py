# Реализуйте функцию, которая получает список из целых чисел, и возвращает новый список,
# в котором каждый элемент с индексом i нового списка является суммой всех чисел
# в исходном списке, кроме числа i.


new_list = []


def new_user_list():
    user_list = list(map(int, input().split()))
    for i, _ in enumerate(user_list):
        new_list.append(sum(user_list) - user_list[i])
    return new_list


print(new_user_list())
