import pandas as pd

df = pd.read_excel('OrderHistory.xlsx')
df = df.sort_values(by='Order ID', ascending=True)
print(df.head(10))

agg_functions = {
'Sales Amount'  : 'sum',
'Order Type'    : ', '.join,
}

simplified_df = df.groupby('Order ID').agg(agg_functions)
simplified_df.to_excel('simplified_order_history.xlsx')

multiple_item_orders = simplified_df[simplified_df['Order Type'].str.contains(',')]
print(multiple_item_orders)
