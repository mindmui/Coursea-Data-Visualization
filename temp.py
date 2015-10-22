# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas

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

# Divide Internetuserate into 9 groups
internetusegroup = []
for i,j in enumerate(data['internetuserate']):
    if j < 5:
        internetusegroup.append("1")
    elif j < 15:
        internetusegroup.append("2")
    elif j < 25:
        internetusegroup.append("3")
    elif j < 35:
        internetusegroup.append("4")
    elif j < 45:
        internetusegroup.append("5")  
    elif j < 55:
        internetusegroup.append("6")
    elif j < 65:
        internetusegroup.append("7")    
    elif j < 75:
        internetusegroup.append("8")
    else:
        internetusegroup.append("9")
        
#initial counts
counter1 = 0
counter2 = 0
counter3 = 0
counter4 = 0
counter5 = 0
counter6 = 0
counter7 = 0
counter8 = 0
counter9 = 0

#use traditional counter to count the number for each case
for item in internetusegroup:
    if item == "1":
        counter1 += 1
    elif item == "2":
        counter2 += 1
    elif item == "3":
        counter3 += 1
    elif item == "4":
        counter4 += 1
    elif item == "5":
        counter5 += 1
    elif item == "6":
        counter6 += 1
    elif item == "7":
        counter7 += 1
    elif item == "8":
        counter8 += 1        
    else:
        counter9 += 1

total = counter1+counter2+counter3+counter4+counter5+counter6+counter7+counter8+counter9

#To display internetusegroup in table
countername = ["<5%","5-15%","15-25%","25-35%","35-45%","45-55%","55-65%","65-75%",">75%"]
counterlist = [counter1,counter2,counter3,counter4,counter5,counter6,counter7,counter8,counter9]
percentcount = [x/float(total)*100 for x in counterlist]
data1 = pandas.DataFrame(countername)
data1["Count"] = counterlist
data1["Percentage"] = percentcount
print data1

###############################################

# Divide hivrate into 3 groups
hivgroup = []
for i,j in enumerate(data['hivrate']):
    if j < 5:
        hivgroup.append("1")
    elif j < 10:
        hivgroup.append("2")
    else:
        hivgroup.append("3")

#initial counts
counter1 = 0
counter2 = 0
counter3 = 0


#use traditional counter to count the number for each case
for item in hivgroup:
    if item == "1":
        counter1 += 1
    elif item == "2":
        counter2 += 1      
    else:
        counter3 += 1

total = counter1+counter2+counter3

#To display internetusegroup in table
countername = ["HIV <5%","HIV 5-10%","HIV >10&"]
counterlist = [counter1,counter2,counter3]
percentcount = [x/float(total)*100 for x in counterlist]
data2 = pandas.DataFrame(countername)
data2["Count"] = counterlist
data2["Percentage"] = percentcount
print " "
print data2


######################################################################

# Divide suicideper100th into 3 groups
suicidegroup = []
for i,j in enumerate(data['suicideper100th']):
    if j < 10:
        suicidegroup.append("1")
    elif j < 20:
        suicidegroup.append("2")
    else:
        suicidegroup.append("3")

#initial counts
counter1 = 0
counter2 = 0
counter3 = 0


#use traditional counter to count the number for each case
for item in suicidegroup:
    if item == "1":
        counter1 += 1
    elif item == "2":
        counter2 += 1      
    else:
        counter3 += 1

total = counter1+counter2+counter3

#To display internetusegroup in table
countername = ["Suicide <10%","Suicide 10-20%","Suicide >20%"]
counterlist = [counter1,counter2,counter3]
percentcount = [x/float(total)*100 for x in counterlist]
data3 = pandas.DataFrame(countername)
data3["Count"] = counterlist
data3["Percentage"] = percentcount
print " "
print data3

