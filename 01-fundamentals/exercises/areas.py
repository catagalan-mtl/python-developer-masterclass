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
    while True:
        shape = input("What shape do you want to calculate?\n>").lower()
        if (shape == "circle" or shape == "rectangle" or shape == "triangle"):
            break
        else:
            print(f"{shape.capitalize()} is not a valid shape\n")

    if shape == "rectangle":
        while True:
            try:
                x = int(input("What's the lenght of the first side?\n>"))
                y = int(input("What's the lenght of the second side?\n>"))
                area = rectangle_area(x, y)
                break
            except(ValueError):
                print("Error: non numeric value\n")

    if shape == "triangle":
        while True:
            try:
                x = int(input("what's the base of the triangle?\n>"))
                y = int(input("what's the height of the triangle?\n>"))
                area = triangle_area(x, y)
                break
            except(ValueError):
                print("Error: non numeric value\n")

    if shape == "circle":
        while True:
            try:
                x = int(input("what's the radius of the circle?\n>"))
                area = circle_area(x)
                break
            except(ValueError):
                print("Error: non numeric value\n")

    print(f"The area of the {shape} is {area}\n---")
    return 0

main()
