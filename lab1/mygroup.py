groupmates = [
    {
        "name": "Андрей",
        "surname": "Ветров",
        "exams": ["РОС", "ТиСОС", "ПИС"],
        "marks": [5, 5, 3]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "exams": ["РОС", "ТиСОС", "ПИС"],
        "marks": [4, 4, 3]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "exams": ["РОС", "ТиСОС", "ПИС"],
        "marks": [3, 5, 3]
    },
    {
        "name": "Екатерина",
        "surname": "Белинская",
        "exams": ["РОС", "ТиСОС", "ПИС"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Мария",
        "surname": "Кузнецова",
        "exams": ["РОС", "ТиСОС", "ПИС"],
        "marks": [3, 4, 5]
    }
]

def print_students(students):
    print("Имя".ljust(15), "Фамилия".ljust(10), "Экзамены".ljust(30), "Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))

def filter_by_average_mark(students, min_avg):
    filtered = []
    for student in students:
        avg = sum(student["marks"]) / len(student["marks"])
        if avg > min_avg:
            filtered.append(student)
    return filtered

min_mark = float(input("Введите минимальный средний балл для фильтра: "))
filtered_students = filter_by_average_mark(groupmates, min_mark)
print_students(filtered_students)
