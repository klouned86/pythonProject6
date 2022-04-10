'1) Создать следущие переменные '

reg_year_days = 365
leap_year_days = 366
real_year_days = 365.25
is_leap_year = True
reg = "Regular year"
leap = "Leap year"

'2) Создать tuples'

year_2021 = (2021, False, reg_year_days)
year_2022 = (2022, False, reg_year_days)
year_2023 = (2023, False, reg_year_days)
year_2024 = (2024, is_leap_year, leap_year_days)

'3) Попробовать поменять значения 2022 года на високосный год (leap year)'

# year_2022 = list(year_2022)
# year_2022[1], year_2022[2] = True, leap_year_days
# year_2022 = tuple(year_2022)
# print(year_2022)

'4) Создать list years и добавить в него все года'

all_year = [year_2021, year_2022, year_2023, year_2024]

'5) Пройти через лист при помощи цикла for и для каждого года вывести следущее сообщение при помощи конкатенации строк'

for i in all_year:
    if i[1] == False:
        print(f"{i[0]} is regular year and has {i[2]}")
    else:
        print(f'{i[0]} is leap year and has {i[2]}'.upper())


'6) Добавить к листу с годами еще один год (в виде tuple смотри пункт 2) и вывести количество элементов на консоль:'

year_2025 = (2025, False, reg_year_days)
all_year.append(year_2025)
print('В листе all_year', len(all_year), 'элементов')


'5) Пройти через лист при помощи цикла for и для каждого года вывести следущее сообщение'

for i in all_year:
    if i[1] == False:
        print(i[0], 'is regular year and has', i[2])
    else:
        print(i[0], 'is leap year and has'.upper(), i[2])

' 6) Создайте словарь c годами где ключ год - значение количество дней (от 2020 до 2030)'

dict_2 = {}
q = 365
w = 366

for i in range(2020, 2031):
    if i == 2020 or i == 2024 or i == 2028:
        dict_2[i] = w
    else:
        dict_2[i] = q



print('Дикт =', dict_2)

' 7*) При помощи цикла for вывести из словаря только не високосные года. <--- Задание со звездочкой))) На пятерку)))'

for k, v in dict_2.items():
    if v == 365:
        print(k)


#
#

