class Student:

    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def print_student(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks)

    def check_pass(self):
        if self.marks >= 40:
            print("Status: Passed")
        else:
            print("Status: Failed")


student1 = Student("Rahul", 12, 65)

student1.print_student()
student1.check_pass()