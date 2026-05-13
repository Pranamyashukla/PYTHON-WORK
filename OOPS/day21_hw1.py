class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary   

    def display(self):
        print(f"Employee Name: {self.name}")
        print(f"Salary: ₹{self.__salary}")



e1 = Employee("Rahul", 50000)


e1.display()