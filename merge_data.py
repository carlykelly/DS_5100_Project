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



