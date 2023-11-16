str1 = input("Enter the string: ")
unique_str = ("")
for i in str1:
    if i not in unique_str:
        unique_str += i
print(unique_str)