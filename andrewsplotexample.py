import pandas as pd
from pandas.plotting import andrews_curves
import matplotlib.pyplot as plt

excel_file = 'CableLog.xlsx'
df = pd.read_excel(excel_file)
print(df)

plt.figure()
andrews_curves(df, 'Quality Test')

plt.show()
