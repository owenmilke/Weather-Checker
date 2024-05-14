# Owen Milke
# CS2300B

from flask import Flask, redirect, url_for, request, render_template, flash
import requests, json

# Creates Flask and secret key used for flash
app = Flask(__name__)
app.config['SECRET_KEY'] = '92051f34a4e348cd1311488984333c199abe2e57cc1fa4bf'

# The list of cities/locations entered by the user
cities = []
# The dictionary of cities/locations that will have their weather displayed
weather = []

# My personal API key for openweathermap
api_key = "2e4d9df079b22a7a57e13526c5f8681c"
# Base URL for openweathermap
base_url = "https://api.openweathermap.org/data/2.5/weather?"

# The index/start page of the Weather Checker site. Primary purpose is to display weather data from all of the user's entered cities/locations
@app.route('/')
def index():
    # Creates a temporary list to store weather data in to avoid duplicates
    temp_weather = []
    # For each city the user entered, go through and find that city's weather data
    for city in cities:
        user_input = city
        city_name = user_input
        state = ""
        # Checks to see if the city/location entered by the user contatins a ',', indicating that the user is choosing the state the city is in as well
        if (", " in user_input):
            # Separates the city name and state code from the ', ' part of the user's input
            city_name = user_input.partition(", ")[0]
            state_code = user_input.partition(", ")[2]
            if (len(state_code) == 2):
                state = "," + state_code + ",US"

        # Creates API URL with our custom parameters. This URL is recreated each time the page is loaded meaning weather data will update in realtime along with the API
        url = base_url + "appid=" + api_key + "&q=" + city_name + state + "&units=imperial"
    
        # Make API request and parse the json data
        response = requests.get(url)
        data = response.json()
    
        # Checks to see if the user entered city/location is viable
        if (data["cod"] == 200):
            # Allocates relevant parts of the parsed json to varialbles
            location = data["name"]
            country = data["sys"]["country"]
            temp = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            min_temp = data["main"]["temp_min"]
            max_temp = data["main"]["temp_max"]
            humidity = data["main"]["humidity"]
            wind = data["wind"]["speed"]
            description = data["weather"][0]["description"]
            
            # Saves the weather data variables to the temp weather dictionary
            temp_weather.append({'location': location,
                            'country': country, 
                            'temp': temp, 
                            'min_temp': min_temp, 
                            'max_temp': max_temp, 
                            'feels_like': feels_like, 
                            'humidity': humidity, 
                            'wind': wind, 
                            'description': description})
        else:
            # Notifies the user if their entered city/location can not be found by the API and removes that invalid city from the list of cities
            flash("Sorry, we couldn't find a city with that name. Please try again.")
            cities.remove(city)
    return render_template('index.html', cities=cities, weather=temp_weather)

# The page of the site that allows users to add a new weather location. Pulls input data from the html form
@app.route('/add/', methods=('GET', 'POST'))
def add():
    if request.method == 'POST':
        city = request.form['city']
        if not city:
            # Notifies the user if they entered a blank city name
            flash('City name is required!')
        else:
            # Adds the city name entered by the user to the list of cities
            cities.append(city)
            return redirect(url_for('index'))
    return render_template('add.html')

# Main function that runs the Flask app
if __name__ == '__main__':
    app.run()