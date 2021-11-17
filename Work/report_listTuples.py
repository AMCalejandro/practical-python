# report.py
#
# Exercise 2.4

def read_portfolio(filename):
	import csv
	list_init = [] # Initialising list in which we append the resulting tuples
	with open(filename, 'r') as csv_file:
		header = next(csv_file)
		file = csv.reader(csv_file)
		for line in file:
			list_init.append((line[0], int(line[1]), float(line[2]) ))
			print(line)
		csv_file.close()
	return(list_init)


list_tuples = read_portfolio("Data/portfolio.csv")
#print(list_tuples)

result = 0  #Object to store results
for stock in list_tuples:
	result += stock[1] * stock[2]


print(('Stocks {result}').format(result=result))


