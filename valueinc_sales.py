#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  1 15:01:32 2025

@author: Bronze
"""

import pandas as pd

data = pd.read_csv('transaction.csv')

data = pd.read_csv('transaction.csv', sep=';' )


#summary of the data 
data.info()


# Cost Per Transaction

data['CostPerTransaction'] = data['NumberOfItemsPurchased'] * data['CostPerItem']

# Sales Per Transaction

data['SalesPerTransaction'] = data['NumberOfItemsPurchased'] * data['SellingPricePerItem']

# Profit Per Transaction

data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

# Mark up 

data['Markup'] = data['ProfitPerTransaction']/data['CostPerTransaction']


# Using Round function to Round Mark up to two decimal places
roundmarkup = round(data['Markup'],2)
 
data['Markup'] = round(data['Markup'],2)
 
 
 
 
 # Combining data fields
 
day = data['Day'].astype(str)
print(day.dtype)
 
year = data['Year'].astype(str)
print(year.dtype)
 
my_date = day+'-'+ data['Month']+'-' + year
 
data['date'] = my_date
 
 
#using iloc to view specific columns/rows
 
data.iloc[0] # views the row with index = 0

data.iloc[0:3]
 
data.head(5) # First 5 rows

data.iloc[:,2]
 
 
 
# Splitting data in Client Keywords field

#new_var = column.str.split('sep', expand = True)

split_col = data['ClientKeywords'].str.split(',', expand = True)

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthOfContract'] = split_col[2]
 
 
# Replace function

data['ClientAge'] = data['ClientAge'].str.replace('[', '')
 
data['LengthOfContract'] = data['LengthOfContract'].str.replace(']', '')
 
 
#Using the lower function to change item description
 
data['ItemDescription'] = data['ItemDescription'].str.lower()
 
 
 
 # Merging Datasets
 
seasons = pd.read_csv('value_inc_seasons.csv', sep =';')

# Merging Datasets
# merge_df = pd.merge(df_old, df_new, on = 'key')

data = pd.merge (data, seasons, on = 'Month' )
 

# Drop Columns

# df = df.drop ('column', axis = 1 )


data = data.drop('ClientKeywords', axis = 1)

data = data.drop('Day', axis = 1)

data = data.drop(['Year', 'Month'], axis = 1)


# Export Final CSV

data.to_csv('ValueInc_Cleaned.csv', index = False)











