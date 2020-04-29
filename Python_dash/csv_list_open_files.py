# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 08:26:26 2019

@author:
"""

import os
import csv
#import glob

#print(glob.glob("c:\\_PRACA\\V300_csv\\*.csv"))

def loadcsvcol(path, col):
    with open(path) as csvfile:
        datareader = csv.reader(csvfile,delimiter=',', quotechar='"')
        
        i=0
        data=[]
        for row in datareader:
            if i > 0:
                data.append(row[col])
            i+=1
    return data
            
path="c:\\_PRACA\\V300_csv\\"
csvbases=[x for x in os.listdir(path) if x.endswith(".csv")]
print(csvbases)

data=[]
for csvbase in csvbases:
    data.append(loadcsvcol(path + csvbase,3))

print(data)


