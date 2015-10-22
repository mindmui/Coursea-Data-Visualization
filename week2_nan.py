# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 01:02:25 2015

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


listinternet = data['internetuserate']
print numpy.sum(listinternet.isnull())
listhiv = data['hivrate']
print numpy.sum(listhiv.isnull())
listsuicide = data['suicideper100th']
print numpy.sum(listsuicide.isnull())