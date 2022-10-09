import requests
import tkinter as tk
from datetime import date, datetime

#function that gets the price of bitcoin from an API request and stores the data as json text
def btcTracker():
    url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR"
    response = requests.get(url).json()
    price = response["USD"]
    time = datetime.now().strftime("%H:%M:%S")

    label_Price.config(text = "$" + str(price))
    label_Time.config(text = "Price as of: " + time)

    canvas.after(1000, btcTracker)

#initalizes the UI window, size and name
canvas = tk.Tk()
canvas.geometry("400x500") 
canvas.title("Bitcoin Price Tracker")

#these are the fonts that the UI will use
font_1 = ("poppins", 24, "bold")
font_2 = ("poppins", 22, "bold")
font_3 = ("poppins", 18, "normal")

#this creates the title label for the UI
label = tk.Label(canvas, text = "Bitcoin Price", font = font_1)
label.pack(pady = 20)

#this creates the price label for the UI
label_Price = tk.Label(canvas, font = font_2)
label_Price.pack(pady=20)

#this creates the time label for the UI
label_Time = tk.Label(canvas, font = font_3)
label_Time.pack(pady = 20)


btcTracker()

canvas.mainloop()