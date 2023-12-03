# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 13:52:05 2023

@author: dorot
"""

"""
This assignment is making use of statistical trends to analyse data 
 related to climate change. Countries selected was the top 10 largest 
 countries in the world and Ghana, Nigeria and the United Kingodm.The data will be
 expressed in 4 different graphs for the analysis.
"""


# Importing the libraries
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import stats as st
from scipy.stats import skew
from scipy.stats import kurtosis


def read_data(file):
    
    """
    This function takes in a file(csv) as a parameter and returns two 
    dataframes of the file one with columns as years and the other
    transposed with countries as years. 
    
    Parameter: 
        file: this is a CSV file read into the function
    """
    # Read the World Bank databank format file
    data = pd.read_csv(file, index_col = ['Country Name', 'Series Name'])
    print(data)
    
    
    df1 = data.drop(['Country Code', 'Series Code'], axis = 1)
    # df1 = pd.pivot_table(data, index=['Country Name','Series Name'], dropna=True)
   
    df1.rename(columns={'1991 [YR1991]': '1991', '1992 [YR1992]':'1992', 
    '1993 [YR1993]': '1993', '1994 [YR1994]':'1994', '1995 [YR1995]': '1995', 
    '1996 [YR1996]': '1996', '1997 [YR1997]':'1997', '1998 [YR1998]': '1998', 
    '1999 [YR1999]': '1999', '2000 [YR2000]':'2000'}, inplace = True)
    
    
    
    
               
   
    df1['1991'] = pd.to_numeric(df1['1991'], errors='coerce')
    df1['1992'] = pd.to_numeric(df1['1992'], errors='coerce')
    
    print(df1.dtypes)
    df2 = df1.T
    return df1, df2

df1, df2 = read_data('Climate_Data.csv')


# Renaming the rows to format as only years
#df2.rename(index={'1991 [YR1991]': '1991', 'Row2':'1992', '1991' [YR1991], '1991 [YR1991]': '1991', 'Row2':'1992', '1991' [YR1991]

print(df1.dtypes)



population = df2.xs('Population, total', level=1, axis = 1)
#print(population)

Ghana_data = df2.xs('Ghana', level=0, axis=1)
print(Ghana_data)


# Using statistical methods to explore the data

print(df2.describe())
print(df2.apply(skew))
print(df2.apply(kurtosis))


 


#annual_water = df2.xs('Population, total', level=1, axis = 1)
#print(annual_water)



"""
df2.set_index(['Algeria','Argentina', 'Australia', 'Brazil','Canada', 'China', 
               'India', 'Kazakhstan','Russia', 'United States', 'Nigeria', 'Ghana',
               'United Kingdom',df2.index ] , inplace=True)
"""






#df2.iloc[1].rename(columns={'CO2 emissions (kt)': 'CO2 Ems', 'GDP (current US$)': 'GDP', 
#                           'Annual freshwater withdrawals, total (% of internal resources)': 'Annual Freshwater',
#                           'Forest area (% of land area)': 'Forest Area', 
 #                          'Renewable energy consumption (% of total final energy consumption)': 'Ren Energy Cons',
 #                          'Population, total': 'Population'},
#                  inplace=True)


"""
    # Extracting the data and storing in the variable country_info
    country_info = data.iloc[1:-1]

    # Transposing the dataframe to have years as columns
    data_years = data.T.iloc[0:]

    # Setting the first row as the column headers
    data_years.columns = data_years.iloc[0]

    # Dropping the first row (which is now duplicated as column headers)
    data_years = data_years[1:]

    return country_info, data_years


# Calling the function read_data
file = 'Climate_Data.csv'  
country_info , data_years = read_data(file)



# Print or use the dataframes as needed
print("Country Information:")
print(country_info)

print("\nDataframe with Years as Columns:")
print(data_years)






"""
"""
#data_years['Series Name'].rename(columns={'CO2 emissions (kt)': 'CO2 Ems', 'GDP (current US$)': 'GDP', 
                           'Annual freshwater withdrawals, total (% of internal resources)': 'Annual Freshwater',
                           'Forest area (% of land area)': 'Forest Area', 
                           'Renewable energy consumption (% of total final energy consumption)': 'Ren Energy Cons',
                           'Population, total': 'Population'},
                  inplace=True)
"""




