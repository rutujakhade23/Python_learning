class Student:
    # subject = "Python"
    # college = "ABC"
    # year = "4th year"
    def __init__(self):
        print("obj is being constructed")


    def __init__(self, name, cgpa):   #parametrized constructor
        self.name = name
        self.cgpa = cgpa

    def get_cgpa(self):
        return self.cgpa


stu1 = Student("Rutuja", 9.2)
stu2 = Student("Swaraj", 9.8)
print(stu1.name, stu1.cgpa)
print(stu2.name, stu2.cgpa)
# print(stu1.subject, stu1.college, stu1.year)
# print(type(stu1))

print(f"{stu2.name} has cgpa = {stu2.get_cgpa()}")