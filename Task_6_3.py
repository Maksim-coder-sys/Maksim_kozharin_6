import csv
import sys
list_users = []
list_hobby = []
count_users = 0
count_hobby = 0
new_dictionary = {}
with open('users.csv', encoding='utf-8')as r_file:
    file_reader = csv.reader(r_file, delimiter=',')
    for row in file_reader:
        str_users = f'{row[0]} {row[1]} {row[2]}'
        list_users.append(str_users)
        count_users += 1
str_hobby = ''
with open('hobby.csv', encoding='utf-8')as r_file:
    file_reader = csv.reader(r_file, delimiter=',')
    for row in file_reader:
        list_hobby.append(row)
        count_hobby += 1
if count_hobby < count_users:
    n = count_users - count_hobby
    for i in range(n):
        list_hobby.append(None)
        count_hobby += 1
if count_hobby > count_users:
    sys.exit(1)
print(list_users)
print(f'Всего в файле {count_users} строк.')
print(list_hobby)
print(f'Всего в файле {count_hobby} строк.')
if count_hobby == count_users:
    for i in range(0,len(list_hobby)):
        new_dictionary[list_users[i]] = list_hobby[i]
print(new_dictionary)
