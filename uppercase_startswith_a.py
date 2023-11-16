ls = ["apple","banana","airport"]
new_ls = []
for i in range(len(ls)):
    if ls[i][0] == "a":
        new_ls.append(str.upper(ls[i]))
print(new_ls)