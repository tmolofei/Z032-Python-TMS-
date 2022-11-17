# Создайте функцию которая работает так же как str.split()
# метод (естественно, без использования str.split())


user_text = "Adfsfs, sdfsdfsd. Fdsfsdf! lkklllls lswllsls"


def split_text():
    user_list = []
    for i in user_text:
        user_list.append(i)
    new_text = "".join(user_list)
    return new_text


print(split_text())
