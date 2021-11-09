# pcost.py
#
# Exercise 1.27

import csv
sum = 0 # Initializing a variable to 0
#with open('Data/portfolio.csv', 'rt') as file:
file = open('Data/portfolio.csv')
rows = csv.reader(file) 
header = next(rows) # Removing the header of the file
for line in rows:
    #print(line)
    #list = line.split(',')
    sum += (int(line[1])*float(line[2])) # Transforming data and calculating the price of all stockes

print(f'Total cost {sum}')

file.close()
