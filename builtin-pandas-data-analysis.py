import pandas as pd

excel_file_path = 'electric_motor_data.csv'

df = pd.read_csv(excel_file_path)
print(df.columns)

df_info = df.info()
print(df_info)

print(df.describe()['i_d'])

grouped_df = df.groupby(['profile_id']).max()
print(grouped_df['torque'])

profile_id_4_df = df[df['profile_id'] == 4]
profile_id_4_df.to_excel('output.xlsx')
