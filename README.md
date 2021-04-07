# corona-dashboard
Analysis of COVID-19 data with visualizations that are shown in a WebApp.
Checkout the WebApp directly by following this [link](https://covid-19-data-comparison.herokuapp.com/). 

The data is taken from the European Centre for Disease Prevention and Control. Use this [link](https://www.ecdc.europa.eu/en/covid-19/data) to get there. 

## Get a first glimpse at the data
You can also get a first impression of the data without using the WebApp. Clone the repository or just download the data folder and COVID-Analysis.ipynb. This jupyter notebook gives you a first overview over the data with some simple visualizations. If you don't know how to use jupyter notebook check out their website [here](https://jupyter.org/).

## How to use the WebApp manually
Clone the repo on the main branch, open the terminal and go to the corona-dashboard folder and type `python corona_dashboard.py`. This will show several lines in the terminal. 
One of these lines will say something like: *Running on http://0.0.0.0:3001/ (Press CTRL+C to quit)*.
Click on the http adress or copy it into to you web browser to get the WebApp.

## Necessary python packages

* flask
* plotly
* pandas
