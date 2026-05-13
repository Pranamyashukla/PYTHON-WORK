class Doctor:
    def __init__(self):
        print("This is the base class")

    
    def bmi(weight, height):
        bmi = weight / (height ** 2)
        print("BMI is:", round(bmi, 2))

        
        if bmi < 18.5:
            print("category: underweight")
        elif 18.5 <= bmi < 24.9:
            print("category: normal weight")
        elif 25 <= bmi < 29.9:
            print("category: overweight")
        else:
            print("category: obese")

    @staticmethod
    def heartrate(heart_rate):
        if 60 < heart_rate < 100:
            print("heart rate is normal")
        else:
            print("you should go to the doctor")


class Patient(Doctor):
    def __init__(self, name, weight, height, heart_rate):
        self.patient_name = name
        self.patient_weight = weight
        self.patient_height = height
        self.patient_heart_rate = heart_rate

    def healthcheck(self):
        print("\nPatient name:", self.patient_name)
        Doctor.bmi(self.patient_weight, self.patient_height)
        Doctor.heartrate(self.patient_heart_rate)


p1 = Patient("Aryan", 60, 1.72, 90)
p1.healthcheck()

p2 = Patient("Aarav", 70, 1.5, 102)
p2.healthcheck()