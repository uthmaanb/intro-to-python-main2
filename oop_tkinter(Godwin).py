# Importing the request and tkinter libraries
import requests
from tkinter import *
from tkinter import messagebox


# Function calling the weather api
def my_weather():
    # Using try and except for error handling
    try:
        city = e1.get()
        url = "https://api.openweathermap.org/data/2.5/weather"
        weatherkey = "b2b3f0036842212c33dbc6743338c9dc"
        params1 = {'appid': weatherkey, 'q': city, 'units': 'Metric'}
        response = requests.get(url, params=params1)
        weather = response.json()
        lab2.config(text=weather['weather'][0]['main'], bg="#ffffff")
        temp.config(text=weather['main']['temp'], bg="#ffffff")
        country.config(text=weather['sys']['country'], bg="#ffffff")
        hum.config(text=weather['main']['humidity'], bg="#ffffff")
        wind.config(text=weather['wind']['speed'], bg="#ffffff")
        city_name.config(text=weather['name'], bg="#ffffff")
        desc.config(text="Weather Description: ", bg="#ffffff")
        lab3.config(text="Temperature: ", bg="#ffffff")
        lab4.config(text="Humidity: ", bg="#ffffff")
        lab5.config(text="Wind Speed: ", bg="#ffffff")
        lab6.config(text="City: ", bg="#ffffff")
        lab7.config(text="Country: ", bg="#ffffff")
    except requests.exceptions.ConnectionError:
        messagebox.showerror("Error", "No Internet Connection")
    except ValueError:
        if e1.get() != str:
            messagebox.showerror("Error", "Invalid! Please Use Strings")
    except KeyError:
        messagebox.showerror("Error", "Invalid! Please put a proper place!")


# Function for Exit button
def exit_btn():
    return root.destroy()


# Function for Clear button
def clear_btn():
    e1.delete(0, END)
    lab2.config(text=" ", bg="aqua")
    temp.config(text=" ", bg="aqua")
    country.config(text=" ", bg="aqua")
    hum.config(text=" ", bg="aqua")
    wind.config(text=" ", bg="aqua")
    city_name.config(text=" ", bg="aqua")
    desc.config(text=" ", bg="aqua")
    lab3.config(text=" ", bg="aqua")
    lab4.config(text=" ", bg="aqua")
    lab5.config(text=" ", bg="aqua")
    lab6.config(text=" ", bg="aqua")
    lab7.config(text=": ", bg="aqua")


# Making Tkinter Window
root = Tk()
root.title("Weather App")
root.geometry("500x500")


# Frames
myframe = Frame(root, bg="aqua")
myframe.place(x=10, y=10, width=750, height=500)

# Labels
lab1 = Label(myframe, text="Enter a City: ", bg="aqua")
lab1.place(x=20, y=10)
lab2 = Label(myframe, text="", bg="aqua")
lab2.place(x=180, y=150)
desc = Label(myframe, text="", bg="aqua")
desc.place(x=20, y=150)
lab3 = Label(myframe, text="", bg="aqua")
lab3.place(x=20, y=175)
temp = Label(myframe, text="", bg="aqua")
temp.place(x=180, y=175)
hum = Label(myframe, text="", bg="aqua")
hum.place(x=180, y=200)
lab4 = Label(myframe, text="", bg="aqua")
lab4.place(x=20, y=200)
wind = Label(myframe, text="", bg="aqua")
wind.place(x=180, y=225)
lab5 = Label(myframe, text="", bg="aqua")
lab5.place(x=20, y=225)
country = Label(myframe, text="", bg="aqua")
country.place(x=180, y=275)
lab6 = Label(myframe, text="", bg="aqua")
lab6.place(x=20, y=250)
lab7 = Label(myframe, text="", bg="aqua")
lab7.place(x=20, y=275)
city_name = Label(myframe, text="", bg="aqua")
city_name.place(x=180, y=250)


# Entries
e1 = Entry(myframe)
e1.place(x=120, y=10)

# Buttons
b1 = Button(myframe, text="Give me the Weather", command=my_weather, bg="green")
b1.place(x=20, y=50)
leave = Button(myframe, text="Exit", command=exit_btn, bg="#ed2d34")
leave.place(x=255, y=50)
clear = Button(myframe, text="Clear", command=clear_btn, bg="#ffffff")
clear.place(x=190, y=50)


root.mainloop()
