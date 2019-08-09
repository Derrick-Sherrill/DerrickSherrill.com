import pandas as pd

excel_file = 'Docs/contacts1.xlsx'
df = pd.read_excel(excel_file)
print(df)

print(df.loc[:,'Name'])
print(df.iloc[:,0])

print(df[df['Title'] =='Engineer'])

excel_file_2 = 'Docs/contacts2.xlsx'
df2 = pd.read_excel(excel_file_2)

df3 = pd.concat([df, df2], axis=0)
print(df3)

total_count = df3.groupby(['Title']).count()
print(total_count['Name'])
