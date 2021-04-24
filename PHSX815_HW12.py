# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 13:24:39 2021

@author: d338c921
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel("C:\\Users\\d338c921\\Documents\\IPEDS_data.xlsx")
d = df.values

#Questions to ask: What school should a prospective student with certain characteristics apply to? 
#Would they get into this school?
#Are there any correlations among the variables? Do you think these are reasonable? 
#How do these features correalt to unseen variables?
#Unforseen consequances of this model?
#Can you visualize the data?

##############################################################################
#pick numerical columns to attempt to visualize
##############################################################################
#Geographic Disrtibution of Schools
plt.figure()
plt.title("Geographic Distribution of Schools")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.scatter(d[:,6], d[:,7])

#Number of Applicants vs. Religious Affiliation
#Does religious affiliation have any correlation with the number of applicants the institution recieves?
#sort institutions into those that are affiliated w/ a religiion and those that aren't
non_rel = []
rel = []
for i in range(1534):
    if (d[i, 8] == "Not applicable"):
        non_rel = np.append(non_rel, d[i, 1])
    else:
        rel = np.append(rel, d[i, 1])

#Tuition & Fees vs. Time
#How do tuition rates chanmge over time? Do they decrease or increase? Why might that be?
plt.figure()
plt.title("Tuition Rates: 2010 - 2013")
plt.xlabel("Year")
plt.ylabel("Tuition")
plt.scatter(np.full((1534), 2010), d[:, 66])
plt.scatter(np.full((1534), 2011), d[:, 67])
plt.scatter(np.full((1534), 2012), d[:, 68]) 
plt.scatter(np.full((1534), 2013), d[:, 69])

#Predominantly White Institution? d[94]
#sort according to % of total enrollment that are white: Predominantely White = 50%+
PWI = []
nPWI = []
for i in range(1534):
    if (d[i, 94] >= 50.0):
        PWI = np.append(PWI, d[i, 1])
    else:
        nPWI = np.append(nPWI, d[i, 1])
        
print("Number of Predominantly White Institutions: " + str(len(PWI)) + "\n")
print(PWI)
print("Number of non-Predominantly White Institutions: " + str(len(nPWI)) + "\n")
print(nPWI)
#Is there any correlation between diversity and access to financial aid?