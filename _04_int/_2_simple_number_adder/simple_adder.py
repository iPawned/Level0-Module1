from tkinter import Tk, simpledialog, messagebox

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    numb1 = simpledialog.askinteger(title="Number Adder", prompt="Enter the first number you want to add:")
    numb2 = simpledialog.askinteger(title="Number Adder", prompt="Enter the second number you want to add:")
    numb3 = numb1 + numb2
    messagebox.showinfo(title="Number Adder", message="The answer is " + str(numb3) + ".")