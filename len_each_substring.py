str1 = "Python is good"
ls = list(str1.split(" "))
len_ls = []
for i in ls:
    len_ls.append(len(i))
print(len_ls)
# import pandas as pd
# db = pd.read_csv("5000 Sales Records.csv")
# #print(db.loc[db.Country.isin(["India", "Australia"])])
# #print(db.Country.describe())
# #print(db.describe())
# #print(db["Units Sold"].mean())
# #print(db.Country.sort_values().unique())
# #print(db.isnull().sum().sum())
# print(db.Country.value_counts())