from tkinter import *

def change_color():
    current_color = box.cget("background")
    next_color = "orange" if current_color == "sky blue" else "sky blue"
    box.config(background=next_color)
    root.after(1000, change_color)

root = Tk(className="Light")
root.geometry("200x200")
box = Text(root, background="orange")
box.pack()
change_color()
