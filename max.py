number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
number_3 = int(input("Enter second number: "))
if (number_1 > number_2 and number_1 > number_3):
    print(number_1,"is max")
else:
    if(number_2 > number_3):
        print(number_2,"is max")
    else:
        print(number_3,"is max")
print(max(number_1,number_2,number_3),"is max")