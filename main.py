import sys
from geometry import *
import os

def print_menu():
    print('Learn Geometry, \n'
          'What do you want to do?, \n'
          '(1) Add new shape, \n'
          '(2) Show all shapes, \n'
          '(3) show shape with the largest perimeter, \n'
          '(4) show shape with the largest area, \n'
          '(5) Show formulas \n'
          '(0) Exit program \n')

def main():

    shapes = ShapeList()  # object containing all shapes added by the user
    while True:
        # TODO: implement user interaction here. You can change the code below
        os.system('clear')
        sp.ShapeList()
        print_menu()
        option = input("Which option would you like to choose?")
        if option == "1":
            which_shape = input("Which shape would u like to add ? ")
            print(" 1. Circle "
                  " 2. Triangle"
                  " 3. Equilateral triangle"
                  " 4. Rectangle"
                  " 5. Square"
                  " 6. Regular pentagon")
            if which_shape == "1":
                radius = input("Please type the radius lenght: ")
                c = Circle(int(radius))
                sp.add_shape(c)
                print("Shape added")
            if which_shape == "2":
                side1 = input("Please type first of sides lenghts: ")
                side2 = input("Please type second of sides lenghts: ")
                side3 = input("Please type third of sides lenghts: ")
                t = Triangle(int(side1), int(side2), int(side3))
                sp.add_shape(t)
                print("Shape added")
            if which_shape == "3":
                side = input("Please type the side lenght: ")
                e = EquilateralTriangle(int(side))
                sp.add_shape(e)
                print("Shape added")
            if which_shape == "4":
                side1 = input("Please type the first side: ")
                side2 = input("Please type the second side: ")
                r = Rectangle(int(side1), int(side2))
                sp.add_shape(r)
                print("Shape added")
            if which_shape == "5":
                side = input("Please type the side lenght: ")
                s = Square(int(side))
                sp.add_shape(s)
                print("Shape added")
            if which_shape == "6":
                side = input("Please type the side lenght: ")
                rp = RegularPentagon(int(side))
                sp.add_shape(rp)
                print("Shape added")
            else:
                print("You must type a number from one to six")
        elif option == "2":
            print(shapes.get_shapes_table())
        elif option == "3":
            shapes.get_largest_shape_by_perimeter()
        elif option == "4":
            shapes.get_largest_shape_by_area()
        elif option == "5":
            item_formula = input('Which item would you like to display formulas from? \n')
            print(" 1. Circle "
                  " 2. Triangle"
                  " 3. Equilateral triangle"
                  " 4. Rectangle"
                  " 5. Square"
                  " 6. Regular pentagon")
            if item_formula == "1":
                print("Circle perimeter: ", Circle.get_perimeter_formula()_formula())
                print("Circle area: ", Circle.get_area_formula())
                input("Type enter to continue  ")
            if item_formula == "2":
                print("Triangle perimeter: ", Triangle.get_perimeter_formula()_formula())
                print("Triangle area: ", Triangle.get_area_formula())
                input("Type enter to continue  ")
            if item_formula == "3":
                print("Equilateral Triangle perimeter: ", EquilateralTriangle.get_perimeter_formula()_formula())
                print("Equilateral Triangle area: ", EquilateralTriangle.get_area_formula())
                input("Type enter to continue  ")
            if item_formula == "4":
                print("Rectangle perimeter: ", Rectangle.get_perimeter_formula()_formula())
                print("Rectangle area: ", Rectangle.get_area_formula())
                input("Type enter to continue  ")
            if item_formula == "5":
                print("Square perimeter: ", Square.get_perimeter_formula()_formula())
                print("Square area: ", Square.get_area_formula())
                input("Type enter to continue  ")
            if item_formula == "6":
                print("Regular Pentagon perimeter: " RegularPentagon.get_perimeter_formula()_formula())
                print("Circle area: " RegularPentagon.get_area_formula())
                input("Type enter to continue  ")
            else:
                print("You must type a number from one to six")
        elif option == "0":
            sys.exit()

if __name__ == "__main__":
    main()

