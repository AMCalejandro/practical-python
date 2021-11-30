# From list of stocks and dictionary of prices, get the current value plus gain/loss

# Custom function to check for empty strings
def is_empty_or_blank(msg):
	""" This function checks if given string is empty
	or contain only shite spaces"""
	import re
	return re.search("^\s*$", msg)

# Function to retrieve list of stocks
def read_portfolio(filename):
	import csv
	list_init = [] # Initialising list in which we append the resulting tuples
	with open(filename, 'r') as csv_file:
		header = next(csv_file).rstrip().split(',')
		file = csv.reader(csv_file)
		# Checking if there if there is any empty string
		for index, line in enumerate(file, start=1):
			bool = None
			for element in line:
				if is_empty_or_blank(element):
					index = int(index)
					print(f'Row {index:>0d}: Couldn\'t convert: {line}')
					bool = True
					break
			if bool:
				continue
			else:
				list_init.append( {header[0] : line[0], header[1] : int(line[1]),\
						  header[2] : float(line[2])} )
	return(list_init)

# Function to get the dictionary of prices
def read_prices(filename):
	import csv
	file = open(filename, 'r')
	csv_file = csv.reader(file)
	dict_init = {}

	for stocks in (csv_file):
		#print(stocks)
		if stocks:
			dict_init[stocks[0]] = stocks[1]
	return(dict_init)

# Function to report a list of tupes from dictionary of prices and list of stocks
def make_report(dict_prices, list_stocks):
	list_init = []
	#print(dict_prices)
	for i in range(len(list_stocks)):
		name,shares,price_old = list(list_stocks[i].values())
		#print(name,shares,price_old)
		price_new = float(dict_prices.get(name))
		list_init.append((name,shares, price_new, (price_new-float(price_old))))
	return(list_init)


# Getting ready to come up with the gain/loss
# Currtent value of the portfolio
#list_dictionary_portfolio = read_portfolio("Data/portfolio.csv")
list_dictionary_portfolio = read_portfolio("Data/missing.csv")

# Getting the prices
dictionary_prices = read_prices("Data/prices.csv")
#print(dictionary_prices)
portfolio_value = 0
current_value = 0
for stock in list_dictionary_portfolio:
	name_stock = stock['name']
	shares_stock = int(stock['shares'])
	portfolio_value += stock['price']*shares_stock
	#print(name_stock)
	#print(shares_stock)
	#Accessing the dictionary of current sotck prices per name
	value_stock = dictionary_prices[name_stock]
	current_value += float(dictionary_prices[name_stock])*shares_stock

# Printing the gain/loss
gain = current_value - portfolio_value
if gain > 0:
	print(('The gain from your portfolio is:  {gain}').format(gain=gain))
elif gain < 0:
	print(('The loss from your portfolio is: {gain}').format(gain=gain))
else:
	print('Neither gains nor losses')


# Printing the current stocks worth
print(('Current stocks value from the porfolio {portfolio_value}').format(portfolio_value=portfolio_value))


# Using the list od stocks and dictionary of prices to come up with the list of tuples
list_tuples = make_report(dictionary_prices, list_dictionary_portfolio)

headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s' % headers)
print(('-'*10 + ' ') * len(headers))
#for r in list_tuples:
#	print('%10s %10d %10.2f %10.2f' % r)

for name,shares,price,change in list_tuples:
	dollar_price='$' + str(price)
	print(f'{name:>10s} {shares:>10d} {dollar_price:>9s} {change:>10.2f}')

