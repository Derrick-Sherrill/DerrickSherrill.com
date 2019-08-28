import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

excel_file_1 = 'shift-data.xlsx'
excel_file_2 = 'third-shift-data.xlsx'

df_first_shift = pd.read_excel(excel_file_1, sheet_name='first')
df_second_shift = pd.read_excel(excel_file_1, sheet_name='second')
df_third_shift = pd.read_excel(excel_file_2)

print(df_first_shift)
print(df_first_shift['Product'])

df_all = pd.concat([df_first_shift, df_second_shift, df_third_shift])
print(df_all)

pivot = df_all.groupby(['Shift']).mean()
shift_productivity = pivot.loc[:,"Production Run Time (Min)":"Products Produced (Units)"]

print(shift_productivity)

#shift_productivity.plot(kind='bar')
#plt.show()

df_all.to_excel("output.xlsx")
