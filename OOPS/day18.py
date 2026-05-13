class Person:
    def __init__(self, name):
        self.name=name
    
class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary=salary

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade=grade
    
class Intern(Employee, Student):
    def __init__(self, name, salary, grade):
        Employee.__init__(self,name, salary)
        Student.__init__(self, name, grade)
    def display(self):
        print(f"{self.salary}, {self.grade}, {self.name}")
    

i1=Intern("pranamya", 30000, 12)
            
i1.display()
            
    