class University:
    def __init__(self, name):
        self.name = name


class StudentDashboard(University):
    def __init__(self, name, subjects, assignments):
        super().__init__(name)
        self.subjects = subjects
        self.assignments = assignments

    def display(self):
        print("----- Student Dashboard -----")
        print(f"Student Name: {self.name}")
        print(f"Subjects: {self.subjects}")
        print(f"Assignments: {self.assignments}")


class TeacherDashboard(University):
    def __init__(self, name, subjects, assignments):
        super().__init__(name)
        self.subjects = subjects
        self.assignments = assignments

    def display(self):
        print("----- Teacher Dashboard -----")
        print(f"Teacher Name: {self.name}")
        print(f"Subjects Teaching: {self.subjects}")
        print(f"Assignments Given: {self.assignments}")


s1 = StudentDashboard(
    "Rahul",
    ["Maths", "Physics", "Computer Science"],
    ["Math Assignment", "Python Project"]
)

t1 = TeacherDashboard(
    "Mrs Sharma",
    ["Computer Science", "AI"],
    ["OOP Worksheet", "AI Research Task"]
)

s1.display()

print()

t1.display()
