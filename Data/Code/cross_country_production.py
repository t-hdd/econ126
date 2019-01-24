#!/usr/bin/env python
# coding: utf-8

import pandas as pd


# 0. Export path: Set to empty string '' if you want to export data to current directory
export_path = '../Csv/'


# 1. Import data
data = pd.read_excel('https://www.rug.nl/ggdc/docs/pwt90.xlsx',sheet_name='Data')


# 2. Create dataset

# Variable equals last year in data
year = data.year.iloc[-1]

# Restrict data to final year
data = data[data['year']==year].reset_index()

# Select columns: 'countrycode','country','cgdpo','emp','hc','ck'
data = data[['countrycode','country','cgdpo','emp','hc','ck']]

# Rename columns
data.columns = ['country_code','country','gdp','labor','human_capital','physical_capital']

# Drop countries with missing observations
data = data.dropna()


# 3. Export data
data[['country_code','country','gdp','labor','human_capital','physical_capital']].to_csv(export_path+'cross_country_production.csv',index=False)