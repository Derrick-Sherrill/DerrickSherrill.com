import numpy as np
import pandas as pd


"""The Script"""
#DataFrame Creation
excel_file = 'Pandas_Workbook.xlsx'
df = pd.read_excel(excel_file)
print(df)
# Python Automatically created index column for us

# Pull Information out of DataFrame

print(df.head(5))
print(df.tail(5))
print(df.index)
print(df.columns)
print(df.dtypes)

#Indexing and Selecting DataFrame
#columns (Series)
print(df['Name']) #Note this is a series
print(type(df['Name']))

print(df[['Name','Occupation']]) #This pulls two series together = dataframe
print(type(df[['Name','Occupation']]))

#Incorrect way but works
print(df['Occupation'][0]) #Chain indexing

#Better versions of the above - LABEL Indexing
print(df.at[0, 'Occupation']) #Pull single value avoiding single value avoiding chained indexed

"""Here the row labels are index positions""" #Changing row labels
df2 = pd.read_excel(excel_file, index_col='Name') #Changing index to non integer labels -- UNIQUE VALUES RECOMMENDED ON DF INDEX
print(df2)
# Label based indexing
print(df2.at["Adam", "Occupation"])

#integer based indexing
print(df2.iat[2,1]) # even no columns are numbers, we can still index off positions


print(df.loc[:,['Name']])  # pull single column
print(df.loc[:,['Name','Occupation']]) #Pull multiple columns

# Rows or columns from labels
print(df.loc[1,:])

#Pull data with slices
print(df.loc[0:5,'Name':'Occupation'])

#Booleans
#Entire operation
print(df.loc[df['Identifier']==True])

#Create boolean series
print(df['Age']>27)
print(df.loc[df['Age']>27])


print(df.loc[0:5,[True,True,True,False]])


# Integer location based
#Single values
print(df.iloc[1,1])
#Lists
print(df.iloc[[1,2,3,4],[1,2]])
#slices of above
print(df.iloc[1:5:1,1:3:1])
