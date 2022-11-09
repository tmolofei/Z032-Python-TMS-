# Написать программу которая получит имя и возраст пользователя,
# проверяет возраст >18 и выдает приветственное сообщение в зависимости от возраста

user_age = int(input('Enter your age: '))

if user_age > 18:
    print('You are welcome. You have an access to this site')
else:
    print("You are too young, you can't visit this site")
