from datetime import datetime

def age_diff(given_date):
    #transform user input year
    x=datetime.strptime(given_date, "%d-%m-%Y")

    #create a datetime object for today
    today=datetime.today()

    #diff in years
    age=today.year - x.year

    #adjusting if month and day hasn't happened yet
    if (today.month<x.month) and (today.day<x.month):
        age-=1
    
    return(age)


print('Enter date below as day-month-year for example 02-09-2002')
given_date=input()
age_diff=age_diff(given_date)
print(f"there are {age_diff} years between {given_date} and now")