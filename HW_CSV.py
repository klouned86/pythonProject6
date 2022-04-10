import csv
import datetime
import random


file_path = "/Users/klouned86/PycharmProjects/pythonProject6/HW_CSV/"
file_name = 'CSV_Task_11.csv'
file_title = file_path + file_name
file_r = file_path + 'CSV_Email450.csv'

# .
#
# NNE
# with open(file_title, 'w') as csv_f:
#     # columns = ['Number', 'Name', 'Age']
#     writer = csv.writer(csv_f)
#     # writer.writeheader()
#     row = ['Number', 'Name', 'Age']
#     writer.writerow(row)
#     for i in range(0, 100):
#          row = ['Numbers_' + str(i), 'Names_' + str(i), '@email.com' + str(i)]
#          writer.writerow(row)
#
# Вариант 2. Создать digits_2.csv файл с 1-м полем которое называется number,
# в котором будут 300 строк с числами от 10 до 310
#
# with open(file_title, 'w', newline='') as csv_35:
#     writer = csv.writer(csv_35)
#     row = ['Number']
#     writer.writerow(row)
#     for i in range(0, 300):
#         row = [i]
#         writer.writerow(row)
#
# Вариант 2. Создать names_2.csv файл с 1-м полем которое называется name,
# в котором будут 400 строк с разными именами
#
# with open(file_title, 'w', newline='') as csv_36:
#     w = csv.writer(csv_36)
#     row = ['Name']
#     w.writerow(row)
#     for i in range(0, 400):
#         row = ['Name_' + str(i)]
#         w.writerow(row)
#
# Вариант 2. Создать emals_2.csv файл с 1-м полем которое называется email,
# в котором будут 400 строк с разными имейлами что-то@gmail.com
#
# with open(file_title, 'w', newline='') as im:
#     w = csv.writer(im)
#     row = ['Emails']
#     w.writerow(row)
#     for i in range(0, 400):
#         row = ['name_' + str(i) + '@email.com']
#         w.writerow(row)
#
# Вариант 2. Создать nne_2.csv файл с 3-мя полями(Number, Name, Email ),
# в котором будут 450 строк. Имя и часть email до @ должны совпадать.
#
# with open(file_title, 'w') as im:
#     w = csv.writer(im)
#     row = ['Number', 'Name', 'Email']
#     w.writerow(row)
#     for i in range(1, 451):
#         row = [str(i), 'Name-' + str(i), 'Email' + str(i)]
#         w.writerow(row)

# Добавить в файл nne_2.csv столбец Date и заполнить каждую строку текущей датой и временем.
# Поле даты заполнить следующим образом:
# a) Первые 50 строк даты по годам от 1980 - 1990 (паспределие рандомно)
# b) Следующие 100 строк даты по годам от 1991 - 2000 (паспределие рандомно)
# с) Следующие 150 строк даты по годам от 2001 - 2010 (паспределие рандомно)
# в) Следующие 150 строк даты по годам от 2011 - 2021 (паспределие рандомно)
'============================================================================================'
# with open(file_title, 'w', newline='') as im:
#     w = csv.writer(im)
#     row = ['Number', 'Name', 'Email', 'Date']
#     w.writerow(row)
#     for i in range(1, 51):
#         dt_now = datetime.datetime.now()
#         row = [str(i), 'Name_' + str(i), 'Email_' + str(i), dt_now]
#         w.writerow(row)
#     for n in range(51, 101):
#         min_year, max_year = 1980, 1990
#         rand_1980 = random.randint( min_year, max_year)
#         row = [str(n), 'Name_' + str(n), 'Email_' + str(n), rand_1980]
#         w.writerow(row)
#     for z in range(101, 151):
#         min_year, max_year = 1991, 2000
#         rand_1991 = random.randint(min_year, max_year)
#         row = [str(z), 'Name_' + str(z), 'Email_' + str(z), rand_1991]
#         w.writerow(row)
#     for u in range(151, 301):
#         min_year, max_year = 2001, 2010
#         rand_2001 = random.randint(min_year, max_year)
#         row = [str(u), 'Name_' + str(u), 'Email_' + str(u), rand_2001]
#         w.writerow(row)
#     for z in range(301, 451):
#         min_year, max_year = 2011, 2021
#         rand_2011 = random.randint(min_year, max_year)
#         row = [str(z), 'Name_' + str(z), 'Email_' + str(z), rand_2011]
#         w.writerow(row)
'============================================================================================'

# Создать файл combo.csv с полями Name, Emaill, Date. 1000 строк.
# a) Соберите имена из файла nne_2.csv.
# b) недостающие 550 строк имён сгенерируйте.
# с) Имена расположите в алфавитном порядке.
# d) Для имён из файла nne_2.csv забрать даты из nne_2.csv которые были с этими именами в nne_2.csv.
# e) Остальные даты генерировать рандомно.
# f) Добавить и заполнить (можно рандомно) столбы Email, Phone, Gender, Salary.


with open(file_title, 'w') as fff:
    w = csv.writer(fff)
    head = ['Number', 'Name', 'Email', 'Date']
    w.writerow(head)
with open(file_title, 'w', newline='') as fff:
    w = csv.writer(fff)
    with open(file_r, 'r', encoding='UTF-8') as f:
        data = csv.reader(f, delimiter=',', skipinitialspace=True)
        for row in data:
            r = row[1]
            m = ['', r, '', '']
            w.writerow(m)
print(data)



