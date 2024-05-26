import math

class Shapes():

    def calc_area(self):
        pass


    def calc_perimeter(self):
        pass
    

class Rectangle(Shapes):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calc_area(self):
        return self.width * self.height
    
    def calc_perimeter(self):
        return 2 * (self.width + self.height)

class Triangle(Shapes):
    def __init__(self, base, height):
        self.base = base
        self.height = height
      
    def calc_area(self):
        return (self.base * self.height / 2) 

    def calc_perimeter(self):
        return 3 * self.base

class Circle(Shapes):
    def __init__(self, radius):
        self.radius = radius
        
    def calc_area(self):
        return round(math.pi * self.radius ** 2)

    def calc_perimeter(self):
        return round(2 * math.pi * self.radius)