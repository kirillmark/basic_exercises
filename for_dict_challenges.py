# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2
def all_names(students):
    all_names = []
    for i in students:
        names = list(i.values())
        all_names.append(*names)
    return all_names


students1 = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
no_repeat_names = []
for i in all_names(students1):
    if not (i in no_repeat_names):
        print(f'{i}: {all_names(students1).count(i)}')
    no_repeat_names.append(i)

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша

students2 = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]

names_count = {}
for student in students2:
    name = student['first_name']
    if name in names_count:
        names_count[name] += 1
    else:
        names_count[name] = 1

most_common_name = max(names_count, key=names_count.get)
print(f"Самое частое имя среди учеников: {most_common_name}")


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
for i, class_students in enumerate(school_students, 1):
    names_count = {}
    for student in class_students:
        name = student['first_name']
        if name in names_count:
            names_count[name] += 1
        else:
            names_count[name] = 1

    most_common_name = max(names_count, key=names_count.get)
    print(f"Самое частое имя в классе {i}: {most_common_name}")



# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

for group in school:
    class_name = group['class']
    female_count = 0
    male_count = 0

    for student in group['students']:
        name = student['first_name']
        if name in is_male:
            if is_male[name]:
                male_count += 1
            else:
                female_count += 1

    print(f"Класс {class_name}: девочки {female_count}, мальчики {male_count}")


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a
def get_stud_lst(students):
    lst = []
    for student in students:
        lst.append(student['first_name'])
    return lst


def get_gender_st(class_, students):
    male_dict = {}
    female_dict = {}
    male_dict[class_] = 0
    female_dict[class_] = 0
    for student in students:
        if is_male[student]:
            male_dict[class_] += 1
        else:
            female_dict[class_] += 1
    return male_dict, female_dict


school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]

is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

common_male = {}
common_female = {}
for class_ in school:
    cl = class_['class']
    st = class_['students']
    st_lst = get_stud_lst(st)
    st_gender_ans = get_gender_st(cl, st_lst)
    common_male[cl] = st_gender_ans[0][cl]
    common_female[cl] = st_gender_ans[1][cl]

most_common_female = max(common_female, key=common_female.get)
print(f"Больше всего девочек в классе {most_common_female}")
most_common_male = max(common_male, key=common_male.get)
print(f"Больше всего мальчиков в классе {most_common_male}")



