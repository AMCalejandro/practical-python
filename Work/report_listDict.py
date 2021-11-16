# report.py
#
# Exercise 2.5

def read_portfolio(filename):
	import csv
	list_init = [] # Initialising list in which we append the resulting tuples
	with open(filename, 'rf') as csv_file:
		header = next(csv_file).rstrip().split(',')
		file = csv.reader(csv_file)
		for line in file:
			list_init.append( {header[0] : line[0], header[1] : int(line[1]), \
					   header[2] : float(line[2])} )
		csv_file.close()
	return(list_init)


list_dictionary = read_portfolio("Data/portfolio.csv")
#print(list_dictionary)

result = 0
for stock in list_dictionary:
	result += stock['price']*stock['shares']
print(('Stocks value {result}').format(result=result))
