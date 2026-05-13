class Grandfather:
    def __init__(self):
        print("this is grandfather")

class Father(Grandfather):
    def __init__(self):
        super().__init__()
        print("this is father")

class Son(Father):
    def __init__(self):
        super().__init__()
        print("this is son")

c1=Son()


class Person:
    def __init__(self, name):
        self.name=name
        
class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary=salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department=department
    def display(self):
        print(f"{self.name}")
        print(f"{self.salary}")
        print(f"{self.department}")

p1=Manager("abc", 230000, "cybersecurity")
p1.display()


class Student:
    def __init__(self, name):
        self.name=name

class Marks(Student):
    def __init__(self, name, marks):
        super().__init__(name)
        self.marks=marks

class Result(Marks):
    def __init__(self, name, marks):
        super().__init__(name, marks)
    def display(self):
        print(f"{self.name}, {self.marks}")
        print("result:", "pass" if self.marks >= 250 else "fail")

p2=Result("xyz", 467)
p2.display()


