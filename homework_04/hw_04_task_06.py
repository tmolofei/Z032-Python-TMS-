# 5. Создайте скрипт который запрашивает у пользователя дату его рождения
# в формате «день/месяц/год», запрашивает дату в таком же формате, а затем
# выводит сколько пользователю было полных лет и дней на указанную дату.
# Для упрощения, предположим что в году 365 дней, в месяце — 30 дней
from datetime import date

today = date.today().strftime('%d/%m/%Y').split("/")
date_of_birth = input("Enter the date of your birthday in dd/mm/yyyy format: ").split('/')
# user_date = input("Enter any date after your bday in dd/mm/yyyy format: ").split('/')

diff_years = (int(today[2]) - int(date_of_birth[2])) * 365
diff_months = (int(today[1]) - int(date_of_birth[1])) * 30
diff_days = int(today[0]) - int(date_of_birth[0])
diff_dates = diff_years + diff_months + diff_days

print(f'Difference between current date and your birthday is '
      f'{diff_dates // 365} years and {diff_dates % 365} days')
