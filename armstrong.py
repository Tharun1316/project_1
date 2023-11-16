number = int(input("Enter number: "))
lnum = len(str(number))
arm_sum = 0
temp = number
while temp > 0:
    rem = temp % 10
    arm_sum = arm_sum + rem ** lnum
    temp = temp // 10
if number == arm_sum:
    print(number,"is armstrong number")
else:
    print(number,"is not armstrong number")


