from tkinter import Tk, simpledialog, messagebox

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    numb1 = simpledialog.askinteger(title="Calculator", prompt="Enter the first number you want to calculate:")
    numb2 = simpledialog.askinteger(title="Calculator", prompt="Enter the second number you want to calculate:")
    func = simpledialog.askstring(title="Calculator", prompt="Would you like to add, subtract, multiply, or divide?")
    if func == "add":
        ans = numb1 + numb2
        messagebox.showinfo(title="Calculator", message="The answer is " + str(ans) + ".")

#* Use if-else statements to provide the desired math operation on the numbers
  #and display the result.