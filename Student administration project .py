# Base class: Person
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def display(self):
        print(f"Name: {self._name}, Age: {self._age}")

# Derived class: Student
class Student(Person):
    def __init__(self, name, age, student_id, grades):
        super().__init__(name, age)
        self._student_id = student_id
        self._grades = grades

    def get_student_id(self):
        return self._student_id

    def get_grades(self):
        return self._grades

    def display(self):
        super().display()
        print(f"Student ID: {self._student_id}, Grades: {self._grades}")

# Derived class: Teacher
class Teacher(Person):
    def __init__(self, name, age, employee_id, subject):
        super().__init__(name, age)
        self.__employee_id = employee_id
        self.__subject = subject

    def get_employee_id(self):
        return self.__employee_id

    def get_subject(self):
        return self.__subject

    def display(self):
        super().display()
        print(f"Employee ID: {self.__employee_id}, Subject: {self.__subject}")

# Polymorphism example
def print_person_details(person):
    person.display()

# Abstraction example
class School:
    def __init__(self, name):
        self._name = name
        self._students = []
        self._teachers = []

    def add_student(self, student):
        self._students.append(student)

    def add_teacher(self, teacher):
        self._teachers.append(teacher)

    def display_students(self):
        print("Students:")
        for student in self._students:
            student.display()

    def display_teachers(self):
        print("Teachers:")
        for teacher in self._teachers:
            teacher.display()

# Encapsulation example
# Using getters and setters to access private variables
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

# Usage example
student1 = Student("Alice", 20, "S12345", [90, 85, 88])
student2 = Student("Bob", 22, "S67890", [75, 80, 70])

teacher1 = Teacher("Mr. Smith", 40, "T1001", "Mathematics")
teacher2 = Teacher("Ms. Johnson", 35, "T1002", "Physics")

school = School("Greenwood High")
school.add_student(student1)
school.add_student(student2)
school.add_teacher(teacher1)
school.add_teacher(teacher2)

# Polymorphism in action
print_person_details(student1)
print_person_details(teacher1)

# Displaying all students and teachers in the school
school.display_students()
school.display_teachers()
