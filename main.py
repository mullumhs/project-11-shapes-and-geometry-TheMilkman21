from shapes import shapes, rectangle, triangle, circle

rectangle = rectangle(10, 3)
print(f"area is {rectangle.calc_area()}, perimeter is {rectangle.calc_perimeter()}")

triangle = triangle(3, 3)
print(f"area is {triangle.calc_area()}, perimeter is {triangle.calc_perimeter()}")

circle = circle(5)
print(f"area is {circle.calc_area()}, perimeter is {circle.calc_perimeter()}")

