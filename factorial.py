import math
number = int(input("Enter number: "))
#print(math.factorial(number))
i=0
fact=1
while i<number:
    fact=fact*(number-i)
    i=i+1
print(fact)