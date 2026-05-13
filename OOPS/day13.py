class Citizen:
    def __init__(self, name, age, gender):
        self.name=name
        self.age=age
        self.gender=gender
    def display1(self):
        print(self.name)
        print(self.age)
        print(self.gender)


p1=Citizen ("pranamya", 14, "male")
p1.display1()

class Person:
    pass
p2=Person()
p2.name="xyz"
p2.age=20
p2.gender="female"
print(p2.name)
print(p2.age)


#create a class car, house, shoes



class Car:
    def __init__(self, brand, color, engine):
        self.brand = brand
        self.color = color
        self.engine=engine

class House:
    def __init__(self, location, price):
        self.location = location
        self.price = price

class Shoes:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size

car1 = Car("toyota", "red", "v8")
house1 = House("new york", 500000)
shoes1 = Shoes("nike", 8)
print(car1.brand, car1.color, car1.engine)
print(house1.location, house1.price)
print(shoes1.brand, shoes1.size)


