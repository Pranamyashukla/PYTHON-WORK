#abstract base class: us
from abc import ABC, abstractmethod

#abstract class
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

#child class

class Dog(Animal):
    def sound(self):
        print("dog barks")

class Cat(Animal):
    def sound(self):
        print("cat meow")

#objects

s1=Dog()
s2=Cat()

s1.sound()
s2.sound()

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(Payment):
    def pay(self, amount):
        print(f"paid {amount} using credit card")

class UPI(Payment):
    def pay(self, amount):
        print(f"paid {amount} using UPI")

c1=CreditCard()
c2=UPI()

c1.pay(100)
c2.pay(2000)