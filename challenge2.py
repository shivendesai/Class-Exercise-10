#Written by Shiven Desai
class Person:
    def __init__(self, name, age, address, city, state, zip_code):
        self.name = name
        self.age = age
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code

class Student(Person):
    def __init__(self, name, age, address, city, state, zip_code, studentID, GPA):
        super().__init__(name, age, address, city, state, zip_code)
        self.studentID = studentID
        self.GPA = GPA

class Teacher(Person):
    def __init__(self, name, age, address, city, state, zip_code, TeacherID, ClassTeaching):
        super().__init__(name, age, address, city, state, zip_code)
        self.TeacherID = TeacherID
        self.ClassTeaching = ClassTeaching

# Example usage
student = Student('Jane Doe', 25, '123 Main St', 'Anytown', 'CA', '12345', 777, 3.8)
print("Student Name: ", student.name)
print("Student Age: ", student.age)
print("Student Address: ", student.address)
print("Student City: ", student.city)
print("Student State: ", student.state)
print("Student Zip Code: ", student.zip_code)
print("Student ID: ", student.studentID)
print("Student GPA: ", student.GPA)

teacher = Teacher("Ms. Cantor", 45, '456 Elm St', 'Anytown', 'CA', '12345', 7, "Python")
print("Teacher Name: " , teacher.name)
print("Teacher Age: " , teacher.age)
print("Teacher Address: ", teacher.address)
print("Teacher City: ", teacher.city)
print("Teacher State: ", teacher.state)
print("Teacher Zip Code: ", teacher.zip_code)
print("Teacher ID: " , teacher.TeacherID)
print("Teacher Course: " , teacher.ClassTeaching)
