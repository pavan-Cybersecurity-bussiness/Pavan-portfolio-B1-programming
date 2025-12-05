#lab task 1
#1
class person :
    def __init__(self,name,age):
        self.name = name
        self.age =age

    def introduction(self):
        print(f"this is {self.name} and {self.name} is {self.age} years old")

# 2
class Student(person):
    def __init__(self, name, age, student_id):
        self.student_id = student_id
        super().__init__(name,age)

    def introduction(self):
        print(f"this is {self.name} and {self.name} is a student with student id{self.student_id} and is {self.age}")

#3
class Teacher(person):
    def __init__(self,name, age,subject):
        self.subject = subject
        super().__init__(name,age)

    def introduction(self):
        print(f"this is {self.name} and {self.name} is a teacher ,who teaches {self.subject} is {self.age} years old")

#testing


student1 = Student("Alice", 16, "S001")
teacher1 = Teacher("Mr. Smith", 35, "Mathematics")

student1.introduction()
teacher1.introduction()
