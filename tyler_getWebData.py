# -*- coding: utf-8 -*-
"""
@author: Tyler Entner
"""
# %%
# Import Block
import pandas as pd
import requests

# %%
# Obtain table for CO2 Emissions

# Save URL of interest
url = "https://en.wikipedia.org/wiki/List_of_countries_by_carbon_dioxide_emissions"


r = requests.get(url)  # Obtain handle to URL

df_list = pd.read_html(r.text)  # this parses all the tables in webpage
df = df_list[1]  # through inspection, table 1 is what we need
df.head()

# Below line creates new column names based on flattened MultiIndex
# Ex: "Fossil CO2 ... " / "1990" becomes "Fossil_CO2_..._1990"
df.columns = ["_".join(a) for a in df.columns.to_flat_index()]

# Or just rename columns....
df.columns = ['Country', '1990', '2005', '2017', 'CO2_pct_world',
              'CO2_pct_change', 'CO2_land_area', 'CO2_per_capita']

# %%
# Save DF to CSV
df.to_csv('co2_data.csv')

# %%

url = "https://en.wikipedia.org/wiki/List_of_countries_by_renewable_electricity_production"

r = requests.get(url)  # Obtain handle to URL

df_list = pd.read_html(r.text)  # this parses all the tables in webpage
df = df_list[1]  # through inspection, table 1 is what we need
df.head()

df.columns = ["_".join(a) for a in df.columns.to_flat_index()]

df.columns = ['Country', 'Year', 'Total', 'Total_RE', 'RE_pct', 'Hydro', 'Hydro_pct_tot',
              'Hydro_pct_re', 'Wind', 'Wind_pct_tot', 'Wind_pct_re', 'Bio', 
              'Bio_pct_tot', 'Bio_pct_re', 'Solar', 'Solar_pct_tot', 
              'Solar_pct_re', 'Geo', 'Geo_pct_tot', 'Geo_pct_re', 'Ref']

df.to_csv('re_data.csv')


# %%