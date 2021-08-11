# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 19:39:32 2021

@author: xxpit
"""

#IMPORT STATEMENT
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Read in the data, sort by renewable energy produced
merged = pd.read_csv('co2_renew_data.csv')
merge_sorted = merged.sort_values(by = 'Total_RE', ascending = False)
plt.plot(merge_sorted['Total_RE']) #example plot for RE? 

#Obtain renewable energy columns
renewables = merge_sorted.loc[:,["Total_RE", "Hydro", "Wind", "Bio", "Solar", "Geo"]]
renewables["Country"] = merge_sorted["Country"]
renewables = renewables.replace(np.nan, 0)
renewables.head()

#plt.bar(renewables["Country"].head(), renewables["Total_RE_Fixed"].head())


#renewables["Total_RE_Fixed"] = 
#plt.bar(renewables["Country"].head(), renewables["Total_RE_Fixed"].head())
renewables["Total_RE_Fixed"] = renewables["Hydro"] + renewables["Wind"] + renewables["Bio"] + renewables["Solar"] + renewables["Geo"]
renewables.head()

#Show top 5 renewable eneryg producers
renewable_top5 = renewables.head()
renewable_top5

#Produce horizontal bar plot for use in report/presentation
left = len(renewable_top5)
plt.barh(renewable_top5["Country"], renewable_top5["Hydro"], left = 0)

plt.barh(renewable_top5["Country"], renewable_top5["Wind"], 
         left = renewable_top5["Hydro"])

plt.barh(renewable_top5["Country"], renewable_top5["Bio"], 
         left = renewable_top5["Hydro"] + renewable_top5["Wind"])

plt.barh(renewable_top5["Country"], renewable_top5["Solar"], 
         left = renewable_top5["Hydro"] + renewable_top5["Wind"] + 
         renewable_top5["Bio"])

plt.barh(renewable_top5["Country"], renewable_top5["Geo"], 
         left = renewable_top5["Hydro"] + renewable_top5["Wind"] + 
         renewable_top5["Bio"] + renewable_top5["Solar"])

plt.title('Breakdown of Renewable Energy')
plt.xlabel('Total Gigawatt Hours of Renewable Energy Produced')
#plt.legend()

#Veritcal bar plot?
plt.bar(renewable_top5["Country"], renewable_top5["Hydro"])
plt.bar(renewable_top5["Country"], renewable_top5["Wind"])
plt.bar(renewable_top5["Country"], renewable_top5["Bio"])
plt.bar(renewable_top5["Country"], renewable_top5["Solar"])
plt.bar(renewable_top5["Country"], renewable_top5["Geo"])

#Seaborn for visualization?
import seaborn as sns
sns.jointplot(x = "2005", y ="2017", edgecolor ="white", data = merge_sorted)