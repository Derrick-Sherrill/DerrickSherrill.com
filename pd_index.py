import numpy as np
import pandas as pd

excel_file = "Pandas_Workbook.xlsx"
df = pd.read_excel(excel_file)
print(df)

print(df.head(5))
print(df.tail(5))
print(df.index)
print(df.columns)
print(df.dtypes)

print(df['Name'])
print(type(df['Name']))

#names = df['Name']
#print(names[0])

#Label
print(df.at[0, "Name" ])
df2 = pd.read_excel(excel_file, index_col="Name")
print(df2)
print(df2.at["Beth","Occupation"])

print(df2.iat[1,1])

print(df.loc[[0,2,4,6], "Age":"Occupation"])
print(df.loc[df["Identifier"]==True])

print(df.iloc[0:5:1, [0,1]])
