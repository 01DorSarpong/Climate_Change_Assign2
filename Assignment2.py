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
    
    
    df2 = df1.T
    
    return df1, df2

df1, df2 = read_data('Climate_Data.csv')


# Defining variables for my plots
years = df2.index
countries = ['Ghana', 'Nigeria', 'Algeria', 'Canada', 'US','Brazil',
             'Argentina', 'India', 'China', 'Kazakhstan','Australia',
             'Russia', 'UK',]


# Creating dataframes for all the 6 series
pop = df2.xs('Population, total', level=1, axis = 1)
CO2 = df2.xs('CO2 emissions (kt)', level=1, axis = 1)
gdp = df2.xs('GDP (current US$)', level=1, axis = 1)
forest = df2.xs('Forest area (% of land area)', level=1, axis = 1)
water = df2.xs('Annual freshwater withdrawals, total (% of internal resources)',
             level=1, axis = 1)
renewable_egy = df2.xs('Renewable energy consumption (% of total final energy consumption)',
             level=1, axis = 1)



"""
This part of the code plots different graphs to show the relationships between
the different series and countries over the years. The first graph is a bar
plot of the population series for all the countries over every 2 years

"""


# Bar graph of population for all countries
pop.T.iloc[:,1::2].plot(kind='bar', figsize=(15,15), width=0.8)

plt.xlabel('Countries')
plt.ylabel('Population')
plt.title('Total population of countries over the years')

plt.legend()


#Bar graph of annual freshwater withdrawals per country 
water.T.iloc[:,1::2].plot(kind='bar', figsize=(15,15), width=0.8)

plt.xlabel('Countries')
plt.ylabel('Total fresh water withdrawals')
plt.title('Totalfresh water withdrawals of countries over the years')

plt.legend()


#Line graph showing CO2 emmissions for countries over the years
CO2.iloc[::].plot(kind='line', figsize=(15,15), linestyle=':', linewidth=4)
plt.xlabel('Years')
plt.ylabel('CO2 Emissions (kt)')
plt.title(' CO2 Emissions over the years per Country')

plt.legend(fontsize='large')
plt.show()


#Line graph showing GDP for all countries over the years
gdp.iloc[::].plot(kind='line', figsize=(15,15), linestyle=':', linewidth=4)
plt.xlabel('Years')
plt.ylabel('GDP (current US$)')
plt.title(' GDP (US$) of all countries over the years')

plt.legend(fontsize='large')
plt.show()


"""
Find the correlation of selected indicators for countries or regions
"""


Ghana = df2.xs('Ghana', level=0, axis=1)
Nigeria = df2.xs('Nigeria', level=0, axis=1)
Algeria = df2.xs('Algeria', level=0, axis=1)

Africa = [Ghana, Nigeria, Algeria]

Canada = df2.xs('Canada', level=0, axis=1)
Brazil = df2.xs('Brazil', level=0, axis=1)
Argentina = df2.xs('Argentina', level=0, axis=1)
US = df2.xs('United States', level=0, axis=1)

Americas = [US, Brazil, Argentina, Canada]

Uk = df2.xs('United Kingdom', level=0, axis=1)
Australia = df2.xs('Australia', level=0, axis=1)
Russia = df2.xs('Russia', level=0, axis=1)

Europe = [Uk, Brazil, Argentina, Canada]

China = df2.xs('China', level=0, axis=1)
India = df2.xs('India', level=0, axis=1)
Kazakhstan = df2.xs('Kazakhstan', level=0, axis=1)
 
Asia = [China, India, Kazakhstan]





# Using statistical methods to explore the data
print(st.kurtosis(Africa_arr))
print(st.skew(Africa_arr))
print(Ghana.describe())
print(pop.apply(skew))






data_correlatioin = df2.corr() 
#check correlation for indi for each country
print(data_correlatioin)








