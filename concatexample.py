import pandas as pd

# concat series

python_series_a = pd.Series([1,2,3,4,5], name="Python Series 1", index=[1,2,3,4,5])
python_series_b = pd.Series([6,7,8,9,10], name='Python Series 2', index=[4,5,6,7,8])

new_df_from_two_series = pd.concat([python_series_a, python_series_b], axis=0)
print(new_df_from_two_series)

new_df_from_two_series_2 = pd.concat([python_series_a, python_series_b], axis=1)
print(new_df_from_two_series_2)

excel_df = pd.read_excel('wb.xlsx')
print(excel_df)

new_df_from_two_dfs = pd.concat([excel_df, new_df_from_two_series_2], axis=1, keys=["a","b"])
print(new_df_from_two_dfs)

print(new_df_from_two_dfs['a'])
