month = input("Enter the month number: ")
    month = month.upper()
days = 0
# months = {"JAN":"JAN : 31","FEB":"FEB : 28","MAR":"MAR : 31","APR":"APR : 30","MAY":"MAY : 31","JUN":"JUN : 30","JUL":"JUL : 31","AUG":"AUG : 31","SEP":"SEP : 30","OCT":"OCT : 31","NOV":"NOV : 30","DEC":"DEC : 31"}
# print(months[month])
if month in ["JAN","MAR","MAY","JUL","AUG","OCT","DEC"]:
    days = 31
elif month == "FEB":
    days = 28
elif month in ["APR","JUN","SEP","NOV"]:
    days = 30
else:
    print("you enter wrong month")
print(month,":",days)