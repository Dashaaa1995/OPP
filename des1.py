class Student:
    grades_lector_python = []
    grades_lector_git = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades_student = {}
        self.gradess = []
        self.sum_of_ratings = 0
        self.number_of_ratings = 0

    def rate_lector(self, lector, course, grade):
        lector.lecture_scores += grade

        if course in 'Python':
            Student.grades_lector_python += grade
        elif course in 'Git':
            Student.grades_lector_git += grade

        if course in lector.gradess:
            lector.gradess[course] += grade
        else:
            lector.gradess[course] = grade

    # средняя оценка у лектора
    def avr_all_lector(lector_python, lector_git):

        avr_phyton = sum(lector_python) / len(lector_python)
        print(f'Средняя оценка за курс у лекторов по \"Phyton\": {avr_phyton}')
        print()

        avr_git = sum(lector_git) / len(lector_git)
        print(f'Средняя оценка за курс у лекторов по "Git": {avr_git}')
        print()

    def socer_student(self, sr):
        for val in sr:
            self.sum_of_ratings += val
            self.number_of_ratings += 1
            self.avr_rating = self.sum_of_ratings / self.number_of_ratings

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {round(self.avr_rating, 1)}\n' \
               f'Завершенные курсы: {self.finished_courses[0]}\n' \
               f'Курсы в процессе изучения: {self.courses_in_progress[0]}, {self.courses_in_progress[1]}'


def __gt__(self, other):
    if self.avr_rating > other.avr_rating:
        return f'Лучший студент: {self.name} с рейтингом: {self.avr_rating}'
    else:
        return f'Лучший студент: {other.name} с рейтингом: {other.avr_rating}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    lecture_scores = []
    gradess = {}
    curs = []
    sum_of_ratings = 0
    number_of_ratings = 0
    avr_rating = 0

    def socer(self, sr):
        for val in sr:
            self.sum_of_ratings += val
            self.number_of_ratings += 1
        self.avr_rating = self.sum_of_ratings / self.number_of_ratings

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {round(self.avr_rating, 1)}'


def __at__(self, other):
    if self.avr_rating > other.avr_rating:
        return f'Лучший лектор: {self.name} с рейтингом: {round(other.avr_rating, 1)}'
    else:
        return f'Лучший лектор: {other.name} с рейтингом: {round(other.avr_rating, 1)}'


class Reviewer(Mentor):
    courses_attacheds = []
    courses_grades = []
    curse_phyton = []
    curse_git = []
    grades_all_phyton = []
    grades_all_git = []

    def rate_hw(self, student, course, grade):
        student.gradess += grade
        if course in 'Python':
            Reviewer.grades_all_phyton += grade
        elif course in 'Git':
            Reviewer.grades_all_git += grade
        if course in student.grades_student:
            student.grades_student[course] += grade
        else:
            student.grades_student[course] = grade

    def avr_all_curs(phyton, git):

        avr_phyton = sum(phyton) / len(phyton)
        print(F'Средняя оценка на курсе у учеников по "Phyton": {avr_phyton}')
        print()

        avr_git = sum(git) / len(git)
        print(F'Средняя оценка на курсе у учеников по "Git": {avr_git}')
        print()

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


some_student1 = Student('Ruoy', 'Eman', 'your_gender')
some_student1.courses_in_progress += ['Python', 'Git']
some_student1.finished_courses += ['Разработчик с нуля']

some_mentor1 = Reviewer('Some', 'Buddy')
some_mentor1.courses_attacheds += ['Python', 'Git']
some_mentor1.rate_hw(some_student1, 'Python', [9, 10, 7, 10, 10])
some_mentor1.rate_hw(some_student1, 'Git', [10, 8, 7, 10, 10])

some_student2 = Student('Дарья', 'Чуканова', 'your_gender')
some_student2.courses_in_progress += ['Python', 'Git']
some_student2.finished_courses += ['Разработчик с нуля']

some_mentor2 = Reviewer('Bonny', 'Sam')
some_mentor2.courses_attacheds += ['Python', 'Git']
some_mentor2.rate_hw(some_student2, 'Python', [7, 10, 9, 8, 10])
some_mentor2.rate_hw(some_student2, 'Git', [10, 9, 10, 9, 10])

some_lector1 = Lecturer('Павел', 'Цуриков')
some_lector1.curs += ['Python', 'Git']
some_student2.rate_lector(some_lector1, 'Python', [7, 7, 9, 8, 10])
some_student1.rate_lector(some_lector1, 'Git', [8, 9, 10, 7, 10])

some_lector2 = Lecturer('Pavel', 'Pit')
some_lector2.curs += ['Python', 'Git']
some_student1.rate_lector(some_lector2, 'Python', [10, 10, 7, 10, 6, 10])
some_student2.rate_lector(some_lector2, 'Git', [10, 5, 10, 6, 5])

print(some_mentor1)
print()

print(some_mentor2)
print()

some_student1.socer_student(some_student1.gradess)
print(some_student1)
print()

some_student2.socer_student(some_student2.gradess)
print(some_student2)
print()

some_lector1.socer(some_lector1.lecture_scores)

print(some_lector1)
print()

some_lector2.socer(some_lector2.lecture_scores)
print(some_lector2)
print()

print(some_student2 > some_student1)
print()

print(some_lector1 < some_lector2)
print()