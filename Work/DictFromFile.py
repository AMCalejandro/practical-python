
prices = {} # Initialise dictionary
with open('Data/prices.csv', 'rt') as f:
    for line in f:
        stripped_line = line.rstrip()
        row = stripped_line.split(',')
        if len(row) > 1:
            prices[row[0]] = float(row[1])

print(prices)	         

