# class Employee:
#     def __init__(self, name, position):
#         self.name = name
#         self.position = position

#     def say_hi(self):
#         print(f'Hi! my name is {self.name}')

#     def tell_position(self):
#         print(f'I am a {self.position}')


# John = Employee('John', 'Software Engineer')

# John.say_hi()
# John.tell_position()
import math

class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_perimeter(self):
        return 2 * (self.height + self.width)
    
    def calculate_area(self):
        return self.height * self.width
    

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_perimeter(self):
        return 2 * self.radius  * math.pi
    
    def calculate_area(self):
        return math.pi * self.radius **2


def main():
    shape = input('shape: ')
    if shape == "rectangle":
        height = float(input("Height: "))
        width = float(input("Width: "))
        rectangle = Rectangle(height, width)
        perimeter = rectangle.calculate_perimeter()
        area = rectangle.calculate_area()
        print("=> Perimeter:", perimeter)
        print("=> Area:", area)
    elif shape == "circle":
        radius = float(input("Radius: "))
        circle = Circle(radius)
        perimeter = circle.calculate_perimeter()
        area = circle.calculate_area()
        print("=> Perimeter:", perimeter)
        print("=> Area:", area)
    else:
        print("=> Invalid!")

main()


from datetime import datetime

class CustomDate:
    def __init__(self):
        self.now = datetime.now()
    
    def get_date(self):
        return self.now.strftime("%d/%m/%Y")
    
    def get_time(self):
        return self.now.strftime("%H:%M:%S")

now = CustomDate()
print(now.get_date())
print(now.get_time())
