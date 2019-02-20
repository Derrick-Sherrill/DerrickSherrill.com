##Requirements:
#Python
#matplotlib
#Pandas
###############

#Import Modules
import pandas
import matplotlib.pyplot as plt


# Script
ExcelWorkbook = "Workbook2.xlsx"
df = pandas.read_excel(ExcelWorkbook)

#Test to make sure data is loaded
print(df.head())

#Pull out columns for graph
#Unneccesary for final graph, but good indication if all your data is being read in.
values = df[['Locations','Profit']]
print(values)

# Bar Chart

ax = values.plot.bar(x='Locations', y='Profit', rot=0)
plt.show()
