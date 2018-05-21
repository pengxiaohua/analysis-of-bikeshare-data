import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York': 'new_york_city.csv',
              'Washington': 'washington.csv' }

months = ['January', 'February', 'March', 'April', 'May', 'June']
week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                        'Would you like to see data for Chicago, New York, or Washington?\n')

            if city not in CITY_DATA:
                raise ValueError('\nERROR: Invalid city entered "{}". Only enter Chicago, New York or Washington.'.format(city))

            # TO DO: get user input for month (all, january, february, ... , june)
            month = input('\nWhich month? January, February, March, April, May, or June?\n')
            if month not in months and month != 'all':
                raise ValueError('\nERROR: Invalid month entered "{}". Only enter months from January to June or all'.format(month))

            # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
            day = input('\nWhich day? all, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday\n')
            if day not in week and day != 'all':
                raise ValueError('\nERROR: Invalid day entered "{}". Only enter week from Monday to Sunday or all'.format(month))

            print('-'*40)
            return city, month, day

        except ValueError as error:
            print(error)
        except KeyboardInterrupt:
            break


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
    city = city.title()
    month = month.title()
    day = day.title()
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'All':
        # use the index of the months list to get the corresponding int
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    elif month == 'All':
        df = df

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]

    elif day == 'All':
        df = df

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    months = ['January', 'February', 'March', 'April', 'May', 'June']

    # TO DO: display the most common month
    most_commom_month = df['month'].mode()[0]
    print("\nThe most common month is {}".format(months[most_commom_month - 1]))

    # # TO DO: display the most common day of week
    most_commom_week = df['day_of_week'].mode()[0]
    print("\nThe most common week is {}".format(most_commom_week))

    # # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_commom_start_hour = df['hour'].mode()[0]
    print("\nThe most common start hour is {}".format(most_commom_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_commomly_start_station = df['Start Station'].mode()[0]
    print("\nThe most commonly start hour is {}".format(most_commomly_start_station))

    # TO DO: display most commonly used end station
    most_commomly_end_station = df['End Station'].mode()[0]
    print("\nThe most commonly end hour is {}".format(most_commomly_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['Combined Station'] = df['Start Station'] + " - " + df['End Station']
    most_frequent_combination_station = df['Combined Station'].mode()[0]
    print("\nThe most most frequent combination of start station and end station trip is {}".format(most_frequent_combination_station))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('\nThe total travel time is {} seconds.'.format(round(total_travel_time, 2)))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('\nThe mean travel time is {} seconds.'.format(round(mean_travel_time, 2)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_of_user_types = df['User Type'].value_counts()
    print('\nThe counts of user types is:\n{}.\n'.format(counts_of_user_types))

    # TO DO: Display counts of gender
    try:
        counts_of_gender = df['Gender'].value_counts()
        print('\nThe counts of gender is:\n{}.\n'.format(counts_of_gender))
    except:
        print('Gender column does not exist!')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year_of_birth = df['Birth Year'].min()
        print('\nThe earliest year of birth is {}.'.format(earliest_year_of_birth))

        most_recent_year_of_birth = df['Birth Year'].max()
        print('\nThe most recent year of birth is {}.'.format(most_recent_year_of_birth))

        most_common_year_of_birth = df['Birth Year'].mode()[0]
        print('\nThe most common year of birth is {}.'.format(most_common_year_of_birth))
    except:
        print('Birth Year column does not exist!')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
