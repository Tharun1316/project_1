a=['tharun','tharun',1,1,'hi','bye',5,'charan','teja',3,3]
b=[]
for i in range(len(a)):
    if a[i] not in b:
        b.append(a[i])
print(b)
for i in b:
    print(i,a.count(i))