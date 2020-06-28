class Student:
    def __init__(self,name,grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)


student = Student("Pepe",(90,21,54,78))
print(student.average())