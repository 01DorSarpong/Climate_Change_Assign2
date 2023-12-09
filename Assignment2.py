# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 13:52:05 2023

@author: dorot
"""

"""
This assignment is making use of statistical trends to analyse data 
 related to climate change. Countries selected for the analyst were the top
 10 largest countries and in addittion Ghana, Nigeria and the United Kingodm.
 The data will be expressed in 4 different graphs for the analysis.
"""


# Importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import stats as st
import seaborn as sns


def read_data(file):
    
    """
    This function takes in a csv file as a parameter and returns two
     dataframes, one with columns as years and the other transposed with 
     countries as years. 
    
    Parameter: 
        file: this is a CSV file read into the function
    """
   
    #Reading the CSV file and setting index as country name and series name
    data = pd.read_csv(file, index_col = ['Country Name', 'Series Name'])
    
    #Removing the country code and series in the data and storing in dataframe1
    df1 = data.drop(['Country Code', 'Series Code'], axis = 1)
  
    #Renaming the columns to remove years in [] 
    df1.rename(columns = {'1991 [YR1991]': '1991', '1992 [YR1992]':'1992', 
    '1993 [YR1993]': '1993', '1994 [YR1994]':'1994', '1995 [YR1995]': '1995', 
    '1996 [YR1996]': '1996', '1997 [YR1997]':'1997', '1998 [YR1998]': '1998', 
    '1999 [YR1999]': '1999', '2000 [YR2000]':'2000'}, inplace = True)           
   
    #Changing the years 1991 and 1992 to numbers
    df1['1991'] = pd.to_numeric(df1['1991'], errors = 'coerce')
    df1['1992'] = pd.to_numeric(df1['1992'], errors = 'coerce')
    
    #Transposing the dataframe 1 and assigning to new dataframe 2
    df2 = df1.T
    
    #The function returns the two dataframes df1 and df2
    return df1, df2


#Calling the function with the climate_data csv file
df1, df2 = read_data('Climate_Data.csv')


"""
This section assigns and defines variables to be used in the graphical and
 statistical analysis. 

 methods like describe(), skew() and kurtosis() to explore the distributions of the indicators for selected 
countries or regions.
"""


# Defining variables for my graphs and statistical analysis
years = df2.index
countries = ['Ghana', 'Nigeria', 'Algeria', 'Canada', 'US', 'Brazil',
             'Argentina', 'India', 'China', 'Kazakhstan',' Australia', 'Russia',
             'UK',]

#Calling out some countries and storing in variables for analysis
Ghana = df2.xs('Ghana', level=0, axis=1)
UK = df2.xs('United Kingdom', level=0, axis=1)
Russia = df2.xs('Russia', level=0, axis=1)

# Creating dataframes for all the 6 indicators
pop = df2.xs('Population, total', level = 1, axis = 1).dropna()
CO2 = df2.xs('CO2 emissions (kt)', level = 1, axis = 1).dropna()
gdp = df2.xs('GDP (current US$)', level = 1, axis = 1).dropna()
forest = df2.xs('Forest area (% of land area)', level = 1, axis = 1).dropna()
water = df2.xs('Annual freshwater withdrawals, total (% of internal resources)',
             level = 1, axis = 1).dropna()
renewable_egy = df2.xs('Renewable energy consumption (% of total final energy consumption)',
             level = 1, axis = 1).dropna()

#Creating a new indicator gdp per capita as gdp divided by population
gdp_per_capita = gdp/pop
print(gdp_per_capita['United Kingdom'])
print(renewable_egy)

plt.figure()
plt.scatter(gdp_per_capita, renewable_egy)
plt.show()


"""
This section uses the kurtosis() and skew() functions in the stats.py file as 
 well as the describe() function in pandas to explore the statistical
 distributions of the data.
"""

print(st.kurtosis(renewable_egy))
print(st.skew(Russia))
print(Ghana.describe())


"""
This part of the code plots different graphs to show the relationships between
 the different series and countries over the years. The graphs plotted are bar 
 and line plots
"""


# Bar graph of population for all countries
pop.T.iloc[:,1::2].plot(kind='bar', figsize=(15,15), width=0.8)

plt.xlabel('Countries')
plt.ylabel('Population')
plt.title('Total population of countries over the years')
plt.legend()
plt.savefig('Assign2_Pop_Bar_graph.png')

#Bar graph of annual freshwater withdrawals per country 
water.T.iloc[:,1::2].plot(kind='bar', figsize=(15,15), width=0.8)

plt.xlabel('Countries')
plt.ylabel('Total fresh water withdrawals')
plt.title('Totalfresh water withdrawals of countries over the years')
plt.legend()
plt.savefig('Assign2_Water_Bar_graph.png')

#Line graph showing CO2 emmissions for countries over the years
CO2.iloc[::].plot(kind='line', figsize=(15,15), linestyle=':', linewidth=4)

plt.xlabel('Years')
plt.ylabel('CO2 Emissions (kt)')
plt.title(' CO2 Emissions over the years per Country')
plt.legend(fontsize='large')
plt.savefig('Assign2_CO2_Line_graph.png')


#Line graph showing GDP for all countries over the years
gdp.iloc[::].plot(kind='line', figsize=(15,15), linestyle=':', linewidth=4)

plt.xlabel('Years')
plt.ylabel('GDP (current US$)')
plt.title(' GDP (US$) of all countries over the years')
plt.legend(fontsize='large')
plt.savefig('Assign2_GDP_Line_graph.png')

plt.show()


"""
This part of the code explores the correlations between the countries on some
 selected indicators. We will investigate correlations between CO2 emmissions
 and GDP as well as Population and Forest Areas and Renewable energy.
"""



#Creating a variable indicator that holds all the indicators in the data
#indicators = pop, water, CO2, gdp, forest, renewable_egy


#Creating a variable that contains the correlation of all the indicators
Ghana = df2.xs('Ghana', level=0, axis=1)
ghana_corr = Ghana.corr()


Russia = df2.xs('Russia', level=0, axis=1)
russia_corr = Russia.corr()

sns.heatmap(ghana_corr, annot=True, cmap='hot', fmt='.2f')
plt.title('Correlation Matrix for Ghana')
plt.savefig('Assign2_GH_HeatMap.png')
plt.show()


sns.heatmap(russia_corr, annot=True, cmap='bone', fmt='.2f')
plt.title('Correlation Matrix for Russia')
plt.savefig('Assign2_RS_HeatMap.png')
plt.show()




















