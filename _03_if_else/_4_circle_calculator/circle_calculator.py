# Write a Python program that asks the user for the radius of a circle.
# Next, ask the user if they would like to calculate the area or circumference of a circle.
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.
import turtle
from tkinter import messagebox, simpledialog, Tk
import math

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    bob = turtle.Turtle()
    rad = simpledialog.askinteger(title="Circle Calculator", prompt="What is the radius?")
    aoc = simpledialog.askstring(title="Circle Calculator", prompt="Area or circumference?")
    if aoc == "area" or "Area":
        bob.circle(radius=rad)
        bob.penup()
        bob.goto(0, 0)
        area = math.pi * rad * rad
        bob.write(arg="area = " + str(area), move=True, align='left', font=('Arial', 8, 'normal'))
    else:
        bob.circle(radius=rad)
        bob.penup()
        bob.goto(0, 0)
        cir = 2 * math.pi * rad
        bob.write(arg="area = " + str(cir), move=True, align='left', font=('Arial', 8, 'normal'))
    bob.hideturtle()
    turtle.done()

#Area = πr^2
#Circumference = 2πr 