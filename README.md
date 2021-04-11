# corona-dashboard
Analysis of COVID-19 data with visualizations that are shown in a WebApp. The app is deployed using [heroku](https://www.heroku.com/).

## heroku-deployment branch
This branch contains the structure that is required by heroku. Most files are the same as on the main branch. 
See the added files needed for heroku deployment in the following section.

## Additional files on this branch
* [Procfile](./Procfile): Name of web app defined and called using the python package gunicorn
* [requirements.txt](./requirements.txt): All installed python packages and their version numbers

## Additional python packages on this branch
* gunicorn: Unix server package needed for app deployment
Find all installed packages [here](./requirements.txt).
