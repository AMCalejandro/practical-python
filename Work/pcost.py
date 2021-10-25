# pcost.py
#
# Exercise 1.27

sum = 0 # Initializing a variable to 0
#with open('Data/portfolio.csv', 'rt') as file:
file = open('Data/portfolio.csv', 'rt')
header = next(file) # Removing the header of the file
for line in file:
    #print(line)
    list = line.split(',')
    sum += (int(list[1])*float(list[2])) # Transforming data and calculating the price of all stockes

print(f'Total cost {sum}')
