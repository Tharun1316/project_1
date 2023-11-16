number = int(input("enter number: "))
for i in range(number):
    for j in range(i+1):
            print("*",end="")
    print("")
    # while i == number-2:
    #     for i in range(number,0,-1):
    #         for j in range(i,0,-1):
    #             print("*",end="")
    #         print("")
    #     i=i+1