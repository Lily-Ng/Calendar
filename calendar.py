'''
This program prints calendar for one entire year based on what day of the week January 1st of that year is
where 1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, 7 = Sunday
'''

# by Lily Ng
# The list below will be used as a reference for the month heading
months= ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
def print_month_cal(days, start):   #Part a
    days_passed= 0
    print("Mo\tTu\tWe\tTh\tFr\tSa\tSu") #print heading
    print("\t"*(start-1), end="")   #indent start-1 times because it starts w/ Monday
    while days_passed<days:
        days_passed+=1
        if (days_passed+start)%7-1==1:
            print("\n", end="")  
        print(str(days_passed)+"\t", end="")    #print out date in a formated way
    print("\n")
    if ((days_passed+start)%7==0):
        return 7    #7 represents Sunday, and it is a special case
    else:
        return (days_passed+start)%7  #return the day it ends at
    
def is_leap_year(year): #Part b
    if (year%4==0 and year%100!=0) or (year%4==0 and year%400==0):
        return True
    else:
        return False
    
def print_calendar(year, start):   #Part c
    for month in range(1,13):
        print("\t\t    ",months[month-1])   #use the global "month" list to determine the month based on a number
        if month==2:    #for february, check if the year is a leap year
            if is_leap_year(year)==True:
                start=print_month_cal(29,start) #February has 29 days during leap years
            else:
                start=print_month_cal(28,start) #update start with where each month ends
        elif month==1 or month ==3 or month==5 or month==7 or month==8 or month==10 or month==12:
            start=print_month_cal(31,start)
        else:
            start=print_month_cal(30,start)
def main(): #Part d:driver program
    year= int(input("Enter the current year: "))    #get all the necessary information from the user
    day_start= int(input("Enter the day of the week of 1/1: "))
    print_calendar(year, day_start) #call function to print calendar
main()
