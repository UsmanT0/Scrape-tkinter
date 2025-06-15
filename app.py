import tkinter as tk
from tkinter import ttk
from Scrape import scrape_weather

def display_weather():
    country = entry1.get().lower()
    city = entry2.get().lower()
    temp = scrape_weather(country,city)
    label.config(text=f"{country}, {city}: {temp}")

# GUI setup
root = tk.Tk()
root.title("Weather App")
root.geometry("300x300")

frame = ttk.Frame(root, padding=10)
frame.pack(fill=tk.BOTH, expand=True)

ttk.Label(frame, text="Enter Name of Country and City").pack()

entry1=ttk.Entry(frame)
entry1.pack()
entry2=ttk.Entry(frame)
entry2.pack()

ttk.Button(frame, text="Get Weather", command=display_weather).pack(pady=10)

label = ttk.Label(frame, text="")
label.pack()

root.mainloop()
