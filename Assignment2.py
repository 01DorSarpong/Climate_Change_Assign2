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
    df1 = pd.read_csv(file, index_col=['Country Name', 'Series Name'])
    
    #Changing the years 1991 and 1992 to numbers
    df1['1991 [YR1991]'] = pd.to_numeric(df1['1991 [YR1991]'], errors = 'coerce')
    df1['1992 [YR1992]'] = pd.to_numeric(df1['1992 [YR1992]'], errors = 'coerce')
    
    #Transposing the dataframe 1 and assigning to new dataframe 2
    df2 = df1.T
        
    #Cleaning df2 by removing country code and series code 
    df2 = df2.drop(['Country Code', 'Series Code'], axis = 0)
    
    #Renaming the index to remove years in [] 
    df2.rename(index = {'1991 [YR1991]': '1991', '1992 [YR1992]':'1992', 
    '1993 [YR1993]': '1993', '1994 [YR1994]':'1994', '1995 [YR1995]': '1995', 
    '1996 [YR1996]': '1996', '1997 [YR1997]':'1997', '1998 [YR1998]': '1998', 
    '1999 [YR1999]': '1999', '2000 [YR2000]':'2000'}, inplace = True)           
        
    #The function returns the two dataframes df1 and df2
    return df1, df2
    

#Calling the function with the climate_data csv file
df1, df2 = read_data('Climate_Data.csv')

"""
This section assigns and defines variables to be used in the graphical and
 statistical analysis. 

 methods like describe(), skew() and kurtosis() to explore the distributions 
 of the indicators for selected countries or regions.
"""


# Defining variables for my graphs and statistical analysis
years = df2.index
countries = ['Ghana', 'Nigeria', 'Algeria', 'Canada', 'United States', 'Brazil',
             'Argentina', 'India', 'China', 'Kazakhstan','Australia', 'Russia',
             'United Kingdom',]

#Calling out some countries and storing in variables for analysis
US = df2.xs('United States', level=0, axis=1)
Ghana = df2.xs('Ghana', level=0, axis=1)
China = df2.xs('China', level=0, axis=1)

# Creating dataframes for all the 6 indicators
pop = df2.xs('Population, total', level = 1, axis = 1).dropna()
CO2 = df2.xs('CO2 emissions (kt)', level = 1, axis = 1).dropna()
gdp = df2.xs('GDP (current US$)', level = 1, axis = 1).dropna()
forest = df2.xs('Forest area (% of land area)', level = 1, axis = 1)

water = df2.xs('Annual freshwater withdrawals',level = 1, axis = 1)
renewable_egy = df2.xs('Renewable energy consumption',
             level = 1, axis = 1).dropna()

#Creating a new dataframe as gdp per capita
gdpCapita = gdp.values / pop.values

"""
This section uses the kurtosis() and skew() functions in the stats.py file as 
 well as the describe() and groupby() function in pandas to explore the 
 statistical distributions of the data.
"""

print(China.describe())
print(st.kurtosis(pop))
print(st.kurtosis(CO2))
print(st.skew(forest))

# Grouping the US dataframe by rainfall and calculaating the mean
mean_rainfall = US.groupby('Annual freshwater withdrawals').mean()
print(mean_rainfall)

#Creating an array of total forest area for Ghana
Gh_forest = np.array(Ghana['Forest area (% of land area)'])
print(Gh_forest)

#Calculating the avaerage forest area of Ghana
mean_GH_population = Gh_forest.mean()
print(mean_GH_population)

"""
This part of the code plots different graphs to show the relationships between
 the different series and countries over the years. The graphs plotted are bar 
 and line plots
"""

# Bar graph of population for all countries plotting years over 2 steps
colors = ['skyblue', 'brown', 'purple', 'lightcoral', 'black']
gdp.T.iloc[:,1::2].plot(kind='bar', figsize=(15,15), width=0.8, color=colors)

#Setting the x and y labels and the ticks
plt.xlabel('Countries', fontsize=15)
plt.title('GDP in US$ of Countries', fontsize=20)
plt.legend()
plt.yticks(fontsize=17)
plt.xticks(rotation=45, fontsize=17)
plt.savefig('Assign2_GDP_Bar_graph.png')

#Bar graph of annual freshwater withdrawals per country over 2 years steps
colors = ['lightgreen', 'brown', 'violet', 'lightblue', 'grey']
CO2.T.iloc[:,1::2].plot(kind='bar', figsize=(15,15), width=0.8, color=colors)

#Setting the x and y labels and the ticks
plt.xlabel('Countries', fontsize=15)
plt.title('CO2 emissions (kt) of Countries', fontsize=20)
plt.legend()
plt.xticks(rotation=45, fontsize=17)
plt.savefig('Assign2_CO2_Bar_graph.png')

#Plotting a line graph showing water consumption for countries over the years
water.plot(kind='line', figsize=(15,10), linestyle='-', linewidth=3)
plt.xlabel('Years', fontsize=15)
plt.ylabel('Water volumes', fontsize=15)
plt.title('Annual Fresh Water Withdrawals', fontsize=20)
plt.legend(fontsize=15)
plt.xticks(fontsize=15)
plt.xlim(0, 9)

#Plotting a line graph showing population for all countries over the years
pop.plot(kind='line', figsize=(15,10), linestyle='-', linewidth=2)
plt.xlabel('Years', fontsize=15)
plt.ylabel('Population', fontsize=15)
plt.title(' Total Population', fontsize=20)
plt.legend(fontsize=15)
plt.xticks(fontsize=15)
plt.xlim(0, 9)
plt.show()

"""
This part of the code explores the correlations of the indicators for all the 
countries. A heatmap is plotted to show the correlations of the indicators
"""

#Calling the .corr() function on the dataframe and storing in a new variable 
df2_corr = df2.corr()
us_corr = US.corr()
gh_corr = Ghana.corr()

#Creating a for loop that plots all the heatmaps for the countries
for name in countries :
    plt.figure(figsize=(8, 6))
    heatmap = sns.heatmap(df2_corr.loc[name,name], annot=True, cmap='hot', fmt='.2f')
    heatmap.set_xticklabels(heatmap.get_xticklabels(), fontsize=15)
    heatmap.set_yticklabels(heatmap.get_yticklabels(), fontsize=15)
    plt.title(name,fontsize=15)
    plt.show()
  















