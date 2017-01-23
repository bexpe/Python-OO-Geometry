import math

class Shape:
    """
    This is an abstract class representing geometrical shape.
    """

    def __init__(self, *arguments):
        """
        Constructs Shape object

        Raises:
            ValueError: If any of the parameters is below 0.
        """
        for arg in arguments:
            if arg <= 0:
                raise ValueError("{} must be bigger than 0".format(arg))

    def get_area(self):
        """
        Calculates shape's area.

        Returns:
            float: area of the shape
        """
        raise NotImplementedError

    def get_perimeter(self):
        """
        Calculates shape's perimeter.

        Returns:
            float: perimeter of the shape
        """
        raise NotImplementedError

    def __str__(self):
        """
        Returns information about the shape as string.

        Returns:
            str: information about shape
        """
        raise NotImplementedError

    @classmethod
    def get_area_formula(cls):
        """
        Returns formula for the area of the shape as a string.

        Returns:
            str: area formula
        """
        return cls.FORMULA_AREA

    @classmethod
    def get_perimeter_formula(cls):
        """
        Returns formula for the perimeter of the shape as a string.

        Returns:
            str: perimeter formula
        """
        return cls.FORMULA_PERIMETER


class Circle(Shape):
    FORMULA_AREA = 'Area = π×r^2'
    FORMULA_PERIMETER = 'Perimeter = 2×π×r'

    def __init__(self, r):
        """
        Constructs Shape object

        Raises:
            ValueError: If any of the parameters is below 0.
        """
        Shape.__init__(self, *[r])
        self.r = r

    def get_area(self):
        """
        Calculates shape's area.

        Returns:
            float: area of the shape
        """
        try:
            self.circle_area = math.pi * self.r ** 2
            return self.circle_area
        except:
            print('Please enter one valid arg')

    def get_perimeter(self):
        """
        Calculates shape's perimeter.

        Returns:
            float: perimeter of the shape
        """
        try:
            self.circle_perimeter = 2 * math.pi * self.r
            return self.circle_perimeter
        except:
            print('Please enter one valid arg')

    def __str__(self):
        """
        Returns information about the shape as string.

        Returns:
            str: information about shape
        """
        return 'Circle, radius = {}'.format(self.r)

class Triangle(Shape):
    FORMULA_AREA = 'Area = math.sqrt(s*(s-a)*(s-b)*(s-c))'
    FORMULA_PERIMETER = 'Perimeter = a+b+c'

    def __init__(self, a, b, c):
        """
        Constructs Shape object

        Raises:
            ValueError: If any of the parameters is below 0.
        """
        Shape.__init__(self, *[a, b, c])
        self.a = a
        self.b = b
        self.c = c

    def get_area(self):
        """
        Calculates shape's area.

        Returns:
            float: area of the shape
        """
        s = (self.a+self.b+self.c)/2
        try:
            self.triangle_area = math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
            return self.triangle_area
        except ValueError:
            print('Please enter 3 valid sides')

    def get_perimeter(self):
        """
        Calculates shape's perimeter.

        Returns:
            float: perimeter of the shape
        """
        try:
            self.triangle_perimeter = self.a+self.b+self.c
            return self.triangle_perimeter
        except:
            print('Please enter 3 valid sides')
    def __str__(self):
        """
        Returns information about the shape as string.

        Returns:
            str: information about shape
        """
        return 'Triangle, a = {}, b = {} and c = {}'.format(self.a, self.b, self.c)


class EquilateralTriangle(Triangle):
    FORMULA_AREA = 'Area = math.sqrt(s*(s-a)*(s-b)*(s-c))'
    FORMULA_PERIMETER = 'Perimeter = a^3'

    def __init__(self, a):
        """
        Constructs Shape object

        Raises:
            ValueError: If any of the parameters is below 0.
        """
        Triangle.__init__(self, *[a, a, a])
        self.a = a

    def get_area(self):
        """
        Calculates shape's area.

        Returns:
            float: area of the shape
        """
        s = (self.a + self.b + self.c) / 2
        try:
            self.equilateral_area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
            return self.equilateral_area
        except:
            print('Please enter one valid side')
    def get_perimeter(self):
        """
        Calculates shape's perimeter.

        Returns:
            float: perimeter of the shape
        """
        try:
            self.equilateral_perimeter = self.a*3
            return self.equilateral_perimeter
        except:
            print('Please enter one valid side')
    def __str__(self):
        """
        Returns information about the shape as string.

        Returns:
            str: information about shape
        """
        return 'Equilateral triangle, a = {}'.format(self.a)


class Rectangle(Shape):
    FORMULA_AREA = 'Area = a*b'
    FORMULA_PERIMETER = 'Perimeter = 2a+2b'

    def __init__(self, a, b):
        """
        Constructs Shape object

        Raises:
            ValueError: If any of the parameters is below 0.
        """
        Shape.__init__(self, *[a, b])
        self.a = a
        self.b = b

    def get_area(self):
        """
        Calculates shape's area.

        Returns:
            float: area of the shape
        """
        try:
            self.rectangle_area = self.a * self.b
            return self.rectangle_area
        except:
            print('Please enter 2 valid sides')

    def get_perimeter(self):
        """
        Calculates shape's perimeter.

        Returns:
            float: perimeter of the shape
        """
        try:
            self.rectangle_perimeter = 2*self.a + 2*self.b
            return self.rectangle_perimeter
        except:
            print('Please enter 2 valid sides')

    def __str__(self):
        """
        Returns information about the shape as string.

        Returns:
            str: information about shape
        """
        return 'Rectangle, a = {} and b = {}'.format(self.a, self.b)

class Square(Rectangle):
    FORMULA_AREA = 'Area = a^2'
    FORMULA_PERIMETER = 'Perimeter = 4a'

    def __init__(self, a):
        """
        Constructs Shape object

        Raises:
            ValueError: If any of the parameters is below 0.
        """
        Rectangle.__init__(self, *[a, a])
        self.a = a

    def get_area(self):
        """
        Calculates shape's area.

        Returns:
            float: area of the shape
        """
        try:
            self.square_area = self.a ** 2
            return self.square_area
        except:
            print('Please enter one valid arg')

    def get_perimeter(self):
        """
        Calculates shape's perimeter.

        Returns:
            float: perimeter of the shape
        """
        try:
            self.square_perimeter = 4 * self.a
            return self.square_perimeter
        except:
            print('Please enter one valid arg')

    def __str__(self):
        """
        Returns information about the shape as string.

        Returns:
            str: information about shape
        """
        return 'square, a = {}'.format(self.a)


class RegularPentagon(Shape):
    FORMULA_AREA = 'Area = math.sqrt(s*(s-a)*(s-b)*(s-c))'
    FORMULA_PERIMETER = 'Perimeter = a+b+c'

    def __init__(self, a):
        """
        Constructs Shape object

        Raises:
            ValueError: If any of the parameters is below 0.
        """
        Shape.__init__(self, *[a])
        self.a = a

    def get_area(self):
        """
        Calculates shape's area.

        Returns:
            float: area of the shape
        """
        try:
            self.pentagon_area = self.a**2 * math.sqrt(5*(5+2*math.sqrt(5)))/4
            return self.pentagon_area
        except:
            print('Please enter one valid side')

    def get_perimeter(self):
        """
        Calculates shape's perimeter.

        Returns:
            float: perimeter of the shape
        """
        try:
            self.pentagon_perimeter = 5*self.a
            return self.pentagon_perimeter
        except:
            print('Please enter one valid side')

    def __str__(self):
        """
        Returns information about the shape as string.

        Returns:
            str: information about shape
        """
        return 'Regular pentagon, a = {}'.format(self.a)


class ShapeList:
    def __init__(self, shapes = None):
        if shapes == None:
            shapes = []
        if type(shapes) != list:
            raise TypeError("Your dates should be in the list. ")

        self.shapes = shapes

    def add_shape(self, shape):
        """
        Adds shape to shapes list. This method should check if shape's has Shape class as it's ancestor(przodek).
        If not it should raise TypeError. Hint: check is instance function.
        (This is a good example of so called polymorphism)
        """
        if isinstance(shape, Shape):
            self.shapes.append(shape)
        else:
            raise TypeError("Shape should be an instance class!")
        return self.shapes

    def get_largest_shape_by_perimeter(self):
        """
        Returns shape with the largest perimeter.
        :return: Shape object
        """
        max_perimeter = 0
        max_perimeter_object = None
        for line in self.shapes:
            if line.get_perimeter() > max_perimeter:
                max_perimeter = line.get_perimeter()
                max_perimeter_object = line
                # print(max_perimeter)
        return max_perimeter_object


    def get_largest_shape_by_area(self):
        """
        Returns shape with the largest area.

        :return: Shape object
        """
        max_area = 0
        max_area_object = None
        for line in self.shapes:
            if line.get_area() > max_area:
                max_area = line.get_area()
                max_area_object = line
                # print(max_area)
        return max_area_object

    def get_shapes_table(self):
        """
        Returns a table with objects list, which was formated to a str.
        """
        title_list = ['idx', 'class', '__str__', 'Perimeter', 'P. Formula', 'Area', 'A. Formula']
        table = []
        str_table = ''
        print(self.shapes)
        for iterator, shape in enumerate(self.shapes):
            table.append([str(iterator + 1), type(shape).__name__, shape.__str__(), str(round(shape.get_perimeter(), 1)),
            shape.get_perimeter_formula(), str(shape.get_area()), shape.get_area_formula()])  # adding all args
        print(table)
        column_length = []
        for title_iterator in range(len(title_list)):
            column_len = len(title_list[title_iterator])
            for line in table:
                if len(line[title_iterator]) > column_len:
                    column_len = len(line[title_iterator])
            column_length.append(column_len)  # making column lenght proper to the text size

        how_wide = 0
        for name in title_list:
            x = (column_length[title_list.index(name)])
            how_wide += (len(("|{: <" + str(x + 2) + "}|").format(name)))
        str_table += ('-' * how_wide)
        str_table += '\n'  # adding frames of a table in a proper size

        for name in title_list:
            str_table += "|"
            x = (column_length[title_list.index(name)])
            str_table += (("{: <" + str(x + 2) + "}").format(name))
            str_table += "|"
        str_table += '\n'
        str_table += ('-' * how_wide)
        str_table += '\n'  # dividing columns


        for row in table:
            str_table += '\n'
            str_table += "|"

            for element in row:
                x = (column_length[row.index(element)])
                str_table += (("|{: <" + str(x + 2) + "}|").format(element))
        return str_table  # returning a table as a string

# sp = ShapeList()
# a = Triangle(3,5,9)
# c = Circle(50)
# d = Circle(2)
# e = Triangle(3,4,5)
# sp.add_shape(a)
# sp.add_shape(c)
# sp.add_shape(d)
# sp.add_shape(e)
#
# # sp.get_largest_shape_by_perimeter()
# # sp.get_largest_shape_by_area()
# sp.get_shapes_table()