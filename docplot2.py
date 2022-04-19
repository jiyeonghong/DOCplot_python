from itertools import zip_longest
import pandas as pd
import matplotlib.pyplot as plt
import csv
"""
Author - Jiyeong Hong
Date - APR 18 2022
Description - DOC plot (date-concentration)

"""

def generategraph(x, y, _title, idx):
    plt.plot(x, y, color = 'g', linestyle = 'dashed',
                marker = 'o',label = "ResultValue")
        
    plt.xticks(rotation = 25)
    plt.xlabel('ActivityStartDate')
    plt.ylabel('ResultValue')
    plt.title(_title, fontsize = 20)
    plt.grid()
    plt.legend()
    plt.savefig(str(idx) + '_Notation.png')
    plt.clf() # Clear plt to get new Notiation's data

def multipleplot(i, x, y): 
    with open('GSLDOC3.csv','r') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        next(lines, None)
        title = "Empty"
        for row in lines:
            if row[1] == str(i): # row[1] == count
                #print(i)
                x.append(row[2]) # stack row[2]
                y.append(float(row[3])) # stack row[3]
                title = row[0] 

        # Call plt
        generategraph(x, y, title, i)
        x.clear() # clear x to add new notation's row[2]
        y.clear() # clear y to add new notation's row[3]


#_maxNotation = 16
x = [] 
y = []
NotationStack = []

with open('GSLDOC3.csv','r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    next(lines, None) 

    for row in lines:
        NotationStack.append(int(row[1]))
# Find higest number in Notation.
_maxNotation = max(NotationStack)


for i in range(1, int(_maxNotation)+1):
    multipleplot(i,x,y)
    
    
