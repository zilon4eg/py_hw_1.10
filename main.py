class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Error'

    def middle_grade(self, student):
        if len(student.grades.values()) > 0:
            mid_grades = 0
            sum_grades = 0
            quantity = 0
            for grades in student.grades.values():
                sum_grades += sum(grades)
                quantity += len(grades)
            mid_grades = round(sum_grades / quantity, 1)
        else:
            mid_grades = 'нет оценок'
        return mid_grades

    def __str__(self):
        parameters = f'Имя: {self.name}\n'
        parameters += f'Фамилия: {self.surname}\n'
        parameters += f'Средняя оценка за домашние задания: {self.middle_grade(self)}\n'
        parameters += f'Курсы в процессе изучения: {str(self.courses_in_progress)[1:-1]}\n'
        parameters += f'Завершенные курсы: {str(self.finished_courses)[1:-1]}\n'
        parameters = parameters.replace("'", "")
        return parameters

    def __lt__(self, other):
        if not isinstance(other, Student):
            print(f'{other} is not Student!')
            return
        else:
            return self.middle_grade(self) < self.middle_grade(other)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print(f'{other} is not Lecturer!')
            return
        else:
            return self.middle_grade(self) < self.middle_grade(other)

    def middle_grade(self, student):
        if len(student.grades.values()) > 0:
            mid_grades = 0
            sum_grades = 0
            quantity = 0
            for grades in student.grades.values():
                sum_grades += sum(grades)
                quantity += len(grades)
            mid_grades = round(sum_grades / quantity, 1)
        else:
            mid_grades = 'нет оценок'
        return mid_grades

    def __str__(self):
        parameters = f'Имя: {self.name}\n'
        parameters += f'Фамилия: {self.surname}\n'
        parameters += f'Средняя оценка за лекции: {self.middle_grade(self)}\n'
        return parameters


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Error'

    def __str__(self):
        parameters = f'Имя: {self.name}'
        parameters += f'\nФамилия: {self.surname}'
        return parameters


def middle_rate_all_students(list_of_students, course):
    all_middle_rate_course = 0
    all_sum_rate_course = 0
    all_quantity_rate_course = 0
    no_course_in_list_count = 0
    for student in list_of_students:
        if course in student.grades.keys():
            all_sum_rate_course += sum(student.grades.get(course))
            all_quantity_rate_course += len(student.grades.get(course))
        else:
            no_course_in_list_count += 1
    if no_course_in_list_count != len(list_of_students):
        all_middle_rate_course = round(all_sum_rate_course / all_quantity_rate_course, 1)
        return all_middle_rate_course
    else:
        return f'Указанного курса нет ни у одного студента'


def middle_rate_all_lecturers(list_of_lecturers, course):
    all_middle_rate_course = 0
    all_sum_rate_course = 0
    all_quantity_rate_course = 0
    no_course_in_list_count = 0
    for lecturer in list_of_lecturers:
        if course in lecturer.grades.keys():
            all_sum_rate_course += sum(lecturer.grades.get(course))
            all_quantity_rate_course += len(lecturer.grades.get(course))
        else:
            no_course_in_list_count += 1
    if no_course_in_list_count != len(list_of_lecturers):
        all_middle_rate_course = round(all_sum_rate_course / all_quantity_rate_course, 1)
        return all_middle_rate_course
    else:
        return f'Указанного курса нет ни у одного лектора'


# ===(Добавляем первого лектора)==
arnold = Lecturer('Arnold', 'Schwarzenegger')
arnold.courses_attached += ['Python']

# ===(Добавляем второго лектора)==
michael = Lecturer('Michael', 'Jackson')
michael.courses_attached += ['Pascal']

# ===(Добавляем проверяющего)==
jesus = Reviewer('Jesus', 'Christ')
jesus.courses_attached += ['Python']
jesus.courses_attached += ['Pascal']

# ===(Добавляем первого студента)==
jools = Student('Jools', 'USA soldier', 'male')
jools.courses_in_progress += ['Python']
jools.courses_in_progress += ['Pascal']
jools.finished_courses += ['С++ для чайников']

# ===(Добавляем второго студента)==
jops = Student('Jops', 'USA soldier', 'male')
jops.courses_in_progress += ['Python']
jops.courses_in_progress += ['Pascal']
jops.finished_courses += ['Java с нуля']

# ===(Добавляем студентам оценки от проверяющего)==
jesus.rate_hw(jops, 'Python', 1)
jesus.rate_hw(jops, 'Python', 8)
jesus.rate_hw(jops, 'Pascal', 10)
jesus.rate_hw(jools, 'Python', 7)
jesus.rate_hw(jools, 'Python', 6)
jesus.rate_hw(jools, 'Pascal', 7)

# ===(Добавляем лекторам оценки от студентов)==
jools.rate_lecture(arnold, 'Python', 9)
jools.rate_lecture(arnold, 'Python', 7)
jools.rate_lecture(arnold, 'Python', 10)
jools.rate_lecture(michael, 'Pascal', 5)
jools.rate_lecture(michael, 'Pascal', 10)
jools.rate_lecture(michael, 'Pascal', 9)

# ===(Выводим данные преподавателей)==
print(arnold)
print(michael)

# ===(Выводим данные проверяющего)==
print(jesus)

# ===(Выводим данные стуентов)==
print(jools)
print(jops)

# ===(Сравниваем студентов по среднему баллу)==
print(jools > jops)

# ===(Сравниваем студентов по среднему баллу)==
print(arnold > michael)

# ===(Создаем список студентов)==
list_of_students = [jools, jops]

# ===(Выводим средний балл всех студентов по курсу)==
print(middle_rate_all_students(list_of_students, 'Pascal'))

# ===(Создаем список лекторов)==
list_of_lecturers = [arnold, michael]

# ===(Выводим средний балл всех лекторов по курсу)==
print(middle_rate_all_lecturers(list_of_lecturers, 'Python'))