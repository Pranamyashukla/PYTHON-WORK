#POLYMORPHISM
print(len("hello world"))
print(len([1, 2, 3, 4, 5]))
class Animal:
    def sound(self):
        print("animal sound")

class Cow(Animal):
    def sound(self):
        print("moo")
    
class Cat(Animal):
    def sound(self):
        print("meow")

a=Animal()
b=Cow()
c=Cat()
a.sound()
b.sound()
c.sound()

print(5+3)
print("hello"+"world")
#duck typing
class Bird:
    def fly(self):
        print("bird can fly")

class Airplane:
    def fly(self):
        print("airplane can fly")


def make_fly(obj):
    obj.fly()

make_fly(Bird())
make_fly(Airplane())


class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius=radius
    def area(self):
        return 3.14*(self.radius**2)
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width

class Triangle(Shape):
    def __init__(self, height, base):
        self.base=base
        self.height=height
    def area(self):
        return 0.5*self.base*self.height
    
shapes=[Circle(7), Rectangle(10,11), Triangle(2, 5)]
for shape in shapes:
    print(shape.area())



class EmailNotification:
    def sent(self, message):
        print(message)
    
class SMSNotification:
    def sent(self, message):
        print(message)
class PushNotification:
    def sent(self, message):
        print(message)

def notify(obj):
    obj.sent("hello user") 

notify(EmailNotification())
notify(SMSNotification())
notify(PushNotification()) 

for n in [EmailNotification(), SMSNotification(), PushNotification()]:
    notify(n)

 
 
#create yoga app (diff classes as different types and level yoga)
#create rider booking app
