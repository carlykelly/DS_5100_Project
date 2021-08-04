#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 16:00:25 2021

@author: chewy2.0
"""

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams["figure.figsize"] = [10, 6]
%config InlineBackend.figure_format = 'retina'

data = pd.read_csv('co2_renew_data.csv')
data.head()


df2 = data.copy()
df2= df2[['Country','1990','2005','2017']]

df3 = df2[(df2['1990']>=500)|(df2['2005']>=500)|(df2['2017']>=500)]
df3.set_index('Country', inplace= True)
df3.head(20)

#worked consider looking at top emmiters???
df3.transpose().apply(lambda x: x*100/sum(x), axis=1).plot(kind="bar", stacked=True, color=('yellow','red','green', 'cyan', 'navy', 'pink', 'magenta', 'orange', 'purple', 'lime','gold', 'grey','coral',  'blue'  ))
print(len(df3))
plt.title("Percent Fossil C02 Emissions > 500 Megatons Per Year ", fontsize=20)
plt.xlabel("Year")
plt.ylabel("Fossil C02 Emissions (% of those > 500 Megatons)",fontsize=16)
plt.legend(loc='best')
plt.show()

fig = plt.figure()
x = np.arange(1)
ax = fig.add_axes([0,0,1,1])

ax.bar(x + 0, df2['1990'].mean(), color = 'b', width = 0.25)
ax.bar( x+ .25, df2['1990'].median(), color = 'r', width = 0.25)

ax.bar(x + 0.75, df2['2005'].mean(), color = 'b', width = 0.25)
ax.bar(x+1, df2['2005'].median(), color = 'r', width = 0.25)

ax.bar(x + 1.5, df2['2017'].mean(), color = 'b', width = 0.25)
ax.bar(x+1.75, df2['2017'].median(), color = 'r', width = 0.25)


ax.set_ylabel('Fossils C02 Emissions in Megatons',fontsize=16)
ax.set_title('Mean & Median Fossils C02 Emissions in Megatons by Year', fontsize=20)
#ax.set_xticks(np.arange(3)+.25)
plt.xticks((0.12, .88, 1.63))
ax.set_xticklabels(['1990', '2005', '2017'], fontsize=18)

#ax.set_yticks(np.arange(0, 81, 10))
ax.legend(labels=['Mean', 'Median'],fontsize=16)
plt.show()