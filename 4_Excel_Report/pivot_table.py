import pandas as pd

df = pd.read_excel('supermarket_sales.xlsx')

# for 1 column we use  []  but for 2 or more columns we use [[]]
df2 = df[['Gender','Product line', 'Total']]

# create a pivot table
# https://datascientyst.com/list-aggregation-functions-aggfunc-groupby-pandas/
df.pivot_table(index='Gender',columns= 'Product line', values='Total', aggfunc='sum')

"""
index = rows
columns
values = this will be the values that we display inside
"""
print(df2)