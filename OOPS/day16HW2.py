class Phone:
    def call(self):
        print("Calling")
        
class Camera(Phone):
    def call(self):
        super().call()
        print("Photo clicked")


class Calculator(Phone):
    def call(self):
        super().call()
        print("calc")
    

class Cellphone(Camera, Calculator):
    def call(self):
        print("This is a cellphone")
        super().call()

p1 = Cellphone()

p1.call()

