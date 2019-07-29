import pandas as pd

# denote spreadsheets
excel_file_1 = 'Workbook_1.xlsx'
excel_file_2 = 'Workbook_2.xlsx'

#read in spreadsheets
df1 = pd.read_excel(excel_file_1)
df2 = pd.read_excel(excel_file_2)

#print columns
print(df1.columns)
print(df2.columns)

# Filter by conditions

print((df1['Name'].isin(df2['Name'])))

filtered_frame_1 = df1.loc[(df1['Name'].isin(df2['Name']))] # Based on another sheet

filtered_frame_2 = df1.loc[~(df1['Name'].isin(df2['Name']))] # Inverse

filtered_frame_3 = df1.loc[(df1['Name'].isin(df2['Name'])) & (df1['Interview Score'] > 4) | (df1['YR Experience'] > 3)] # Multiple Filters

all_frames = [df1, df2]
all_df = pd.merge(df1, df2, on='Name')
print(all_df)

filtered_frame_4 = all_df.loc[(all_df['YR Experience'] < 5) & (all_df['Group Interview Score'] > 4)]
print(filtered_frame_4)
