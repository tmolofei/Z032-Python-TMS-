# 5. Реализовать функцию, которая получает изменяемое количество словарей
# (ключи - буквы, значения - числа) и объединяет их в один словарь.
# Значения dict должны быть суммированы в случае идентичных ключей


dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}
result = {}


def join_dict(*args):
    for item in args:
        for key, value in item.items():
            if key not in result:
                result.setdefault(key, value)
            elif key in result:
                result[key] += value
    print(result)


join_dict(dict_1, dict_3, dict_2)
