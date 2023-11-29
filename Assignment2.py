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


def read_data(file):
    
    """
    This function takes in a file(csv) as a parameter and returns two 
    dataframes of the file one with columns as years and the other
    transposed with countries as years. 
    
    Parameter: 
        file: this is a CSV file read into the function
    """
    # Read the World Bank databank format file
    data = pd.read_csv(file)
    #print(data)
    
    df1 = pd.pivot_table(data, index=['Country Name','Series Name'], dropna=True)
    #print(df1)
    
    df2 = df1.T
    return df1, df2


df1, df2 = read_data('Climate_Data.csv')
print(df2)

plt.figure()


df2[:'Series Name'].rename(columns={'CO2 emissions (kt)': 'CO2 Ems', 'GDP (current US$)': 'GDP', 
                           'Annual freshwater withdrawals, total (% of internal resources)': 'Annual Freshwater',
                           'Forest area (% of land area)': 'Forest Area', 
                           'Renewable energy consumption (% of total final energy consumption)': 'Ren Energy Cons',
                           'Population, total': 'Population'},
                  inplace=True)
print(df2)

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



# Using statistical methods to explore the data

#print(country_info.describe())
#print(data_years.describe())



print(data_years.iloc[1])
 # Cleaning up the data to rename columns and headers


"""
"""
#data_years['Series Name'].rename(columns={'CO2 emissions (kt)': 'CO2 Ems', 'GDP (current US$)': 'GDP', 
                           'Annual freshwater withdrawals, total (% of internal resources)': 'Annual Freshwater',
                           'Forest area (% of land area)': 'Forest Area', 
                           'Renewable energy consumption (% of total final energy consumption)': 'Ren Energy Cons',
                           'Population, total': 'Population'},
                  inplace=True)
"""




