from tkinter import simpledialog, Tk, messagebox

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    score = 0
    rid1 = simpledialog.askstring(title="Riddle 1:", prompt="The more you take, the more you leave behind. What am I?")
    if rid1 == "Footprints":
        print("Correct!")
        score = score + 1
    else:
        print("Incorrect")
    rid2 = simpledialog.askstring(title="Riddle 2:", prompt="What has a head, no legs, brown, and a tail?")
    if rid2 == "A penny":
        print("Correct!")
        score = score + 1
    else:
        print("Incorrect")
    rid3 = simpledialog.askstring(title="Riddle 3:", prompt="What belongs to you, but other people use more than you?")
    if rid3 == "Your name":
        print("Correct!")
        score = score + 1
    else:
        print("Incorrect")
    messagebox.showinfo(title="Results:", message="You got a " + str(score) + " out of 3!")