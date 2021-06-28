import tkinter as tk  # import as tkinter or as whatever you would like to call it
from tkinter import *  # import from tkinter whatever you are going to use or * to import everything
root = tk.Tk()  # root is parent window

# Code to add widgets will go here...
root.geometry("250x300")  # window size
root.title("Adding with Tkinter")  # title of window

num1 = StringVar()  # setting the variables you will use
num2 = StringVar()
res = StringVar()


number1 = Label(root, text="First: ")  # setting labels
number2 = Label(root, text="Second: ")
theResult = Label(root, text="Result: ")

number1.place(x=10, y=10)  # setting the place of labels
number2.place(x=10, y=45)
theResult.place(x=10, y=80)

entry1 = Entry(root, textvariable=num1)  # setting up entries for input, which variable it uses
entry2 = Entry(root, textvariable=num2)
result = Entry(root, textvariable=res, state="readonly")  # set results entry as a readonly because we don't want input


entry1.place(x=75, y=10)  # placing entry boxes
entry2.place(x=75, y=45)
result.place(x=75, y=80)


def add():  # defining function for addition
    one = int(num1.get())
    two = int(num2.get())
    resultss = one + two
    res.set(resultss)  # res is set variable and resultss is answer of function.


def clear():  # defining function for clearing the program
    entry1.delete(0, END)
    entry2.delete(0, END)
    result.config(state=NORMAL)  # because the clear function doesn't clear the readonly, change state to normal
    result.delete(0, END)
    result.config(state="readonly")  # change back to readonly


def kill():
    return root.destroy()


addbtn = Button(root, text="ADD", command=add)  # setting up buttons
clearbtn = Button(root, text="CLEAR", command=clear)
extbtn = Button(root, text="KILL", command=kill)

addbtn.place(x=10, y=120)  # placing buttons
clearbtn.place(x=90, y=120)
extbtn.place(x=185, y=120)


root.mainloop()  # continuously runs program in window
