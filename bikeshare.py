import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

Months=['january','february','march','april','may','june']
    
Days=['sunday','monday','tuesday','wednesday','thursday','friday','saturday']

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
    x=input("please enter valid city:chicago,washington,new york city")
    while(x.lower() not in CITY_DATA):
        x=input("WRONG!!!!please enter valid city:chicago,washington,new york city")
    city=x.lower()
    # TO DO: get user input for month (all, january, february, ... , june)
    
   
    x=input("please enter valid month:january,february,march,april,may,june OR enter all for no month filter")
    while((x.lower()!="all") and (x.lower() not in Months)):
        x=input("WRONG!!!please enter valid month:january,february,march,april,may,june OR enter all for no month filter")
    month=x.lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
   
    x=input("please enter valid day:sunday,monday,tuesday,wednesday,thursday,friday,saturday OR enter all for no day filter")
    while((x.lower()!="all") and (x.lower() not in Days)):
        x=input("WRONG!!!please enter valid day:sunday,monday,tuesday,wednesday,thursday,friday,saturday OR enter all for no day filter")
    day=x.lower()

    print('-'*40)
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
    df = pd.read_csv(CITY_DATA.get(city))
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['Month']=df['Start Time'].dt.month
    for i in range(6):
            if Months[i]==month:
                month=i
                break
    df['Day']=df['Start Time'].dt.weekday
    for j in range(7):
            if Days[j]==day:
                day=j
                break
    if(month!="all" and day!="all"):
        return(df.loc[df['Day']==j-1].loc[df['Month']==i+1])
    elif(month!="all" and day=="all"):   
        return(df.loc[df['Month']==i+1])
    elif(day!="all" and month=="all"):        
        return(df.loc[df['Day']==j-1])
    else:
        return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # TO DO: display the most common month
    #print("Most Common Month")
    #x=df.mode()[0]
    #return(Months[x-1])


    # TO DO: display the most common day of week

    #print("Most Common Day")
    #x=df.mode()[0]
    #return(Days[x])
    # TO DO: display the most common start hour
    
    print("Most Popular Hour")
    print(df['Start Time'].dt.hour.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("Most popular Start Station")
    print(df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print("Most popular End Station")
    print(df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    print("Most Frequent Trip")
    print(df.groupby(['Start Station','End Station']).size().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print(df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print(df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("User Type Count")
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if 'Gender' in df:
        print("Gender Count")
        print(df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print("Most Common Year")
        print(df['Birth Year'].mode()[0])
        print("Most Earliest Year")
        print(df['Birth Year'].min())
        print("Most Recent Year")
        print(df['Birth Year'].max())
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    reply=input("do you want to see user data")
    i=0
    while(reply.lower()=="yes"):
        print(df.iloc[i:i+5])
        reply=input("do you want to see more user data")
        if(reply.lower()=="yes"):
            i=i+5
        else:
            break
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        #print(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        #giving user the option to restart
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()