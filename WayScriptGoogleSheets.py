import pandas as pd

product = inputs['Product']
amount = inputs['Amount']

amount = [int(a) for a in amount]

data = {'product':product, 'amount':amount}
df = pd.DataFrame(data)

a_total = df.loc[df['product']=='A']['amount'].sum()
print(a_total)

outputs['a_total'] = a_total
