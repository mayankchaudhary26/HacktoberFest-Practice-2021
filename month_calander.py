
month = int(input("give the month: "))
year = int(input("give the year: "))

days_passed = 0

def findLeap(year):                       # function to check leap year

    if(year % 400 == 0): 
        return 1

    if(year % 4 == 0 and year%100 != 0): 
        return 1

    return 0

def daysInMonth(month, year):                                 # function to find days in current month

    if(month == 2 and findLeap(year)): 
        return 29 
    elif(month == 2): 
        return 28 
    elif(month == 4 or month== 6 or month== 9 or month== 11): 
        return 30 
    else: 
        return 31  


for current_year in range(1900, year+1):               # calculate the total days passed 

    if(current_year < year):

        if(findLeap(current_year)): 
            days_passed += 366
        else: 
            days_passed += 365 

    else : 

        for current_month in range(1, month + 1): 

            if(current_month < month): 
                days_passed += daysInMonth(current_month, current_year) 


week_day = days_passed % 7              # get the week day

print("\n     Calander     ")

print("M  T  W  T  F  S  S")

# print("\n--------------------")

print("   " * (week_day), end= "")

for i in range(1, daysInMonth(month, year) + 1): 

    if(i < 10): 
        print("0", end="") 

    if((i + week_day) % 7 == 0):
        print(i)

    else: 
        print(i, end =" ")

