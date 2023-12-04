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


# Creating dataframes for all the series
pop = df2.xs('Population, total', level=1, axis = 1)
CO2 = df2.xs('CO2 emissions (kt)', level=1, axis = 1)
gdp = df2.xs('GDP (current US$)', level=1, axis = 1)
forest = df2.xs('Forest area (% of land area)', level=1, axis = 1)
water = df2.xs('Annual freshwater withdrawals, total (% of internal resources)',
             level=1, axis = 1)
renewable_egy = df2.xs('Renewable energy consumption (% of total final energy consumption)',
             level=1, axis = 1)


print(pop)
pop_years = pop[::].values
print(pop_years)

plt.figure(figsize=(12,15))

pop.plot(kind='bar')

"""
plt.bar(countries, pop_years[0], label='1991')
plt.bar(countries, pop_years[1], label='1992')
plt.bar(countries, pop_years[2], label='1993')
plt.bar(countries, pop_years[3], label='1994')
plt.bar(countries, pop_years[4], label='1995')
plt.bar(countries, pop_years[5], label='1996')
plt.bar(countries, pop_years[6], label='1997')
plt.bar(countries, pop_years[7], label='1998')
plt.bar(countries, pop_years[8], label='1999')
plt.bar(countries, pop_years[9], label='2000')
"""
plt.xlabel('Countries')
plt.ylabel('Total Population')
plt.title(' Total population of countries over the years')

plt.legend(fontsize='large')
plt.show()


cy = pop.iloc[0]
gh_pop = pop['Ghana']
ng_pop = pop['Nigeria']
alg_pop = pop.iloc[1]
cd_pop = pop['Canada']
us_pop = pop['United States']
bz_pop = pop['Brazil']
ar_pop = pop['Argentina']
in_pop = pop['India']
ch_pop = pop['China']
kz_pop = pop['Kazakhstan']
au_pop = pop['Australia']
rs_pop = pop['Russia']
kg_pop = pop['United Kingdom']

"""
gh_pop = pop['Ghana']
ng_pop = pop['Nigeria']
alg_pop = pop['Algeria']
cd_pop = pop['Canada']
us_pop = pop['United States']
bz_pop = pop['Brazil']
ar_pop = pop['Argentina']
in_pop = pop['India']
ch_pop = pop['China']
kz_pop = pop['Kazakhstan']
au_pop = pop['Australia']
rs_pop = pop['Russia']
kg_pop = pop['United Kingdom']
"""



gh_co2 = CO2['Ghana']
ng_co2 = CO2['Nigeria']
alg_co2 = CO2['Algeria']
cd_co2 = CO2['Canada']
us_co2 = CO2['United States']
bz_co2 = CO2['Brazil']
ar_co2 = CO2['Argentina']
in_co2 = CO2['India']
ch_co2 = CO2['China']
kz_co2 = CO2['Kazakhstan']
au_co2 = CO2['Australia']
rs_co2 = CO2['Russia']
kg_co2 = CO2['United Kingdom']

CO2_countries = np.array([gh_co2,ng_co2, alg_co2, cd_co2, us_co2, bz_co2, ar_co2, in_co2, ch_co2, kz_co2, au_co2, rs_co2, kg_co2])


#print(CO2_countries)



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



Africa_arr = np.array(Africa)
#print(Africa_arr)

# Using statistical methods to explore the data
print(st.kurtosis(Africa_arr))
print(st.skew(Africa_arr))
print(Ghana.describe())
print(pop.apply(skew))





data_correlatioin = df2.corr()
#print(data_correlatioin)


# Plotting a line graph of CO2 emmissions for all countries
"""
plt.figure(figsize=(12,15))
plt.plot(years, gh_co2, label='Ghana')
plt.plot(years, ng_co2, label='Nigeria')
plt.plot(years, alg_co2, label='Algeria')
plt.plot(years, cd_co2, label='Canada')
plt.plot(years, us_co2, label='US')
plt.plot(years, bz_co2, label='Brazil')
plt.plot(years, ar_co2, label='Argentina')
plt.plot(years, in_co2, label='India')
plt.plot(years, ch_co2, label='China')
plt.plot(years, kz_co2, label='Kazakhstan')
plt.plot(years, kg_co2, label='UK')

plt.xlabel('Years')
plt.ylabel('CO2 Emissions (kt)')
plt.title(' CO2 Emissions over the years per Country')

plt.legend(fontsize='large')
plt.show()
"""

# Plotting a bar graph of Population of all countries

plt.figure(figsize=(12,15))



plt.xlabel('Countries')
plt.ylabel('Total Population')
plt.title(' Total population of countries over the years')

plt.legend(fontsize='large')
plt.show()



#df2.iloc[1].rename(columns={'CO2 emissions (kt)': 'CO2 Ems', 'GDP (current US$)': 'GDP', 
#                           'Annual freshwater withdrawals, total (% of internal resources)': 'Annual Freshwater',
#                           'Forest area (% of land area)': 'Forest Area', 
 #                          'Renewable energy consumption (% of total final energy consumption)': 'Ren Energy Cons',
 #                          'Population, total': 'Population'},
#                  inplace=True)



"""
#data_years['Series Name'].rename(columns={'CO2 emissions (kt)': 'CO2 Ems', 'GDP (current US$)': 'GDP', 
                           'Annual freshwater withdrawals, total (% of internal resources)': 'Annual Freshwater',
                           'Forest area (% of land area)': 'Forest Area', 
                           'Renewable energy consumption (% of total final energy consumption)': 'Ren Energy Cons',
                           'Population, total': 'Population'},
                  inplace=True)
"""




