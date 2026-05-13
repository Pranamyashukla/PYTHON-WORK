class Father:
    def show(self):
        print("father")

class Child1(Father):
    def display1(self):
        print("this is child 1")

class Child2(Father):
    def display2(self):
        print("this is child 2")

class Child3(Father):
    def display3(self):
        print("this is child 3")

c1=Child1()
c2=Child2()
c3=Child3()
c1.show()
c1.display1()
c2.show()
c2.display2()

class Person:
    def __init__(self, name):
        self.name=name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject=subject
    def display(self):
        print(f"teacher: {self.name}, {self.subject}")

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade=grade
    def display(self):
        print(f"{self.name}, {self.grade}")

t1=Teacher("abc", "phy")
s1=Student("xyz", 97)
s1.display()

#class shape user input whats the shape, class circle, class rectangle, if input is circle, print area of circle else rectangle
