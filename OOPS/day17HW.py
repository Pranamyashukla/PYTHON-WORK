
class Shape:
    def get_shape(self):
        self.choice = input("enter shape (circle/rectangle): ").lower()

class Circle(Shape):
    def area(self):
        r = float(input("enter radius: "))
        area = 3.14 * r * r
        print(f"area of circle: {area}")


class Rectangle(Shape):
    def area(self):
        l = float(input("Enter length: "))
        b = float(input("Enter breadth: "))
        area = l * b
        print(f"area of rectangle: {area}")

s = Shape()
s.get_shape()

if s.choice == "circle":
    c = Circle()
    c.area()
else:
    r = Rectangle()
    r.area()


