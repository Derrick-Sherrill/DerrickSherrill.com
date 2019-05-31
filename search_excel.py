import numpy as np
import pandas as pd

excel_file = 'Pandas_Workbook.xlsx'
df = pd.read_excel(excel_file)
print(df)

print(df['Name'].where(df['Occupation'] == 'Programmer'))
programmers = df['Name'].where(df['Occupation'] == 'Programmer')
print(programmers.dropna())

excel_files = ['Pandas_Workbook.xlsx','Pandas_Workbook_copy.xlsx','Pandas_Workbook_copy_2.xlsx']

for individual_excel_file in excel_files:
    df = pd.read_excel(individual_excel_file)
    programmers = df['Name'].where(df['Occupation'] == 'Programmer').dropna()
    print("File Name" + individual_excel_file)
    print(programmers)
