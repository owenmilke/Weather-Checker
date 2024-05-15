<h1>Weather Checker - Owen Milke</h1>

<h3>Required Insallations:</h3>
The required installations/imports for this program are Flask and requests. All instalations are able to be done using pip3 in the terminal.

<h3>Program Summary:</h3>
<h4>Program Description:</h4>
My program uses a combination of Python and html/css code utilizing Flask to make an interactive weather checking website that utilizes openweathermap's weather API to gather real time weather data from countries across the world.
The site is comprized of two main pages, 'My Locations' and 'Add Location'. 
The 'My Locations' page displays weather data for each validated city/location the user entered. Because the API URls that gather the weather data are recreated each time the 'My Locations' page is loaded, as soon as updated weather data is picked up by the API it will be updated on my website as well, meaning the weather data on my website is dynamic.
The 'Add Location' page allows the user to enter the name of a city they would like the weather for using Flask and an html form. The user is able to enter a city either in the form "City Name" or "City Name, State Abreviation" ("Burlington" or "Burlington, VT"). This added level of specification is often required when searching for cities in the US because if there are multiple cities with the same name, only the most popular will be shown my the API.
All weather data is stored on the site until the Flask app is shut down.

<h3>Known Bugs:</h3>
The only bug that I am aware of at the time of my submission is more an element of the API than my own code. The way the API is set up, if you were to enter 'Burlington, Vermont' it would not actually find weather data for Burlington, VT, as it wants either a the country or US state abreviation of the city, and would instead give you weather data of whatever the most popular Burlington is. Thats why in my code I have an If-statement that checks if the city the user attempted to enter includes it's state or not, as the entire API URL has to change if that precision is required.

<h3>Future Work:</h3>

* Adding the ability to remove a city from the user's saved list of weather data
* Changing the measument system used (I set it to Imperial for this program but Metric and Kelvin are also possible with this API)
* Making the program look nicer through more css work
