month = int(input("Enter the month number: "))
if month in [1,3,5,7,8,10,12]:
    days = 31
elif month == 2:
    days = 28
else:
    days = 30
print(month,":",days)