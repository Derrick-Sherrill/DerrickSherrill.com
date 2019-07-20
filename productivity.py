import pandas as pd

excel_file = 'Workbook1.xlsx'

df_1 = pd.read_excel(excel_file)
df_2 = pd.read_excel(excel_file, sheet_name='2nd')

print(df_1.head(5))
print(df_2.head(5))

frames = [df_1, df_2]
all_data_df = pd.concat(frames, axis=0)
print(all_data_df)

productivity_df = all_data_df.groupby(['Operator','Line #']).mean() #.min() .max() . sum()
print(productivity_df['Amount'])
