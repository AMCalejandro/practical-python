# From list of stocks and dictionary of prices, get the current value plus gain/loss


# Function to retrieve list of stocks
def read_portfolio(filename):
	import csv
	list_init = [] # Initialising list in which we append the resulting tuples
	with open(filename, 'r') as csv_file:
		header = next(csv_file).rstrip().split(',')
		file = csv.reader(csv_file)
		for line in file:
			list_init.append( {header[0] : line[0], header[1] : int(line[1]), \
					   header[2] : float(line[2])} )
		csv_file.close()
	return(list_init)

# Function to get the dictionary of prices
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


# Currtent value of the portfolio
list_dictionary_portfolio = read_portfolio("Data/portfolio.csv")
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


gain = current_value - portfolio_value
if gain > 0:
	print(('The gain from your portfolio is:  {gain}').format(gain=gain))
elif gain < 0:
	print(('The loss from your portfolio is: {gain}').format(gain=gain))
else:
	print('Neither gains nor losses')


print(('Current stocks value from the porfolio {portfolio_value}').format(portfolio_value=portfolio_value))

#print(abs(current_value-portfolio_value))
