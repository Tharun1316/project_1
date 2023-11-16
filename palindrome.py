str1 = input("Enter the string: ").lower()
new_str = ''
for i in range(len(str1)-1,-1,-1):
    new_str += str1[i]
if(str1 == new_str):
    print(str1,"is a palindrome")
else:
    print(str1,"is not a palindrome")