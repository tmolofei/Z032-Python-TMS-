# Написать программу которая получит имя и возраст пользователя,
# проверяет возраст >18 и выдает приветственное сообщение в зависимости от возраста
# Завернуть программу из п.1 в вечный цикл


while True:
    user_age = input('Enter your age: ')
    if str(user_age).lower() == 'stop':
        break
    elif int(user_age) > 18:
        print('You are welcome. You have an access to this site')
    else:
        print("You are too young, you can't visit this site")
