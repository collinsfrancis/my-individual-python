class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score


class Gradebook:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_average(self):
        if len(self.students) == 0:
            return 0

        total = 0
        for student in self.students:
            total += student.score
        return total / len(self.students)
    
s1=Student("poker", 80)
s2=Student("sabrina",20)
s3=Student("collins",87)

gradebook=Gradebook()
gradebook.add_student(s1)
gradebook.add_student(s2)
gradebook.add_student(s3)
print("class average",gradebook.get_average())
