#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import quandl as Quandl
import wbdata as wb


# 0. Export path: Set to empty string '' if you want to export data to current directory
export_path = '../Csv/'


# 1. Import country codes and organize

# 1.1 Import country codes and names from the country_codes file from Quandl's WB WDI documentation: https://www.quandl.com/data/WWDI/documentation/documentation
country_Codes = {}

try:
    text_file = open('country_codes', 'r')
    lines = text_file.readlines()
    for line in lines:
        split = line.split('|')
        if len(split)>1:
            if len(split[1])==4:
                country_codes[split[0]] = split[1][:-1]
except:
    country_codes = {
 'Afghanistan': 'AFG',
 'Africa': 'AFR',
 'Albania': 'ALB',
 'Algeria': 'DZA',
 'American Samoa': 'ASM',
 'Andorra': 'AND',
 'Angola': 'AGO',
 'Antigua and Barbuda': 'ATG',
 'Arab World': 'ARB',
 'Argentina': 'ARG',
 'Armenia': 'ARM',
 'Aruba': 'ABW',
 'Australia': 'AUS',
 'Austria': 'AUT',
 'Azerbaijan': 'AZE',
 'Bahamas, The': 'BHS',
 'Bahrain': 'BHR',
 'Bangladesh': 'BGD',
 'Barbados': 'BRB',
 'Belarus': 'BLR',
 'Belgium': 'BEL',
 'Belize': 'BLZ',
 'Benin': 'BEN',
 'Bermuda': 'BMU',
 'Bhutan': 'BTN',
 'Bolivia': 'BOL',
 'Bosnia and Herzegovina': 'BIH',
 'Botswana': 'BWA',
 'Brazil': 'BRA',
 'Brunei Darussalam': 'BRN',
 'Bulgaria': 'BGR',
 'Burkina Faso': 'BFA',
 'Burundi': 'BDI',
 'Cabo Verde': 'CPV',
 'Cambodia': 'KHM',
 'Cameroon': 'CMR',
 'Canada': 'CAN',
 'Caribbean small states': 'CSS',
 'Cayman Islands': 'CYM',
 'Central African Republic': 'CAF',
 'Chad': 'TCD',
 'Channel Islands': 'CHI',
 'Chile': 'CHL',
 'China': 'CHN',
 'Colombia': 'COL',
 'Comoros': 'COM',
 'Congo, Dem. Rep.': 'COD',
 'Congo, Rep.': 'COG',
 'Costa Rica': 'CRI',
 "Cote d'Ivoire": 'CIV',
 'Croatia': 'HRV',
 'Cuba': 'CUB',
 'Curacao': 'CUW',
 'Cyprus': 'CYP',
 'Czech Republic': 'CZE',
 'Denmark': 'DNK',
 'Djibouti': 'DJI',
 'Dominica': 'DMA',
 'Dominican Republic': 'DOM',
 'East Asia & Pacific (all income levels)': 'EAS',
 'East Asia & Pacific (developing only)': 'EAP',
 'East Asia and the Pacific (IFC classification)': 'CEA',
 'Ecuador': 'ECU',
 'Egypt, Arab Rep.': 'EGY',
 'El Salvador': 'SLV',
 'Equatorial Guinea': 'GNQ',
 'Eritrea': 'ERI',
 'Estonia': 'EST',
 'Ethiopia': 'ETH',
 'Euro area': 'EMU',
 'Europe & Central Asia (all income levels)': 'ECS',
 'Europe & Central Asia (developing only)': 'ECA',
 'Europe and Central Asia (IFC classification)': 'CEU',
 'European Union': 'EUU',
 'Faeroe Islands': 'FRO',
 'Fiji': 'FJI',
 'Finland': 'FIN',
 'France': 'FRA',
 'French Polynesia': 'PYF',
 'Gabon': 'GAB',
 'Gambia, The': 'GMB',
 'Georgia': 'GEO',
 'Germany': 'DEU',
 'Ghana': 'GHA',
 'Greece': 'GRC',
 'Greenland': 'GRL',
 'Grenada': 'GRD',
 'Guam': 'GUM',
 'Guatemala': 'GTM',
 'Guinea': 'GIN',
 'Guinea-Bissau': 'GNB',
 'Guyana': 'GUY',
 'Haiti': 'HTI',
 'Heavily indebted poor countries (HIPC)': 'HPC',
 'High income': 'HIC',
 'High income: OECD': 'OEC',
 'High income: nonOECD': 'NOC',
 'Honduras': 'HND',
 'Hong Kong SAR, China': 'HKG',
 'Hungary': 'HUN',
 'Iceland': 'ISL',
 'India': 'IND',
 'Indonesia': 'IDN',
 'Iran, Islamic Rep.': 'IRN',
 'Iraq': 'IRQ',
 'Ireland': 'IRL',
 'Isle of Man': 'IMN',
 'Israel': 'ISR',
 'Italy': 'ITA',
 'Jamaica': 'JAM',
 'Japan': 'JPN',
 'Jordan': 'JOR',
 'Kazakhstan': 'KAZ',
 'Kenya': 'KEN',
 'Kiribati': 'KIR',
 'Korea, Dem. Rep.': 'PRK',
 'Korea, Rep.': 'KOR',
 'Kosovo': 'KSV',
 'Kuwait': 'KWT',
 'Kyrgyz Republic': 'KGZ',
 'Lao PDR': 'LAO',
 'Latin America & Caribbean (all income levels)': 'LCN',
 'Latin America & Caribbean (developing only)': 'LAC',
 'Latin America and the Caribbean (IFC classification)': 'CLA',
 'Latvia': 'LVA',
 'Least developed countries: UN classification': 'LDC',
 'Lebanon': 'LBN',
 'Lesotho': 'LSO',
 'Liberia': 'LBR',
 'Libya': 'LBY',
 'Liechtenstein': 'LIE',
 'Lithuania': 'LTU',
 'Low & middle income': 'LMY',
 'Low income': 'LIC',
 'Lower middle income': 'LMC',
 'Luxembourg': 'LUX',
 'Macao SAR, China': 'MAC',
 'Macedonia, FYR': 'MKD',
 'Madagascar': 'MDG',
 'Malawi': 'MWI',
 'Malaysia': 'MYS',
 'Maldives': 'MDV',
 'Mali': 'MLI',
 'Malta': 'MLT',
 'Marshall Islands': 'MHL',
 'Mauritania': 'MRT',
 'Mauritius': 'MUS',
 'Mexico': 'MEX',
 'Micronesia, Fed. Sts.': 'FSM',
 'Middle East & North Africa (all income levels)': 'MEA',
 'Middle East & North Africa (developing only)': 'MNA',
 'Middle East and North Africa (IFC classification)': 'CME',
 'Middle income': 'MIC',
 'Moldova': 'MDA',
 'Monaco': 'MCO',
 'Mongolia': 'MNG',
 'Montenegro': 'MNE',
 'Morocco': 'MAR',
 'Mozambique': 'MOZ',
 'Myanmar': 'MMR',
 'Namibia': 'NAM',
 'Nepal': 'NPL',
 'Netherlands': 'NLD',
 'New Caledonia': 'NCL',
 'New Zealand': 'NZL',
 'Nicaragua': 'NIC',
 'Niger': 'NER',
 'Nigeria': 'NGA',
 'North Africa': 'NAF',
 'North America': 'NAC',
 'Northern Mariana Islands': 'MNP',
 'Norway': 'NOR',
 'OECD members': 'OED',
 'Oman': 'OMN',
 'Other small states': 'OSS',
 'Pacific island small states': 'PSS',
 'Pakistan': 'PAK',
 'Palau': 'PLW',
 'Panama': 'PAN',
 'Papua New Guinea': 'PNG',
 'Paraguay': 'PRY',
 'Peru': 'PER',
 'Philippines': 'PHL',
 'Poland': 'POL',
 'Portugal': 'PRT',
 'Puerto Rico': 'PRI',
 'Qatar': 'QAT',
 'Romania': 'ROU',
 'Russian Federation': 'RUS',
 'Rwanda': 'RWA',
 'Samoa': 'WSM',
 'San Marino': 'SMR',
 'Sao Tome and Principe': 'STP',
 'Saudi Arabia': 'SAU',
 'Senegal': 'SEN',
 'Serbia': 'SRB',
 'Seychelles': 'SYC',
 'Sierra Leone': 'SLE',
 'Singapore': 'SGP',
 'Sint Maarten (Dutch part)': 'SXM',
 'Slovak Republic': 'SVK',
 'Slovenia': 'SVN',
 'Small states': 'SST',
 'Solomon Islands': 'SLB',
 'Somalia': 'SOM',
 'South Africa': 'ZAF',
 'South Asia': 'SAS',
 'South Asia (IFC classification)': 'CSA',
 'South Sudan': 'SSD',
 'Spain': 'ESP',
 'Sri Lanka': 'LKA',
 'St. Kitts and Nevis': 'KNA',
 'St. Lucia': 'LCA',
 'St. Martin (French part)': 'MAF',
 'St. Vincent and the Grenadines': 'VCT',
 'Sub-Saharan Africa (IFC classification)': 'CAA',
 'Sub-Saharan Africa (all income levels)': 'SSF',
 'Sub-Saharan Africa (developing only)': 'SSA',
 'Sub-Saharan Africa excluding South Africa': 'SXZ',
 'Sub-Saharan Africa excluding South Africa and Nigeria': 'XZN',
 'Sudan': 'SDN',
 'Suriname': 'SUR',
 'Swaziland': 'SWZ',
 'Sweden': 'SWE',
 'Switzerland': 'CHE',
 'Syrian Arab Republic': 'SYR',
 'Tajikistan': 'TJK',
 'Tanzania': 'TZA',
 'Thailand': 'THA',
 'Timor-Leste': 'TLS',
 'Togo': 'TGO',
 'Tonga': 'TON',
 'Trinidad and Tobago': 'TTO',
 'Tunisia': 'TUN',
 'Turkey': 'TUR',
 'Turkmenistan': 'TKM',
 'Turks and Caicos Islands': 'TCA',
 'Tuvalu': 'TUV',
 'Uganda': 'UGA',
 'Ukraine': 'UKR',
 'United Arab Emirates': 'ARE',
 'United Kingdom': 'GBR',
 'United States': 'USA',
 'Upper middle income': 'UMC',
 'Uruguay': 'URY',
 'Uzbekistan': 'UZB',
 'Vanuatu': 'VUT',
 'Venezuela, RB': 'VEN',
 'Vietnam': 'VNM',
 'Virgin Islands (U.S.)': 'VIR',
 'West Bank and Gaza': 'PSE',
 'World': 'WLD',
 'Yemen, Rep.': 'YEM',
 'Zambia': 'ZMB',
 'Zimbabwe': 'ZWE'}
    
        
# 1.2 Use wbdata to get lists of country codes by income groups
countries_income_all =  [i['id'] for i in wb.get_country(incomelevel=['LIC','MIC','HIC'],display=False)]
countries_income_h = [i['id'] for i in wb.get_country(incomelevel=['HIC'],display=False)]
countries_income_m = [i['id'] for i in wb.get_country(incomelevel=['MIC'],display=False)]
countries_income_l = [i['id'] for i in wb.get_country(incomelevel=['LIC'],display=False)]

countries_income_oecd = ['AUS','CAN','CHL','CZE','DNK','EST','HUN','ISL','ISR','JPN'
                       ,'KOR','NZL','NOR''POL','SVK','SVN','SWE','CHE','USA']


# 2. Import data from Quandl

# 2.1 Money supply (LCU)
moneyDf = pd.DataFrame({})

for name,key in country_codes.items():
    try:
        df = Quandl.get('WWDI/'+key+'_FM_LBL_MONY_CN',authtoken="QqLL1AFCjc31_MVo4qsU")
        df.columns = [key]
        moneyDf = pd.concat([moneyDf,df],axis=1)
    except:
        pass

# 2.2 GDP deflator
deflatorDf = pd.DataFrame({})

for name,key in country_codes.items():
    try:
        df = Quandl.get('WWDI/'+key+'_NY_GDP_DEFL_ZS',authtoken="QqLL1AFCjc31_MVo4qsU")
        df.columns = [key]
        deflatorDf = pd.concat([deflatorDf,df],axis=1)
    except:
        pass

# 2.3 Real GDP
gdpDf = pd.DataFrame({})

for name,key in country_codes.items():
    try:
        df = Quandl.get('WWDI/'+key+'_NY_GDP_MKTP_KD',authtoken="QqLL1AFCjc31_MVo4qsU")
        df.columns = [key]
        gdpDf = pd.concat([gdpDf,df],axis=1)
    except:
        pass
    
    
# 3. Create datasets for quantity theory without interest and exchange rates

# 3.1 Dataframes to use
dataFrames = [moneyDf, deflatorDf, gdpDf]

# 3.2 Identify the codes for countries that have at least some data in all DataFrames
availableCodes = []
for code in country_codes.values():
    if all(code in frame for frame in dataFrames):
        if any( all(np.isnan(x) for x in frame[code]) for frame in dataFrames):
            print(code)
        else:
            availableCodes.append(code)        
            
# print('Number of countries: ',len(availableCodes))

# 3.3 Construct the dataset including the average growth rates of variabes for each country for which 
# at least 10 years of data are available
included_codes = []
obs = []
mData = []
pData = []
yData = []
    
for c in availableCodes:
    count = 0
    ind = []
    
    for i in dataFrames[0].index[1:]:

        noneNan = all( not np.isnan(frame[c].loc[i]) for frame in dataFrames)
        anyNan = any( np.isnan(frame[c].loc[i]) for frame in dataFrames)

        if noneNan:
            count+=1
            ind.append(i)
        elif anyNan and count>0:
            break

    if count >9:
        m = (moneyDf[c].loc[ind[-1]]/moneyDf[c].loc[ind[0]])**(1/count)-1
        p = (deflatorDf[c].loc[ind[-1]]/deflatorDf[c].loc[ind[0]])**(1/count)-1
        y = (gdpDf[c].loc[ind[-1]]/gdpDf[c].loc[ind[0]])**(1/count)-1

        included_codes.append(c)
        mData.append(np.around(m,5))
        pData.append(np.around(p,5))
        yData.append(np.around(y,5))
        obs.append(count)


# 3.4 Identify the names of the countries that are incuded
included_names = []
for c in included_codes:
    for name, code in country_codes.items():
        if c == code:
            included_names.append(name)

# 3.5 Create the main dataframe
quantity_theory_data = pd.DataFrame({'iso code':included_codes,'observations':obs,'inflation':pData,'money growth':mData,'gdp growth':yData},index = included_names)
quantity_theory_data = quantity_theory_data[['iso code','observations','inflation','money growth','gdp growth']]
quantity_theory_data = quantity_theory_data.sort_index()

print('Number of countries: ',len(quantity_theory_data))


# 3.6 Create dataframes organized by income levels
indexL=[]
indexM=[]
indexH=[]
indexOecd=[]

# 3.7 Create lists of country names in each income-level group
for country in quantity_theory_data.index:
    code = quantity_theory_data['iso code'].loc[country]
    if code in countries_income_l:
        indexL.append(country)
    if code in countries_income_m:
        indexM.append(country)
    if code in countries_income_h:
        indexH.append(country)
    if code in countries_income_oecd:
        indexOecd.append(country)

# 3.8 Drop countries with inf values
quantity_theory_data = quantity_theory_data.replace([np.inf, -np.inf], np.nan).dropna()

# 3.9 Export data to csv

# All countries
quantity_theory_data.to_csv(export_path+'quantity_theory_data.csv',index=True,index_label='country')

# Low-income countries
# quantity_theory_data.loc[indexL].to_csv(export_path+'quantity_theory_data_l.csv',index=True,index_label='country')

# Middle-income countries
# quantity_theory_data.loc[indexM].to_csv(export_path+'quantity_theory_data_m.csv',index=True,index_label='country')

# High-income countries
# quantity_theory_data.loc[indexH].to_csv(export_path+'quantity_theory_data_h.csv',index=True,index_label='country')

# OECD member countries
# quantity_theory_data.loc[indexOecd].to_csv(export_path+'quantity_theory_data_oecd.csv',index=True,index_label='country')

