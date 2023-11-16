list1 = [23, 1, 28, 90, 99]
list2 = [23, 76, 34, 27, 99, 13]
li = []
for i in list1:
    for j in list2:
        if i == j:
            li.append(i)
print(li)