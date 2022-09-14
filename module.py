def houseArea(length, width):
    area = length * width
    return area
length = float(input("What is the length of your house?: "))
width = float(input("What is the width of your house?: "))

print(houseArea(length, width))



pi = 3.14159
radius = int(input("Whats the radius of the circle?: "))
circumference = pi * radius ** 2

print("The circumference of the circle is: ", circumference)