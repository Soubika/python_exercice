'''
Python : programmation orientée objet
Openclasseroom
'''

class Rectangle:
    
    def __init__(self, length, width, color = "red"):
        self.length = length
        self.width = width
        self.color = color

    
    def calculate_area(self):
        return self.width * self.length

rectangle = Rectangle(2, 3)
rect1 = Rectangle(5, 3, "blue")
rect2 = Rectangle(3, 1, "pink")

print(rectangle.length)
rectangle.color="yellow"

area = rectangle.calculate_area()
print(area)
