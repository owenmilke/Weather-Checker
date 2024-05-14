# M3OEP-omilke
<h2>Owen Milke CS2300B Module 3 Open-Ended Project</h2>

<h3>Required Insallations:</h3>
The required installations/imports for my program are Flask and requests. json is also used but I don't believe it needs to be installed manually. All of my instalations were able to be done using pip3 in the terminal.

<h3>Program Summary:</h3>
<h4>Program Description:</h4>
My program uses a combination of Python and html/css code utilizing Flask to make an interactive weather checking website that utilizes openweathermap's weather API to gather real time weather data from countries across the world.
The site is comprized of two main pages, 'My Locations' and 'Add Location'. 
The 'My Locations' page displays weather data for each validated city/location the user entered. Because the API URls that gather the weather data are recreated each time the 'My Locations' page is loaded, as soon as updated weather data is picked up by the API it will be updated on my website as well, meaning the weather data on my website is dynamic.
The 'Add Location' page allows the user to enter the name of a city they would like the weather for using Flask and an html form. The user is able to enter a city either in the form "City Name" or "City Name, State Abreviation" ("Burlington" or "Burlington, VT"). This added level of specification is often required when searching for cities in the US because if there are multiple cities with the same name, only the most popular will be shown my the API.
All weather data is stored on the site until the Flask app is shut down.

<h3>Languages:</h3>
<h4>Starting Language:</h4>
My program starts/runs in Python and uses html/css as a second language.

<h4>Why These Languages?</h4>
Python is used for scanning/parsing weather data from openweathermap's API and turning it into usable data, as well as a Flask app that allows Python and html to combine, while also being a way to run the website. I also thought that Python would be more effective than c++ for this project because if its readabilty and efficiency for utilizing APIs.
html/css is primarily used for the visual aspect as I believe this progam works better as a webstie than in a terminal. The html also has some dynamic elements utilizing integrated Python code that allows the contents of the page to change in a similar way to how PHP would.

<h4>How are the Languages Connected?</h4>
The program is started by running the Python file which starts the Flask app. html/css is then used to dynamically display everything being done by the Python code and the API data. Information is passed back and forth in a way as user input collected from the html form is passed into the Python code, which is then validated and used to collect data from the API, which then gets passed back to the html in order to be displayed on the webpage.

<h3>Known Bugs:</h3>
The only bug that I am aware of at the time of my submission is more an element of the API than my own code. The way the API is set up, if you were to enter 'Burlington, Vermont' it would not actually find weather data for Burlington, VT, as it wants either a the country or US state abreviation of the city, and would instead give you weather data of whatever the most popular Burlington is. Thats why in my code I have an If-statement that checks if the city the user attempted to enter includes it's state or not, as the entire API URL has to change if that precision is required.

<h3>Future Work:</h3>
* Adding the ability to remove a city from the user's saved list of weather data
* Changing the measument system used (I set it to Imperial for this program but Metric and Kelvin are also possible with this API)
* Making the program look nicer through more css work

<h3>Expected Grade:</h3>
I am very happy with the current state of my program as it was my first time using an API which is something I haven't had the opportunity to learn before. I also learned a lot more about Flask that I didn't know in my past experiences with it.
I believe that my program is complex enough for this project as it uses more than one programming language and required me to learn how to work with an API. My program as fully validates user input and is visually responsive.
I used both Python and html/css for this project and each language plays to their individual strenghts. Data is also passed between each language in both user input and data from the API.
My documentation is very robust and all elements of my code are explained.
My video goes over the content of my program and showcases multiple demo runs.
I created the repository over 7 days ago and worked on this project on at least 3 separate days.

Overall, after looking at the rubric, I could see getting between 80-100 points on this project depending on if it is deemed complex enough and the amount of languages I used are sufficient given what they do for my program.