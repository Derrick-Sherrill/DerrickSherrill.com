import pandas as pd

excel_file = 'M_Index.xlsx'
df = pd.read_excel(excel_file)
print(df)

df1 = df.set_index(['Stock','Month'])
print(df1)

print(df1.loc["WM"])
print(df1.loc[("MSFT","Jan")])

print(df1.loc[pd.IndexSlice[:,"Jan"],:])
