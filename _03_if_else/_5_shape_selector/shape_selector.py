import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    jeff = turtle.Turtle()
    # Ask the user what shape they want to draw and store it in a variable
    shape = simpledialog.askstring(title="What Shape?", prompt="Circle or Square?")
    # Draw the shape requested by the user using if-elif-else statements
    if shape == "Circle":
        jeff.circle(150)
    else:
        for i in range(4):
            jeff.left(90)
            jeff.forward(100)
    # Call the turtle .done() method
    turtle.done()