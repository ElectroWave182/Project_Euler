from sys import stdin, stdout
input, print = stdin.readline, stdout.write


def main ():

    weekDay = 2
    sundays = 0
    months = [
        31, # January
        28, # February
        31, # March
        30, # April
        31, # May
        30, # June
        31, # July
        31, # August
        30, # September
        31, # October
        30, # November
        31  # December
    ]
    
    for year in range (1901, 2001):
    
        # Leap year?
        leap = year % 4 == 0
        leap = year % 100 != 0 and leap
        leap = year % 400 == 0 or leap
        
        for month in months:
        
            # First of the month sunday
            if weekDay == 0:
                sundays += 1
                
            # 29th of February
            if leap and month == 28:
                weekDay += 1
                
            weekDay = (weekDay + month) % 7
            
    print (str (sundays))


main ()