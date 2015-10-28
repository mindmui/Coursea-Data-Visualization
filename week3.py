# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 15:39:11 2015

@author: Mind
"""

import pandas
import numpy

#import data
data = pandas.read_csv('gapminder.csv', low_memory=False)

# bug fix for display formats to avoid run time errors
pandas.set_option('display.float_format', lambda x:'%f'%x)

# Covert text string to upper (or lower)
#data.columns = map(str.upper, data.columns)

# To check numbers of rows and columns
#print(len(data))
#print(len(data.columns))

# Before start counting 
# Convert strings to numeric
data['internetuserate'] = data['internetuserate'].convert_objects(convert_numeric=True)
data['hivrate'] = data['hivrate'].convert_objects(convert_numeric=True)
data['suicideper100th'] = data['suicideper100th'].convert_objects(convert_numeric=True)


# replace group 9 to NaN
data['internetuserate'] = data['internetuserate'].replace(9, numpy.nan)

#to include NA
cs = data['internetuserate'].value_counts(dropna = False, sort = False)

# set 11 as dummy
data.loc[data['internetuserate'].isnull(),'internetuserate'] = 11 

# dictionary to recode 
recode1 = {1:6 ,2:5, 3:4} #old value = new value
data['OURFREQ'] = data['internetuserate'].map(recode1)

# to capture more quantitative features
recode2 = {1: '30 days', 2: '22 days'}
data['OURFREQbyMonth'] = data['internetuserate'].map(recode2)

# for example
data['Estimatedaysmoke'] = data['OURFREQbyMonth']*data['OURFREQperday']
# get first 25 lines
data['internetuserate'].head(25)

# always check for errors
sub3 = data[['internetuserate','hivrate','suicideper100th']]
sub3.head(25)

# to divide into groups using lambda function
def ETHNICITY(row):
    if row['NUMETHNIC'] > 1:
        return 1
    if row['H1GI4'] == 1:
        return 2
    
    
data['ETHNICITY'] = data.apply(lambda row: ETHNICITY(row), axis =1)

sub2 = data[['AID','H1GI4']]
print sub2.head(25)


# compare age group :
# check the freq distr. first
# if you want to cut into 4 groups cut according to quartiles

sub2['agegroupto4']= pandas.qcut(sub2.AGE,4,labels=['A','B','C','D'])

# customize split
sub2['agebyourgroup3'] = pandas.cut(sub2.AGE,[17,20,22,25])
# 18-20, 21-22, 22-25

# cross tab function:
print pandas.crosstab(sub2['agebyourgroup3'], sub2['agegroupto4'])


