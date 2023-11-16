number = int(input("Enter the number: "))
for i in range(2,(number//2)+1):
    if number % i == 0:
        print(number, "is not a prime")
        break
else:
    print(number, "is a prime")

