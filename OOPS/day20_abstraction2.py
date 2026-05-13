from abc import ABC, abstractmethod
class Bankaccount(ABC):
    def __init__(self, holder, balance):
        self.holder=holder
        self.balance=balance
    @abstractmethod
    def interestcalc(self):
        pass

class SavingAccount(Bankaccount):
    def interestcalc(self):
        interest=self.balance*6.5
        print(f"saving interest is {interest}")

class CurrentAccount(Bankaccount):
    def interestcalc(self):
        interest=self.balance*0.6
        print(f"current interest is {interest}")

i1=SavingAccount("xyz", 2000)
i2=CurrentAccount("abc", 3000)
i1.interestcalc()
i2.interestcalc()


class Employee(ABC):
    def __init__(self, name):
        self.name=name
    @abstractmethod
    def calcsalary(self):
        pass

class FullEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary=monthly_salary
    def calcsalary(self):
        salary=self.monthly_salary*12
        print(f"{self.name} yearly salary is {salary}")

class PartTimeEmployee(Employee):
    def __init__(self, name, hours, rate):
        super().__init__(name)
        self.hours=hours
        self.rate=rate
    def calcsalary(self):
        salary=self.hours*self.rate
        print(f"{self.name} salary is {salary}")

        
s1=FullEmployee("a", 12000)
s2=PartTimeEmployee("b", 12, 400)

s1.calcsalary()
s2.calcsalary()

#university management system: student dashboard(subjects, assignments); teacher dashboard(subjects, assignments)
#"hospital managment system" inheritance, polymorphism,abstraction(Doctor management, Patient records , Appointment booking, Billing system, person(abstract class))
    