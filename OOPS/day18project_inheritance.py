class Person:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"name: {self.name}")

class Student(Person):
    def student_role(self):
        print("i am a student")

class Teacher(Person):
    def teacher_role(self):
        print("i am a teacher")

class Staff(Person):
    def staff_role(self):
        print("i am staff")

class CR(Student):
    def cr_role(self):
        print("i am class representative (cr)")

class Principal(Teacher):
    def principal_role(self):
        print("i am principal")

class HeadManager(Staff):
    def manager_role(self):
        print("i am the head manager")

class ScienceRep(Student):
    def science_role(self):
        print("i am science representative")

class SuperTeacher(Teacher, ScienceRep):
    def super_role(self):
        print("i am a super teacher (teacher and science representative)")

print("CR") 
cr = CR("aman") 
cr.show()
cr.student_role()
cr.cr_role()

print("principal")
p = Principal("aarav")
p.show()
p.teacher_role()
p.principal_role()

print("head manager")
hm = HeadManager("raj")
hm.show()
hm.staff_role()
hm.manager_role()

print("super teacher")
st = SuperTeacher("harleen")
st.show()
st.teacher_role()
st.science_role()
st.super_role()
