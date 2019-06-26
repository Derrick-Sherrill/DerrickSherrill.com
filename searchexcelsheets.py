import pandas as pd
import numpy as np

initial_workbook = 'A.xlsx'
info_workbook = 'B.xlsx'
output_workbook = 'output.xlsx'

df_initial = pd.read_excel(initial_workbook)
df_info = pd.read_excel(info_workbook)

# print(df_initial.columns)
# print(df_info.columns)

df_initial.rename(columns={'Code':'IDs'}, inplace=True)

df_3 = pd.merge(df_initial, df_info[['IDs','ID']], on='IDs', how='left')
print(df_3)

df_3.rename(columns={'IDs':'Code'}, inplace=True)

df_3 = df_3.replace(np.nan, '', regex=True)
print(df_3)

df_3.to_excel(output_workbook, index=False)
