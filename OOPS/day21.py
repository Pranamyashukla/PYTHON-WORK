from abc import ABC, abstractmethod
class MLModel(ABC):
    @abstractmethod
    def train(self):
        pass
    @abstractmethod
    def predict(self):
        pass

class LinearRegression(MLModel):
    def train(self):
        print("training linear regression model")
    def predict(self):
        print("prediction using linear regression")

class DecisionTree(MLModel):
    def train(self):
        print("training decision tree model")
    def predict(self):
        print("prediction using decision tree")

models=[LinearRegression(), DecisionTree()]
for model in models:
    model.train()
    model.predict()

class Vehicle(ABC):
    @abstractmethod
    def accelerate(self):
        pass


class Car(Vehicle):
    def accelerate(self):
        print("car has a speed of 20kmh")

class Bike(Vehicle):
    def accelerate(self):
        print("bike has a speed of 30 kmph")

class Truck(Vehicle):
    def accelerate(self):
        print("truck has a speed of 10kmph")


v1=[Car(), Bike(), Truck()]
for vehicle in v1:
    vehicle.accelerate()

class Student:
    def __init__(self):
        self.name="pranamya"
        self._marks=90

s=Student()
print(s.name)
print(s._marks)

#accessing private variable using method
class Bank:
    def __init__(self, name, balance):
        self.__balance=balance
        self.name=name
    def deposit(self, amount):
        self.__balance+=amount
        print(f"deposited amount is {amount}")
    def withdraw(self, amount):
        if amount< self.__balance:
            self.__balance-=amount
            print(f"withdraw {amount}")
        else:
            print("insufficient balance")
    def showbalance(self):
        print(f"{self.__balance}")

pnb=Bank("abc", 80000)
pnb.deposit(2000)
pnb.withdraw(1300)
pnb.showbalance()

#employee salary system (salary private)
#product(name, price(private), profit loss, two cases selling, whether profit or loss)
