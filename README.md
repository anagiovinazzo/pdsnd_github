# US Bikeshare Data Exploration with Python

## Project Overview
This project, which originated from Udacity's Programming for Data Science with Python course, makes use of Python code and the pandas library to explore user data for a bike share company in three major US cities: Chicago, New York City, and Washington. 

### Data Analyzed
* Most frequent times of travel (e.g. month, day of the week, hour of the day)
* Station usage metrics (e.g. most popular start and end stations)
* Trip duration statistics (e.g. length of total travel time, length of average travel time)
* User statistics (e.g. subscriber vs. customer, gender, birth year)

### Date Created and Date of Updates
* Project originally created and submitted on 5/4/2023.
* Project and README.md updated on 6/15/2023.

## Built With
* [Python 3.11.3](https://www.python.org/} - The programming language used to develop this project.
* [pandas](https://pandas.pydata.org/) - The main library used in this project to access information from .csv files.
* [time](https://docs.python.org/2/library/time.html) - A library used in this project to calculate processing time for each calculation.

## Files Used
* chicago.csv - The dataset containing bikeshare information for Chicago, as provided by Udacity.
* new_york_city.csv - The dataset containing bikeshare information for NYC, as provided by Udacity.
* washington.csv - The dataset containing bikeshare information for Washington, as provided by Udacity.

## Credits
* [Statology.org](https://www.statology.org/pandas-combine-two-columns/) - Used to double-check my work when writing code for combined start/end stations.
* [SparkByExamples.com](https://sparkbyexamples.com/pandas/get-first-n-rows-of-pandas/) - Used the i.loc[:n] method explained here and supplemented it with a While loop to allow the user to get lines of raw data.
* [StuffThatSpins.com](https://stuffthatspins.com/stuff/ASCII-Art-bicycle-bike-cycling.html) - Borrowed ASCII art of cyclists to create the separators in my code to make the program more visually interesting.
* [Marsja.se](https://www.marsja.se/pandas-count-occurrences-in-column-unique-values/) - Referenced this site to learn to use df['Column'].value_counts() to create the customer counts and gender counts for the user_stats(df) function. 
* [Pandas Documentation](http://pandas.pydata.org/pandas-docs/stable/)
* [Udacity](https://www.udacity.com/) - Programming for Data Science with Python course.
* [Dillinger](https://dillinger.io/) - For README formatting.

