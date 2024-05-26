from shapes import Shapes, Rectangle, Triangle, Circle

rectangle = Rectangle(10, 3)
print(f"area is {Rectangle.calc_area()}, perimeter is {Rectangle.calc_perimeter()}")

triangle = Triangle(3, 3)
print(f"area is {Triangle.calc_area()}, perimeter is {Triangle.calc_perimeter()}")

circle = Circle(5)
print(f"area is {Circle.calc_area()}, perimeter is {Circle.calc_perimeter()}")

