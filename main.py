from shapes import Shapes, Rectangle, Triangle, Circle


def menu():
    print("welcome to shapes")
    choice = input("1: Rectangle\n2: Triangle\n3: circle\n:")
    if choice == "1":
        rectangle()
    elif choice == "2":
        triangle()
    elif choice == "3":
        circle()
    else:
        
        
    


def rectangle():
    width = float(input("enter width: "))
    height = float(input("enter height: "))
    rectangle = Rectangle(width, height)
    print(f"\narea is: {rectangle.calc_area()}\nperimeter is: {rectangle.calc_perimeter()}\n")
    pause()

def triangle():
    base = float(input("enter base: "))
    height = float(input("enter height: "))
    triangle = Triangle(base, height)
    print(f"\narea is {triangle.calc_area()}\nperimeter is {triangle.calc_perimeter()}\n")
    pause()

def circle():
    radius = float(input("enter radius: "))
    circle = Circle(radius)
    print(f"\narea is {circle.calc_area()}\nperimeter is {circle.calc_perimeter()}\n")
    pause()

def pause():
    input("\npress enter to continue: \n")


while True:
    menu()




