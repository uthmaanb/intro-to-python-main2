from tkinter import *
window = Tk()
window.config(bg="yellow")
window.title("Second Screen")
window.geometry("400x400")

results = StringVar()

Label(window, text="Sorted List:").place(x=10, y=150)
sort_ed = Label(window, text="", textvariable=results)
sort_ed.place(x=150, y=150)


def bubble():
    list_a = [4, 8, 1, 14, 8, 2, 9, 5, 7, 6, 6]

    indexing_length = len(list_a) - 1  # SCan not apply comparision starting with last item of list (No item to right)
    sorted_list = False  # Create variable of sorted and set it equal to false

    while not sorted_list:  # Repeat until sorted = True
        sorted_list = True  # Break the while loop whenever we have gone through all the values

        for i in range(0, indexing_length):  # For every value in the list
            if list_a[i] > list_a[i+1]:  # if value in list is greater than value directly to the right of it,
                sorted_list = False  # These values are unsorted
                list_a[i], list_a[i+1] = list_a[i+1], list_a[i]  # Switch these values
                results.set(list_a)
    results.set(list_a)


Button(window, text="Sort", command=bubble).place(x=180, y=100)


window.mainloop()
