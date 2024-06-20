import requests
import tkinter as tk
import customtkinter
from tkinter import messagebox as m

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

def get_weather(city):
    api_key = "f6be5906359d00480b0462d14341e197"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={api_key}&q={city}&units=metric"

    try:
        response = requests.get(complete_url)
        response.raise_for_status()
        data = response.json()

        if data["cod"] != "404":
            main = data["main"]
            weather = data["weather"][0]
            temperature = main["temp"]
            humidity = main["humidity"]
            pressure = main["pressure"]
            weather_description = weather["description"]

            weather_report = (
                f"Weather in {city}:\n"
                f"Temperature: {temperature}°C\n"
                f"Humidity: {humidity}%\n"
                f"Pressure: {pressure} hPa\n"
                f"Description: {weather_description.capitalize()}"
            )
        else:
            weather_report = f"City {city} not found."

    except requests.exceptions.RequestException as e:
        weather_report = f"Error fetching weather data: {e}"

    return weather_report

def display_weather():
    city = city_entry.get()
    if city:
        weather_report = get_weather(city)
        result_label.configure(text=weather_report)
    else:
        m.showwarning("Input Error", "Please enter a city name.")

root = customtkinter.CTk()
root.title("Weather App")
root.geometry("500x400")
root.resizable(False, False)

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20)

city_label = customtkinter.CTkLabel(master=frame, text="Enter city name:")
city_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

city_entry = customtkinter.CTkEntry(master=frame, placeholder_text="City Name", width=200)
city_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

get_weather_button = customtkinter.CTkButton(master=frame, text="Get Weather", command=display_weather)
get_weather_button.grid(row=0, column=2, padx=5, pady=5, sticky=tk.W)

result_label = customtkinter.CTkLabel(master=root, text="", wraplength=450)
result_label.pack(pady=20)

root.mainloop()
