# Using python dictionaries as containers


def read_prices(filename):
	import csv
	file = open(filename, 'r')
	csv_file = csv.reader(file)
	dict_init = {}

	for stocks in csv_file:
		#print(stocks)
		if stocks:
			dict_init[stocks[0]] = stocks[1]

	return(dict_init)


