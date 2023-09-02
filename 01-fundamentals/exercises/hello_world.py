import math

def rectangle_area(side1, side2):
    area = side1 * side2
    return area

def triangle_area(base, height):
    area = (base * height) / 2
    return area

def circle_area(r):
    area = math.pi * (r ** 2)
    return round(area, 2)

def main():
    shape = input("What shape do you want to calculate?\n>").lower()

    if shape == "rectangle":
        x = int(input("What's the lenght of the first side?\n>"))
        y = int(input("What's the lenght of the second side?\n>"))
        area = rectangle_area(x, y)
    elif shape == "triangle":
        x = int(input("what's the base of the triangle?\n>"))
        y = int(input("what's the height of the triangle?\n>"))
        area = triangle_area(x, y)
    elif shape == "circle":
        x = int(input("what's the radius of the circle?\n>"))
        area = circle_area(x)
    else:
        print(f"{shape.capitalize()} is not a valid shape")
        return 1

    print(f"The area of the {shape} is {area}\n---")
    return 0

main()
