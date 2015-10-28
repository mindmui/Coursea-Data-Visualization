# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 17:01:20 2015

@author: Mind
"""

import pandas
import numpy

#import data
data = pandas.read_csv('gapminder.csv', low_memory=False)

# bug fix for display formats to avoid run time errors
pandas.set_option('display.float_format', lambda x:'%f'%x)

# Convert strings to numeric
data['internetuserate'] = data['internetuserate'].convert_objects(convert_numeric=True)
data['hivrate'] = data['hivrate'].convert_objects(convert_numeric=True)
data['suicideper100th'] = data['suicideper100th'].convert_objects(convert_numeric=True)



data['internetQ']= pandas.qcut(data['internetuserate'],3,labels=['Low','Average','High'])
c1 = data['internetQ'].value_counts(sort=False, dropna=False)
p1 = data['internetQ'].value_counts(sort=False, dropna=False, normalize=True)
print '#### Internet Use Rate ###'
print 'Group', '    Counts'
print c1
print " "
print 'Group', '    Percentage'
print p1


data['hivQ']= pandas.qcut(data['hivrate'],3,labels=['Low','Average','High'])
c2 = data['hivQ'].value_counts(sort=False, dropna=False)
p2 = data['hivQ'].value_counts(sort=False, dropna=False, normalize=True)

print " "
print '#### HIV Rate ###'
print 'Group', '    Counts'
print c2
print " "
print 'Group', '    Percentage'
print p2

data['suicideQ']= pandas.cut(data['suicideper100th'],[0,10,20,100],labels=['Suicide <10%','Suicide 10–20%','Suicide >20%'])
c2 = data['suicideQ'].value_counts(sort=False, dropna=False)
p2 = data['suicideQ'].value_counts(sort=False, dropna=False, normalize=True)

print " "
print '#### Suicide Rate ###'
print 'Group', '           Counts'
print c2
print " "
print 'Group', '          Percentage'
print p2
