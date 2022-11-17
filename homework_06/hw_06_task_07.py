# Создать функцию для нахождения двойного факториала


def double_factorial():
    factorial = 1
    user_num = int(input())
    if user_num % 2 == 1:
        for i in range(1, user_num + 1, 2):
            factorial *= i
    if user_num % 2 == 0:
        for i in range(2, user_num + 1, 2):
            factorial *= i
    print(factorial)


double_factorial()
