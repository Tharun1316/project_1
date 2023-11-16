str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
slist1 = list(str1)
slist1.sort()
slist2 = list(str2)
slist2.sort()
if slist1 == slist2:
    print("Given strings are anagram")
else:
    print("Given strings are not anagram")
