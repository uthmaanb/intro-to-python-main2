import tkinter
from tkinter import *

root = Tk()

# code to add widgets and style window will go here
root.geometry("500x650")
root.title("BMI-calc (Uthmaan Breda)")

# insert image
treadmill = PhotoImage(file="treadmill-removebg-preview.png")
img = Label(root, image=treadmill)
img.place(x=5, y=5)

# set variables
bmi = StringVar()
ibmi = StringVar()
w_input = StringVar()
h_input = StringVar()
a_input = StringVar()


# set frame for content
Label(root, text="Enter Weight, Height and Gender").place(x=150, y=120)
frame = Frame(root, bd=10, borderwidth="1", relief="sunken", padx="20", pady="20")
frame.place(x=5, y=150)

#  set and place labels and entries
label = Label(frame, text="Weight: ").grid(row=1, column=1)
entry1 = Entry(frame, textvariable=w_input)
entry1.focus()
entry1.grid(row=1, column=2)
label1 = Label(frame, text="kg").grid(row=1, column=3)

label3 = Label(frame, text="Height: ").grid(row=2, column=1)
entry2 = Entry(frame, textvariable=h_input)
entry2.grid(row=2, column=2)
label4 = Label(frame, text="cm").grid(row=2, column=3)

# more labels and entries
label6 = Label(frame, text="Age: ").grid(row=3, column=4)
entry3 = Entry(frame, textvariable=a_input, state=DISABLED)
entry3.grid(row=3, column=5)

# Gender (option menu and Placement)
label5 = Label(frame, text="Gender: ")
label5.grid(row=3, column=1)

option = ["Male", "Female"]  # set values for option list
values = StringVar(root)  # set variable to keep track of option value selected
values.set("Select an option")  # set the default value on display (a value from list can be put by saying option[0])


def activate(value):
    values.set(value)
    if value == "Female":
        entry3.config(state=NORMAL)
    elif value != "Female":
        entry3.config(state=DISABLED)


# Create the optionmenu widget and passing
# the option and values to it.
opt = OptionMenu(frame, values, *option, command=activate)
opt.config(width=15)
opt.grid(row=3, column=2)

# labels and entries for output
label7 = Label(root, text="BMI: ").place(x=10, y=350)
entry4 = Entry(root, textvariable=bmi, state="readonly")
entry4.place(x=50, y=350)
label8 = Label(root, text="Ideal BMI: ").place(x=250, y=350)
entry5 = Entry(root, textvariable=ibmi, state="readonly")
entry5.place(x=325, y=350)


def bmi_calc():
    if values.get() == "Male":
        weight = float(w_input.get())
        height = float(h_input.get())
        bmi_m_ans = ((0.5 * float(weight)) / ((float(height) / 100) ** 2)) + 11.5
        ibmi.set(bmi_m_ans)

        weight = float(w_input.get())
        height = float(h_input.get())
        bmi_ans = float(weight) / ((float(height) / 100) ** 2)
        bmi.set(bmi_ans)

    elif values.get() == "Female":

        weight = float(w_input.get())
        height = float(h_input.get())
        age = float(a_input.get())
        bmi_f_ans = ((0.5 * weight) / ((height / 100) ** 2)) + (0.03 * age) + 11
        ibmi.set(bmi_f_ans)

        weight = float(w_input.get())
        height = float(h_input.get())
        bmi_ans = float(weight) / ((float(height) / 100) ** 2)
        bmi.set(bmi_ans)


# kill program
def kill():
    return root.destroy()


def clear():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.config(state=NORMAL)
    entry4.config(state=NORMAL)
    entry5.config(state=NORMAL)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
    entry3.config(state="readonly")
    entry4.config(state="readonly")
    entry5.config(state="readonly")
    entry1.focus()
    values.set("Select an option")


# set button for bmi calculation
calc_bmi = Button(root, text="Calculate Ideal BMI", command=bmi_calc).place(x=150, y=300)

# make buttons for clear and exit function
clr_btn = Button(root, text="clear", command=clear).place(x=100, y=450)
kill_btn = Button(root, text="kill", command=kill).place(x=200, y=450)

root.mainloop()  # continuously runs program in window
