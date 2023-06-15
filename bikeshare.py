import time
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

bike_art = """
      __o
     -\<,
.....O/ O
"""

bike_art_conclusion = """
                        \o/
  __o          __o       I
 `\<,         `\<,      `\\,
_O/ O_________O/_O______O/_O_
"""

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington).
    city_options = ['Chicago', 'New York City', 'Washington']
    month_options = ['January', 'February', 'March', 'April', 'May', 'June', 'All']
    day_options = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'All']
    
    city = ''
    while city not in city_options:
        city = input("Select a city: Chicago, New York City, or Washington:\n").title()
        if city in city_options:
            print('You have selected {}.'.format(city))
        else:
            print('Sorry, please select a valid city.')

    # get user input for month (all, january, february, ... , june)
    month = ''
    while month not in month_options:
        month = input("Select a month: January, February, March, April, May, June, or All:\n").title()
        if month in month_options:
            print('You have selected {}.'.format(month))
        else:
            print('Sorry, please select a valid month.')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = ''
    while day not in day_options:
        day = input("Select a day of the week: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or All:\n").title()
        if day in day_options:
            print('You have selected {}.'.format(day))
        else:
            print('Sorry, please select a valid day of the week.')

    print(bike_art)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # convert city selection to the proper case and format to match the .csv filename.
    filename = city.lower().replace(' ', '_')+'.csv'
    
    # load data file into a dataframe
    df = pd.read_csv(filename)
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month, day of week, and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'All':
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1
        
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df
    print(df)

def convert_twelve_hr(popular_hour):
    """
    Takes an hour in 24-hour time (e.g. 17) and converts it to 12-hour time and reflect a.m./p.m. (e.g. 5 p.m.)
    Conditional statements are included to handle unusual cases, like midnight and noon.
    """
    if popular_hour == 0:
        twelve_hour_time = str(popular_hour + 12) + ' a.m.'
    elif popular_hour == 12:
        twelve_hour_time = str(popular_hour) + ' p.m.'
    elif popular_hour > 12:
        twelve_hour_time = str(popular_hour - 12) + ' p.m.'
    else:
        twelve_hour_time = str(popular_hour) + ' a.m.'
    return twelve_hour_time
        

def time_stats(df):
    """
    Displays statistics on the most frequent times of travel.
    
    Conditional statements are used to change the phrasing of each line depending on prior selections.
    If the user has made a selection (e.g. user has chosen Tuesday), the wording reflects the user's choice rather than stating that Tuesday is the most popular day.
    This action is performed by checking whether the dataframe contains one or more unique elements.
    If the user has chosen All, then the wording will change to state the most popular month and day.
    """

    start_time = time.time()

    # display the most common month or display the month the user selected.
    popular_month = df['month'].mode()[0]
    if df['month'].nunique() > 1:
        print('The most common month of travel is {},'.format(popular_month))
    else:
        print('For the month you selected, {},'.format(popular_month))

    # display the most common day of the week or display the day of the week the user selected. change the phrasing depending on previous selections.
    popular_day = df['day_of_week'].mode()[0]
    if df['day_of_week'].nunique() > 1 and df['month'].nunique() > 1:
        print('the most common day of travel is {},'.format(popular_day))
    elif df['day_of_week'].nunique() == 1 and df['month'].nunique() > 1:
        print('and for the day you selected, {},'.format(popular_day))
    elif df['day_of_week'].nunique() > 1 and df['month'].nunique() == 1:
        print('the most common day of travel is {},'.format(popular_day))
    else:
        print('and for the day you selected, {},'.format(popular_day))

    #display the most common start hour and convert to 12-hour time using convert_twelve_hr(popular_hour). change the phrasing depending on previous selections.
    popular_hour = df['hour'].mode()[0]
    twelve_hour_time = convert_twelve_hr(popular_hour)
    if df['day_of_week'].nunique() == 1 and df['month'].nunique() > 1:
        print('the most common start hour is {}'.format(twelve_hour_time))
    elif df['day_of_week'].nunique() == 1 and df['month'].nunique() == 1:
        print('the most common start hour is {}'.format(twelve_hour_time))
    else:
        print('and the most common start hour is {}'.format(twelve_hour_time))
        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print(bike_art)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('The most popular start station is {}.'.format(popular_start_station))

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('The most popular end station is {}.'.format(popular_end_station))

    # display most frequent combination of start station and end station trip
    start_end = 'a starting station of ' + df['Start Station'] + ' and an ending station of ' + df['End Station']
    popular_start_end = start_end.mode()[0]
    print('The most frequent start/end station combination is {}.'.format(popular_start_end))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print(bike_art)

def convert_seconds(total_seconds):
    """Converts seconds to hours, minutes, and seconds."""
    travel_hours = total_seconds // 3600
    remaining_seconds = total_seconds % 3600
    travel_minutes = remaining_seconds // 60
    travel_seconds = int(remaining_seconds % 60)
    return travel_hours, travel_minutes, travel_seconds

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    start_time = time.time()

    # display total travel time in hours, minutes, seconds
    total_seconds = sum(df['Trip Duration'])
    travel_hours, travel_minutes, travel_seconds = convert_seconds(total_seconds)
    print('The total travel time in your selected span for your selected city is {} hours, {} minutes, and {} seconds.'.format(travel_hours, travel_minutes, travel_seconds))

    # display mean travel time in hours, minutes, seconds
    total_seconds = df['Trip Duration'].mean()
    travel_hours, travel_minutes, travel_seconds = convert_seconds(total_seconds)
    print('The average trip duration is {} hours, {} minutes, and {} seconds.'.format(travel_hours, travel_minutes, travel_seconds))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print(bike_art)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    start_time = time.time()

    print('\nLet\'s take a look at the number of subscribers vs. customers:\n')
    # Display counts of user types
    try:
        customer_count = df['User Type'].value_counts()
        print(customer_count)
    except KeyError:
        print('Sorry, this data is unavailable for your current selection.')
        

    # Display counts of gender
    print('\nHere\'s the breakdown of users by gender for your selected period overall:\n')
    try:
        male_count = (df.Gender.values == 'Male').sum()
        female_count = (df.Gender.values == 'Female').sum()
        print ('There are {} male users and {} female users for your selected period.'.format(male_count, female_count))
    except KeyError:
        print('Sorry, this data is unavailable for your current selection.')

    # Display earliest, most recent, and most common year of birth
    print('\nFinally, let\'s look at some birth year stats:\n')
    try:
        popular_birth_year = int(df['Birth Year'].mode()[0])
        min_birth_year = int(df['Birth Year'].min())
        max_birth_year = int(df['Birth Year'].max())
        print('The earliest user birth year is {}.'.format(min_birth_year))
        print('The most recent user birth year is {}.'.format(max_birth_year))
        print('The most common user birth year is {}.'.format(popular_birth_year))
    except KeyError:
        print('Sorry, this data is unavailable for your current selection.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print(bike_art)

def get_raw_data(df):
    """get the first 5 rows of raw data"""
    pd.set_option('display.max_columns',200)
    x = 0
    y = 5
    ask_data = 'Would you like to see the first five rows of data for your selections? Select Yes or No.\n'
    raw_data_choice = ''
    while raw_data_choice != 'No':
        raw_data_choice = input(ask_data).title()
        if raw_data_choice == 'Yes':
            print(df.iloc[x:y])
            x += 5
            y += 5
            ask_data = 'Would you like to see the next five rows of data for your selections? Select Yes or No.\n'
        elif raw_data_choice == 'No':
            print('Okay, let\'s move on.')
        else:
            print('Sorry, that\'s not a valid response.')
            
            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        binary_options = ['Yes', 'No']
        
        run_time_stats = ''
        try:
            while run_time_stats not in binary_options:
                run_time_stats = input('Would you like to see usage time statistics? Select Yes or No.\n').title()
                if run_time_stats == 'Yes':
                    print('Great! Here are some usage time statistics.')
                    time_stats(df)
                elif run_time_stats == 'No':
                    print('Okay, let\'s move on.')
                else:
                    print('Sorry, that\'s not a valid response.')
        except KeyError:
            print('Sorry, this data is unavailable for your current selection.')
        
        station_metrics = ''
        try:
            while station_metrics not in binary_options:
                station_metrics = input('Would you like to see station usage metrics? Select Yes or No.\n').title()
                if station_metrics == 'Yes':
                    print('Excellent! Here are some station usage metrics.')
                    station_stats(df)
                elif station_metrics == 'No':
                    print('Okay, let\'s move on.')
                else:
                    print('Sorry, that\'s not a valid response.')
        except KeyError:
            print('Sorry, this data is unavailable for your current selection.')
        
        duration_metrics = ''
        try:
            while duration_metrics not in binary_options:
                duration_metrics = input('Would you like to see trip duration statistics? Select Yes or No.\n').title()
                if duration_metrics == 'Yes':
                    print('\nExcellent! Here are some trip duration metrics.')
                    trip_duration_stats(df)
                elif duration_metrics == 'No':
                    print('Okay, let\'s move on.')
                else:
                    print('Sorry, that\'s not a valid response.')
        except KeyError:
            print('Sorry, this data is unavailable for your current selection.')
            
        user_metrics = ''
        while user_metrics not in binary_options:
            user_metrics = input('Would you like to see user statistics? Select Yes or No.\n').title()
            if user_metrics == 'Yes':
                print('\nExcellent! Here are some user stats.')
                user_stats(df)
            elif user_metrics == 'No':
                print('Okay, let\'s move on.')
            else:
                print('Sorry, that\'s not a valid response.')

        get_raw_data(df)

        print('\nThanks for investigating US bikeshare data! That\'s all we have for right now.\n')
        print(bike_art_conclusion)
        restart = input('\nWould you like to restart? Enter Yes or No.\n')
        if restart.title() != 'Yes' and restart.title() != 'Y':
            break


if __name__ == "__main__":
	main()
