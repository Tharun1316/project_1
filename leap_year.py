year = int(input("Enter the year: "))
if(year % 4 == 0):
    if( year % 400 == 0 or year % 100 != 0):
        print(year,"is leap year")
    else:
        print(year,"is not a leap year")
else:
    print(year,"is not a leap year")