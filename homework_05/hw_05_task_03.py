# Создайте программу которая запрашивает у пользователя число,
# а затем выводит в консоль все целые числа от 1 до данного числа и их квадраты,
# например: «Введите число: » 5 Число 1, квадрат 1 Число 2, квадрат 4 Число 3,
# квадрат 9 Число 4, квадрат 16 Число 5, квадрат 25

num = int(input())

for i in range(1, num + 1):
    print(f'Number {i}, square number {pow(i, 2)}')
