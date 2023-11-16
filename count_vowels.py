str1 = input("Enter the string: ")
count = 0
for i in str1:
    if i in ['a','e','i','o','u']:
        count += 1
print("count of vowels : ",count)