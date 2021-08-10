#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 16:40:08 2021

@author: carlykelly
"""

import pandas as pd
import requests
import unittest
import difflib

class Project1():
    
    def __init__(self, mylink, table_num=1, data='cotest', r=None):
        self.mylink = mylink
        self.table_num = table_num
        self.data = data
        if r == None:
            self.r = ''
        else:
            self.r = r

    def webscrape(self):
        
        #This code was taken from tyler_getWebData.py
        # Save URL of interest
        url = self.mylink
        

        self.r = requests.get(url)  # Obtain handle to URL
        
        df_list = pd.read_html(self.r.text)  # this parses all the tables in webpage
        df = df_list[self.table_num] 

        # Below line creates new column names based on flattened MultiIndex
        # Ex: "Fossil CO2 ... " / "1990" becomes "Fossil_CO2_..._1990"
        df.columns = ["_".join(a) for a in df.columns.to_flat_index()]
        
        # Save DF to CSV
        df.to_csv(f'{self.data}_data.csv')
        return self.r
    def merge(self, csv1, csv2, title1='csv1', title2='csv2'):
        
        #This code is taken from merge_data.py
        csv1 = pd.read_csv(f'{csv1}')
        csv2 = pd.read_csv(f'{csv2}')
    
    
        co2_comp_renew = csv1['Country'].isin(csv2['Country'])
        dif_df = csv1[~co2_comp_renew]
    
        database = csv2['Country']
        similar = [difflib.get_close_matches(word, database, n = 1, cutoff = 0.8) for word in dif_df['Country']]
    
        dif_df['Country'] = similar
        dif_df = dif_df[dif_df['Country'].astype(str) != '[]']
        dif_df['Country'] = [country[0] for country in dif_df['Country']]
        csv1.loc[dif_df.index, 'Country'] = dif_df['Country']
    
    
        #SECOND PASS
        co2_comp_renew = csv1['Country'].isin(csv2['Country'])
        dif_df = csv1[~co2_comp_renew]
    
    
    
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
        csv1.loc[dif_df.index, 'Country'] = dif_df['Country']
        
        #THIRD PASS
        co2_comp_renew = csv1['Country'].isin(csv2['Country'])
        dif_df = csv1[~co2_comp_renew]
        
        merged = pd.merge(csv1, csv2, on = "Country", how = "inner")
        merged.to_csv(f'{title1}_{title2}_data.csv')

class webscrapetestsuite(unittest.TestCase): 
    
    def test_link_input(self):
        # test that the requests work
        test1 = Project1('https://en.wikipedia.org/wiki/List_of_countries_by_carbon_dioxide_emissions')
        test1.webscrape()
        
        # Testing that we access the website without an error
        expected = 200
        #Checking that the status code is 200 (reached without error)
        self.assertEqual(test1.r.status_code, expected)
        
    def test_merge(self):
        # test that the merge method work
        #Creating a class from which to run the merge method.
        #Need to put in the website as class is designed to first scrape, then merge
        test2 = Project1('https://en.wikipedia.org/wiki/List_of_countries_by_carbon_dioxide_emissions')
        test2.merge('../Carly_only_Project1/co2_data.csv', '../Carly_only_Project1/re_data.csv')
        
        # Testing that we have the expected number of rows in our output
        expected = 196
        #The program is designed that the merged csv should be saved in the same file
        #this code so relative path is just the file name
        file_path = "csv1_csv2_data.csv"
        #Reading in csv from the path name above
        df_to_test = pd.read_csv(file_path)
        # Comparing the number of rows in the csv output to 196
        self.assertEqual(len(df_to_test['Country']), expected)
        
if __name__ == '__main__':
    unittest.main()