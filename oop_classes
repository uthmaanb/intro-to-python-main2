class Shapes:  # creating the parent/ base/ super class
    def __init__(self, name, sides):  # giving the class attributes
        # naming the attributes
        self.name = name
        self.sides = sides

    def area(self):  # defining method/ function for class
        print("I am a: " + self.name + "\n" +
              "I have " + self.sides + " sides")


# defining object
obj_shape = Shapes("shape", "so many")
obj_shape.area()


class Rectangle(Shapes):
    def __init__(self, len1, wid1):
        self.length = len1
        self.width = wid1

    def area(self):
        result = self.length * self.width
        return result


obj_book = Rectangle(10, 7)
obj_screen = Rectangle(5, 7)
print("area of book: " + str(obj_book.area()))
print("area of screen: " + str(obj_screen.area()))


class Circle(Shapes):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        result = 3.14159265359 * self.radius**2
        return result


obj_pie = Circle(8)
print("area of pie: " + str(obj_pie.area()))


class Triangle(Shapes):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        result = 1/2 * self.height * self.width
        return result


obj_slice_pizza = Triangle(5, 8)
print("area of slice pizza: " + str(obj_slice_pizza.area()))
