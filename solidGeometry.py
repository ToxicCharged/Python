import math


class square:

    def __init__(self, side):
        self.a = side

    def diagonal(self):
        return math.sqrt(2) * self.a

    def perimeter(self):
        return 4 * self.a

    def area(self):
        return self.a ** 2


class rectangle:

    def __init__(self, length, breadth):
        self.l = length
        self.b = breadth

    def diagonal(self):
        return math.sqrt(self.l ** 2 + self.b ** 2)

    def perimeter(self):
        return 2 * (self.l + self.b)

    def area(self):
        return self.l * self.b


class circle:

    def __init__(self, radius):
        self.r = radius

    def circumference(self):
        return 2 * math.pi * self.r

    def area(self):
        return math.pi * self.r ** 2


class triangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        semiPerimeter = (self.a + self.b + self.c) / 2
        return math.sqrt(semiPerimeter * (semiPerimeter - self.a) * (semiPerimeter - self.b) * (semiPerimeter - self.c))


class cube:

    def __init__(self, side):
        self.a = side

    def diagonal(self):
        return math.sqrt(3) * self.a

    def perimeter(self):
        return 12 * self.a

    def lateralSurfaceArea(self):
        return 4 * self.a ** 2

    def totalSurfaceArea(self):
        return 6 * self.a ** 2

    def volume(self):
        return self.a ** 3


class cuboid:

    def __init__(self, length, breadth, height):
        self.l = length
        self.b = breadth
        self.h = height

    def diagonal(self):
        return math.sqrt(self.l ** 2 + self.b ** 2 + self.h ** 2)

    def perimeter(self):
        return 2 * (self.l + self.b + self.h)

    def lateralSurfaceArea(self):
        return 2 * (self.l + self.b) * self.h

    def totalSurfaceArea(self):
        return 2 * (self.l * self.b + self.b * self.h + self.l * self.h)

    def volume(self):
        return self.l * self.b * self.h


class sphere:

    def __init__(self, radius):
        self.r = radius

    def surfaceArea(self):
        return 4 * math.pi * self.r ** 2

    def volume(self):
        return 4 / 3 * math.pi * self.r ** 3


class hemisphere:

    def __init__(self, radius):
        self.r = radius

    def curvedSurfaceArea(self):
        return 2 * math.pi * self.r ** 2

    def totalSurfaceArea(self):
        return 3 * math.pi * self.r ** 2

    def volume(self):
        return 2 / 3 * math.pi * self.r ** 3


class cylinder:

    def __init__(self, radius, height):
        self.r = radius
        self.h = height

    def diagonal(self):
        return math.sqrt(4 * self.r ** 2 + self.h ** 2)

    def curvedSurfaceArea(self):
        return 2 * math.pi * self.r * self.h

    def totalSurfaceArea(self):
        return 2 * math.pi * self.r * (self.r + self.h)

    def volume(self):
        return math.pi * self.r ** 2 * self.h


class cone:

    def __init__(self, radius, height):
        self.height = height
        self.radius = radius
        self.slantHeight = math.sqrt(height ** 2 + radius ** 2)

    def curvedSurfaceArea(self):
        return math.pi * self.radius * self.slantHeight

    def totalSurfaceArea(self):
        return math.pi * self.radius * (self.slantHeight + self.radius)

    def volume(self):
        return 1/3 * math.pi * self.radius ** 2 * self.height


def main():

    print()
    print("1) 2d shapes")
    print("2) 3d solids")
    print()
    figure = input("Choose an option: ")
    print()

    if figure == '1':

        print("1) Square")
        print("2) Rectangle")
        print("3) Circle")
        print("4) Triangle")
        print()
        shape = input("Choose an option: ")

        if shape == '1':
            a = float(input("Enter side: "))
            squareObject = square(a)

            print()
            print("Diagonal = " + str(squareObject.diagonal()))
            print("Perimeter = " + str(squareObject.perimeter()))
            print("Area = " + str(squareObject.area()))

        elif shape == '2':
            l = float(input("Enter length: "))
            b = float(input("Enter breadth: "))
            rectangleObject = rectangle(l, b)

            print()
            print("Diagonal = " + str(rectangleObject.diagonal()))
            print("Perimeter = " + str(rectangleObject.perimeter()))
            print("Area = " + str(rectangleObject.area()))

        elif shape == '3':
            r = float(input("Enter radius: "))
            circleObject = circle(r)

            print()
            print("Circumference = " + str(circleObject.circumference()))
            print("Area = " + str(circleObject.area()))

        elif shape == '4':
            a = float(input("Enter first side: "))
            b = float(input("Enter second side: "))
            c = float(input("Enter third side: "))
            triangleObject = triangle(a, b, c)

            print()
            print("Perimeter = " + str(triangleObject.perimeter()))
            print("Area = " + str(triangleObject.area()))

        else:
            print("Invalid choice.")

    elif figure == '2':

        print("1) Cube")
        print("2) Cuboid")
        print("3) Sphere")
        print("4) Hemi Sphere")
        print("5) Cylinder")
        print("6) Cone")
        print()
        solid = input("Choose an option: ")

        if solid == '1':
            a = float(input("Enter side: "))
            cubeObject = cube(a)

            print()
            print("Diagonal = " + str(cubeObject.diagonal()))
            print("Perimeter = " + str(cubeObject.perimeter()))
            print("Lateral Surface Area = " + str(cubeObject.lateralSurfaceArea()))
            print("Total Surface Area = " + str(cubeObject.totalSurfaceArea()))
            print("Volume = " + str(cubeObject.volume()))

        elif solid == '2':
            l = float(input("Enter length: "))
            b = float(input("Enter length: "))
            h = float(input("Enter length: "))
            cuboidObject = cuboid(l, b, h)

            print()
            print("Diagonal = " + str(cuboidObject.diagonal()))
            print("Perimeter = " + str(cuboidObject.perimeter()))
            print("Lateral Surface Area = " + str(cuboidObject.lateralSurfaceArea()))
            print("Total Surface Area = " + str(cuboidObject.totalSurfaceArea()))
            print("Volume = " + str(cuboidObject.volume()))

        elif solid == '3':
            r = float(input("Enter radius: "))
            sphereObject = sphere(r)

            print()
            print("Surface Area = " + str(sphereObject.surfaceArea()))
            print("Volume = " + str(sphereObject.volume()))

        elif solid == '4':
            r = float(input("Enter radius: "))
            hemisphereObject = hemisphere(r)

            print()
            print("Curved Surface Area = " + str(hemisphereObject.curvedSurfaceArea()))
            print("Total Surface Area = " + str(hemisphereObject.totalSurfaceArea()))
            print("Volume = " + str(hemisphereObject.volume()))

        elif solid == '5':
            r = float(input("Enter radius: "))
            h = float(input("Enter height: "))
            cylinderObject = cylinder(r, h)

            print()
            print("Diagonal = " + str(cylinderObject.diagonal()))
            print("Curved Surface Area = " + str(cylinderObject.curvedSurfaceArea()))
            print("Total Surface Area = " + str(cylinderObject.totalSurfaceArea()))
            print("Volume = " + str(cylinderObject.volume()))

        elif solid == '6':
            r = float(input("Enter radius: "))
            h = float(input("Enter height: "))
            coneObject = cone(r, h)

            print()
            print("Curved Surface Area = " + str(coneObject.curvedSurfaceArea()))
            print("Total Surface Area = " + str(coneObject.totalSurfaceArea()))
            print("Volume = " + str(coneObject.volume()))

        else:
            print("Invalid choice.")

    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
