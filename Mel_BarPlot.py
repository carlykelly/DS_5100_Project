#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 15:57:27 2021

@author: melaniehazlett
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 09:36:28 2021
@author: xxpit
"""

import pandas as pd
import difflib

co2 = pd.read_csv('co2_data.csv')
renew = pd.read_csv('re_data.csv')

merged = pd.merge(co2, renew, on = "Country", how = "inner")
merged.to_csv('co2_renew_data.csv')

co2_comp_renew = co2['Country'].isin(renew['Country'])
dif_df = co2[~co2_comp_renew]

database = renew['Country']
similar = [difflib.get_close_matches(word, database, n = 1, cutoff = 0.8) for word in dif_df['Country']]

dif_df['Country'] = similar
dif_df = dif_df[dif_df['Country'].astype(str) != '[]']
dif_df['Country'] = [country[0] for country in dif_df['Country']]
co2.loc[dif_df.index, 'Country'] = dif_df['Country']


#SECOND PASS
co2_comp_renew = co2['Country'].isin(renew['Country'])
dif_df = co2[~co2_comp_renew]



translation = {
    'Czech Republic':'Czechia',
    'East Timor':'Timor Leste',
    'Eswatini':'Eswatini (Swaziland)',
    'North Korea':'Korea DPR',
    'São Tomé and Príncipe':'Sao Tome & Principe',
    'South Korea':'Korea Rep',
    'Sudan South Sudan':'South Sudan',
    'The Gambia': 'Gambia'
    }


for original, translate in translation.items():
    dif_df['Country'] = dif_df['Country'].str.replace(original, translate)
co2.loc[dif_df.index, 'Country'] = dif_df['Country']

#THIRD PASS
co2_comp_renew = co2['Country'].isin(renew['Country'])
dif_df = co2[~co2_comp_renew]

merged = pd.merge(co2, renew, on = "Country", how = "inner")
merged.to_csv('co2_renew_data.csv')


#Check what is different from perspective of RENEW

#Sudan problem
# row = renew[renew["Country"].str.contains("Sudan")]

# new_row = row.loc[182]
# new_row["Total"] = sum(row["Total"])
# new_row["Total_RE"] = sum(row["Total"])
# new_row["RE_pct"] = sum(row["Total"])
# new_row["Hydro"] = sum(row["Hydro"])
# new_row["Hydro_pct_re"] = sum(row["Hydro_pct_re"])

df = pd.read_csv(r"co2_renew_data.csv")

df.CO2_land_area
#type(df.CO2_land_area)

########## Beginning of Charts ##############
#import packages
import pandas as pd
from matplotlib import pyplot as plt

#Create font dictionaries to be used in all plots for consistency
font = {'family': 'Arial',
        'color':  'black',
        'weight': 'bold',
        'size': 14
        }
fonttitle = {'family': 'Arial', 
             'color': 'black', 
             'weight': 'bold', 
             'size': 12}

#Create barchart with highest emissions per land area
#sort datagrame by Co2 land area from high to low
df2 = df.sort_values('CO2_land_area', axis=0, ascending=False)
#create x and y from sorted DF
country = df2['Country']
per_land_area = df2['CO2_land_area']

# Use top 10 highest. Create bar chart.  Adjust color and width of bars
plt.bar(country[:10], per_land_area[:10], width = 0.4, color = 'green')
plt.xticks(rotation = 45) #rotate so they fit but are still readable
plt.title('Highest CO2 Emissions Per Land Area', fontdict=font) #set title with title font
plt.xlabel('Country', fontdict = fonttitle) #set x and y axis with axis fonts
plt.ylabel('CO2 Emissions', fontdict = fonttitle)
plt.show()


#Create barchart with highest emissions per capita
#sort datagrame by Co2 emissions per capita from high to low
df1 = df.sort_values('CO2_per_capita', axis=0, ascending=False)
#create x and y from sorted df
per_capita = df1['CO2_per_capita']
country2 = df1['Country']
plt.bar(country2[:10], per_capita[:10], width = 0.4, color = 'blue')
plt.xticks(rotation = 45)
plt.title('Highest CO2 Emissions Per Capita', fontdict = font)
plt.xlabel('Country', fontdict = fonttitle)
plt.ylabel('CO2 Emissions', fontdict = fonttitle)
plt.show()


#Scatter Plot of Per Land Area versus Per Capita
# create x and y from DF
per_capita1 = df['CO2_per_capita']
per_land_area1 = df['CO2_land_area']
#create scatter plot
plt.scatter(per_land_area1, per_capita1, s = 3, color = 'blue')
plt.xlabel('Per Land Area', fontdict = fonttitle)
plt.ylabel('Per Capita', fontdict = fonttitle)
plt.title('C02 Emissions Per Land Area versus Per Capita', fontdict = font)
plt.text(46643, 24, 'Bahrain')
plt.text(16935, 46.8, 'Curacao')
plt.text(3074, 64.9, 'Palau')
plt.text(76841, 9.6, 'Singapore')
plt.text(8440, 37.1, 'Qatar')
plt.show()



