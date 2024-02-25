# Import necessary packages
# Import tkinter to use GUI
import tkinter as tk
# Import requests to make API requests
import requests
# Import emoji to use emojis
import emoji

# Define the function to fetch weather data and call weather API
def getWeather(canvas):
    # Retrieves the value entered by user
    # Textfield is an instance of the 'Entry' widget in GUI created using tkinter
    # .get() is a method from 'Entry' that retrieves the value of the widget as a str
    city = textfield.get()

    #https://openweathermap.org/api/one-call-3 - get data from this website
    # API request to fetch weather data for the given city
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=f669e3dcecea4bda4abc83c3207936f3"
    # 'requests.get(api)' sends a HTTP GET request to the specified API endpoint
    # HTTP GET is a method used in the Hypertext Transfer Protocol (HTTP) for retrieving data or resources from a server
    # '.json()' converts json file into Python object so  you can perform further calculations/transformations
    json_data = requests.get(api).json()

    # Extract relevant weather information from the JSON file
    # [0] is used to access the first term  of the 'weather' array (the brackets)

    condition = json_data['weather'][0]['main']
    # int() function is used to convert float to integer
    temp = int(json_data['main']['temp'] - 273.15)
    feels_like = int(json_data['main']['feels_like'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']

    # Convert temperature from  Celcius to Fahrenheit
    new_temp = temp * 9 / 5 + 32
    new_min_temp = min_temp * 9 / 5 + 32
    new_max_temp = max_temp * 9 / 5 + 32
    new_feels_like = feels_like * 9 / 5 + 32

    # Prepare final information and data strings
    # Write how it will be printed in the app
    # Final_info stores the summary
    final_info = condition + '\n' + str(new_temp) + '°F\n'
    # Final_data stores the detailed info
    final_data = (
        standing_emoji + "Feels Like: " + str(new_feels_like) + '°F\n' +
        temperature_emoji + "Min Temp: " + str(new_min_temp) + '°F\n' +
        temperature_emoji + "Max Temp: " + str(new_max_temp) + '°F\n' +
        water_emoji + "Humidity: " + str(humidity) + '%\n' +
        wind_emoji + "Wind: " + str(wind) + ' mph'
    )

    # Update labels with weather information
    # Printing information in the GUI box
    label1.config(text=final_info)
    label2.config(text=final_data)

# Define icons using unicode (allows computers to understand icons)
cloud_emoji = '\u2601'
sun_emoji = '\u2600'
umbrella_emoji = '\u2614'
snowflake_emoji = '\u2744'
rainbow_emoji = '\U0001F308'
moon_emoji = '\U0001F319'
wind_emoji = '\U0001F4A8'
water_emoji = '\U0001F4A6'
pressure_emoji = '\U0001F4A5'
temperature_emoji = '\U0001F321'
standing_emoji = '\U0001F467'

# Create the main GUI window
canvas = tk.Tk()
# geometry() method allows you to define the size of the window
# Dimensions are width x height
# 600 pixels wide and 500 pixels high
canvas.geometry("600x500")
# Sets the title of the window and adds icons
canvas.title("Michelle's Weather App" + cloud_emoji + sun_emoji + umbrella_emoji + snowflake_emoji)

# Define font styles
f = ('poppins', 30, 'bold')
t = ('poppins', 41, 'bold')

# Creates an entry widget, centers the allignment, specifies the width(20 characters), and the font
textfield = tk.Entry(canvas, justify='center', width=20, font=t)
# Pack() method is used to organize widgets
# 'pady = 20' makes it so there are 20 pixels above and below the textfield widget
textfield.pack(pady=20)
# focus() method sets the keyboard focus on the textfield widget immediately when the GUI is launched
textfield.focus()
# blind() method associate an event with a function
# binds the  '<Return>' event to the getWeather function
# '<Return>' is basically pressing the 'enter' key
textfield.bind('<Return>', getWeather)

# label1 is for the final_info
# Applies the fonts to the information
label1 = tk.Label(canvas, font=t)
# '.pack()' function sizes it so that the preferred size is shown
label1.pack()

# label2 is for the final_data
label2 = tk.Label(canvas, font=f)
label2.pack()

# Starts/initiates the event loop for the Tkinter application
canvas.mainloop()