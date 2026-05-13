class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class EmployeeDetails(Employee):
    def __init__(self, name, salary, role):
        super().__init__(name, salary)
        self.role = role

    def display(self):
        print(f"name: {self.name}")
        print(f"salary: {self.salary}")
        print(f"role: {self.role}")

e1 = EmployeeDetails("aman", 50000, "software engineer")
e1.display()