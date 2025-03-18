class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        total = 0
        for student in self.students:
            total += student.get_grade()
        return total / len(self.students)

student1 = Student("Thomas", 11, 77)
student2 = Student("Tom", 13, 78)
student3 = Student("Tim", 14, 99)

course1 = Course("Computer Science", 2)

course1.add_student(student1)
course1.add_student(student2)

for student in course1.students:
    print(student.name)

print((course1.add_student(student3)))# false
print(f"The average grade in {course1.name} is {course1.get_average_grade()}")

