class Father:
    def __init__(self, name):
        self.name=name
    def showname(self):
        print("Fathers name is:", self.name)
    def occupation(self):
        print("Father is a doctor")


class Child(Father):
    def __init__(self, name, age):
        super().__init__(name)
        self.age=age
    def showdetails(self):
        print("Childs name is", self.name)
        print(self.age)

s=Child("pranam", 15)
s.showname()
s.occupation()
s.showdetails()
 

class Animal:
    def sound(self):
        print("animal makes sound")

class Dog(Animal):
    def sound(self):
        print("dog barks")
        print("my name is", self.name)


d=Dog()
d.name="shadow"
d.sound()



class Doctor:
    def __init__(self):
        print("This is the base class")
    def bmi(weight, height):
        bmi= weight/(height**2)
        print("BMI is", bmi)
    def heartrate(heart_rate):
        if heart_rate>60 and heart_rate<100:
            print("heart rate is normal")
        else:
            print("you should go to the doctor")
    
class Patient(Doctor):
    def __init__(self, name, weight, height, heart_rate):
        self.patient_name=name
        self.patient_weight=weight
        self.patient_height=height
        self.patient_heart_rate=heart_rate
    def healthcheck(self):
        print("\n patient name: ", self.patient_name)
        Doctor.bmi(self.patient_weight, self.patient_height)
        Doctor.heartrate(self.patient_heart_rate)

p1=Patient("Aryan", 60, 1.72, 90)
p1.healthcheck()
p2=Patient("Aarav", 70, 1.5, 102)
p2.healthcheck()





