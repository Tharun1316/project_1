number = int(input("Enter the number: "))
a = 0
b = 1
print(a,b,end=" ")
while number != 0:
    c = a + b
    print(c,end=" ")
    a = b
    b = c
    number -= 1

