class Father:
    def __init__(self, fname, lname):
        self.fname=fname
        self.lname=lname
    def skill1(self):
        print("golfing")

class Mother:
    def __init__(self, mname, lname):
        self.mname=mname
        self.lname=lname
    def skill2(self):
        print("vlogging")

class Child(Father, Mother):
    def __init__(self, fname, lname, mname, cname):
        Father.__init__(self, fname, lname)
        Mother.__init__(self, mname, lname)
        self.cname=cname
    def skills(self):
        print("child skills") 
    def display(self):
        print(f"fathers name is: {self.fname} {self.lname}" )
        print(f"mothers name is {self.mname} {self.lname}")
        print(f"childs name is {self.cname} {self.lname}")

s1=Child("father", "last", "mother", "child")
s1.skill1()
s1.skill2()
s1.display()
#MRO 
class A:
    def __init__(self):
        print("class A")

class B(A):
    def __init__(self):
        super().__init__()
        print("class B constructor")

class C(A):
    def __init__(self):
        super().__init__()
        print("class C constructor")

class D(B, C):
    def __init__(self):
        super().__init__()
        print("class D constructor")

obj1=D()

#create an employee system, parent class employee, salary; child class employee details(role), display fucntion(salary, name, role)
#create class camera and phone and calculator, phone calls camera, 