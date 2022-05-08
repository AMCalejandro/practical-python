# From list of stocks and dictionary of prices, get the current value plus gain/loss

import fileparse
import stock
import tableformat
from portfolio import Portfolio
# Custom function to check for empty strings
def is_empty_or_blank(msg):
	""" This function checks if given string is empty
	or contain only shite spaces"""
	import re
	return re.search("^\s*$", msg)


def read_portfolio(filename, select = None, types = None, has_headers = True, delimiter = ",", silence_errors = False):
	with open(filename) as lines:
		list_dictionaries = fileparse.parse_csv(lines, select = ['name','shares','price'], types = [str,int,float])
		list_portfolio = [ stock.Stock(dict['name'], dict['shares'], dict['price']) for dict in list_dictionaries]
	#return(list_portfolio)
	return Portfolio(list_portfolio)
# Function to retrieve list of stocks
# Improved with zip and enumerate.
# read_portfolio is not hardcoded anymore and now is able to access the values of interest
# given more generic files
#def read_portfolio(filename):
#        import csv
#        list_init = [] # Initialising list in which we append the resulting tuples
#        with open(filename, 'r') as file:
#                csv_file = csv.reader(file)
#                header = next(csv_file)

        # Checking if there if there is any empty string
#                for index, line in enumerate(csv_file, start=1):
#                        record = dict(zip(header, line))
                        #print(record)
#                        bool = None
#                        for element in line:
#                                if is_empty_or_blank(element):
#                                        index = int(index)
#                                        print(f'Row {index:>0d}: Couldn\'t convert: {line}')
#                                        bool = True
#                                        break
#                        if bool:
#                                continue
#                        else:
#                                list_init.append( {'name': record['name'],\
#                                                  'shares' : int(record['shares']),\
#                                                  'price': float(record['price'])} )
                                #print(list_init)
#        return(list_init)


def read_prices(filename, select = None, types=None, has_headers = False,  delimiter = ",", silence_errors=False):
	with open(filename) as lines:
		tuple_prices = fileparse.parse_csv(lines, select = select, types = types, has_headers = has_headers, delimiter= delimiter, silence_errors = silence_errors)
	return(tuple_prices)
# Function to get the dictionary of prices
#def read_prices(filename):
#	import csv
#	file = open(filename, 'r')
#	csv_file = csv.reader(file)
#	dict_init = {}
#
#	for stocks in (csv_file):
#		#print(stocks)
#		if stocks:
#			dict_init[stocks[0]] = stocks[1]
#	file.close()
#	return(dict_init)


# Function to report a list of tupes from dictionary of prices and list of stocks
def make_summary(dict_prices, list_stocks):
	list_init = []
	#print(dict_prices)

	#for i in range(len(list_stocks)):
	for i in list_stocks:
		#name,shares,price_old = list(list_stocks[i].__dict__.values()) # Using __dict__ variable to retrieve an list of the values from the stock.Stock instance
		name, shares, price_old = [i.name,i.shares,i.price]
		#print(name,shares,price_old)
		price_new = float(dict_prices.get(name))
		list_init.append((name,shares, price_new, (price_new - float(price_old))))
	return(list_init)


# Getting ready to come up with the gain/loss
# Currtent value of the portfolio

#list_dictionary_portfolio = read_portfolio("Data/portfolio.csv")
# Reading data with missing values to make sure my function handles them
#list_dictionary_portfolio = read_portfolio("Data/missing.csv")
# Trying to read data with different format to make sure the right use of zip and enumerate
#list_dictionary_portfolio = read_portfolio("Data/portfoliodate.csv")


# Getting the prices
#dictionary_prices = read_prices("Data/prices.csv")
#print(dictionary_prices)


#print(make_report(dictionary_prices, list_dictionary_portfolio))


### THIS HAS BEEN IMPROVED MAKING USE OF LIST COMPREHENSION ###
#portfolio_value = 0
#current_value = 0
#for stock in list_dictionary_portfolio:
#	name_stock = stock['name']
#	shares_stock = int(stock['shares'])
#	portfolio_value += stock['price']*shares_stock
	#print(name_stock)
	#print(shares_stock)
	#Accessing the dictionary of current sotck prices per name
	#value_stock = dictionary_prices[name_stock]
#	current_value += float(dictionary_prices[name_stock])*shares_stock
def print_report(list_dictionary_portfolio, dictionary_prices):
	# Doing sequence reduction to get the portfolio value in one line of code
	#portfolio_value = sum([float(s['price']) * int(s['shares']) for s in list_dictionary_portfolio])
	#portfolio_value = sum([float(s.price) * int(s.shares) for s in list_dictionary_portfolio])

	#portfolio_value = sum([s.cost for s in list_dictionary_portfolio])
	portfolio_value = list_dictionary_portfolio.total_cost
	print("Initial portfolio value:", portfolio_value)

	#Doing sequence reduction to get the current value of our portfolio
	#current_value = sum([ float(dictionary_prices[s['name']]) * int(s['shares']) for s in list_dictionary_portfolio])

	#current_value = sum([ float(dictionary_prices[s.name]) * int(s.shares) for s in list_dictionary_portfolio])
	current_value = sum([float(dictionary_prices[name]) * int(n) for name,n in list_dictionary_portfolio.tabulate_shares().items()])
	print("Current portofolio value", current_value)

	# Printing the gain/loss
	gain = current_value - portfolio_value
	if gain > 0:
        	print(('The gain from your portfolio is:  {gain}').format(gain=gain))
	elif gain < 0:
        	print(('The loss from your portfolio is: {gain}').format(gain=gain))
	else:
        	print('Neither gains nor losses')


def print_sharesUpdate(list_dictionary_portfolio, dictionary_prices, formatter):
	# Using the list of stocks and dictionary of prices to come up with the list of tuples
	list_tuples = make_summary(dictionary_prices, list_dictionary_portfolio)
	formatter.headings(['Name','Shares','Price','Change'])
	#headers = ('Name', 'Shares', 'Price', 'Change')
	#print('%10s %10s %10s %10s' % headers)
	#print(('-'*10 + ' ') * len(headers))


	for name, shares, price, change in list_tuples:
		rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
		formatter.row(rowdata)
	#for name,shares,price,change in list_tuples:
	#	dollar_price='$' + str(price)
        #	print(f'{name:>10s} {shares:>10d} {dollar_price:>9s} {change:>10.2f}')



#def portfolio_report(portfolio_filename, prices_filename):
#	list_dictionary_portfolio = read_portfolio(portfolio_filename)
#	dictionary_prices = read_prices(prices_filename)
#
#	print_report(list_dictionary_portfolio, dictionary_prices)
#	print_sharesUpdate(list_dictionary_portfolio, dictionary_prices)

#portfolio_report('Data/portfolio.csv', 'Data/prices.csv')


def portfolio_report(portfolio_filename, prices_filename, select_pf = None, types_pf = None, has_headers_pf = True, delimiter_pf = ",", silence_errors_pf = False, select_pc = None, types_pc = None, has_headers_pc = False, delimiter_pc = ",", silence_errors_pc = False, fmt = 'txt'):
	list_dictionary_portfolio = read_portfolio(portfolio_filename, select = select_pf, types = types_pf, has_headers = has_headers_pf, delimiter = delimiter_pf, silence_errors = silence_errors_pf)
	dictionary_prices = dict(read_prices(prices_filename, select = select_pc, types = types_pc, has_headers = has_headers_pc, delimiter = delimiter_pc, silence_errors = silence_errors_pc))

	#print(list_dictionary_portfolio)
	#print(dictionary_prices)
	#formatter = tableformat.TextTableFormatter()

	formatter = tableformat.create_formatter(fmt)
	print_report(list_dictionary_portfolio, dictionary_prices)
	print_sharesUpdate(list_dictionary_portfolio, dictionary_prices, formatter)


def main(args):
    if len(args) != 4:
        raise SystemExit("Usage: %s portfolio pricefile format" % args[0])
    portfolio_report(args[1], args[2], select_pf = ['name','shares','price'], types_pf = [str,int,float], delimiter_pf = ",", fmt = args[3])

#portfolio_report('Data/portfolio.csv', 'Data/prices.csv', select_pf = ['name','shares','price'], types_pf = [str,int,float], has_headers_pf = True, delimiter_pf = ",", silence_errors_pf = False)

if __name__ == '__main__':
    import sys
    main(sys.argv)



#def portfolio_report(portfolio_filename, prices_filename, select_pf, types_pf, has_headers_pf, delimiter_pf, silence_errors_pf=False):
#	list_dictionary_portfolio = read_portfolio(portfolio_filename, select = select_pf, types = types_pf, has_headers = has_headers_pf, delimiter = delimiter_pf, silence_errors = silence_errors_pf)
#	dictionary_prices = read_prices(prices_filename)
#
#	print(list_dictionary_portfolio)
#	print(dictionary_prices)
#
#	print_report(list_dictionary_portfolio, dictionary_prices)
#	print_sharesUpdate(list_dictionary_portfolio, dictionary_prices)

#portfolio_report('Data/portfolio.csv', 'Data/prices.csv', select_pf = ['name','shares','price'], types_pf = [str,int,float], has_headers_pf = True, delimiter_pf = ",")



# The issue is that dictionary_prices get a list of tuples from fileparse.parse_csv()
# Currently, my function in this file called read_prices() retrieves a dictionary, and I make use of such to get the outputs required. I need to adapt this
