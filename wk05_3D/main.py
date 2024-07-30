from shapes.geometry import Circle, Rectangle

# radius = int(input("Raduis : "))
# width = int(input("Width: "))
# height = int(input("Height: "))

circle = Circle(radius=5)
rectangle = Rectangle(width=5, height=4)

# Print the area of the instantiated shapes
print(f"The area of the circle is: {circle.area()}")
print(f"The area of the rectangle is: {rectangle.area()}")