# С клавиатуры вводится строка, которая должна содержать как минимум два пробела.Верните
# строку, в которой первое и последнее слова начинаются с заглавной буквы, а весь остальной
# текст написан в нижнем регистре.

user_text = input("Enter any text: ")

formatted_text = user_text.capitalize().split()
formatted_text[-1] = formatted_text[-1].capitalize()

print(" ".join(formatted_text))
