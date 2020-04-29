# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 10:17:48 2019

@author: jasa
"""

import csv
with open('c:\_PRACA\V300_csv\WC22100700_V300_FT_PL1Llevel.csv') as csvfile:
    datareader = csv.reader(csvfile,delimiter=',', quotechar='"')
   
    
    i=0
    data=[]
    for row in datareader:
        if i > 0:
            data.append(row[3])
        i+=1

for num in data:
    print(num)