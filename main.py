# This is a sample Python script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

Chislo1 = 777
Stroka1 = 'kakoito tekst'
pravda = True
flot = 5.55
name = 'Mihail'
print (name)
age = 62
print (age)
age = age + 62
print (age)
is_student = True
print (is_student)

# Переменные
home_works_executed = 12
needed_hours = 1.5
lessons_name = 'Pyton'
one_task_time = needed_hours / home_works_executed
print('Курс:', lessons_name, 'всего задач:',
      home_works_executed,',затрачено часов',needed_hours,
      ',среднее время выполнения',one_task_time, '.')

# Строки и индексация
example = 'lyubayactroka'
print(example[0])
print(example[-1])
dl = len(example)
haff_len = dl//2
diff = dl-haff_len
print(dl, haff_len, diff)
print(example[haff_len:])
print(example[::-1])
print(example[1::2])
