# Turning the pcost.py script into a function

#def portfolio_cost(filename):
#    import csv
#    import sys
#    sum = 0 # Initializing a variable to 0
#    file = open(filename)
#    rows = csv.reader(file)
#    headers = next(rows)
#    line_count=0
#    for line in rows:
#        try:
#            #list = line.split(',')
#            sum += (int(line[1])*float(line[2]))
#            line_count += 1
#        except:
#            print("Missing integers in line:",int(line_count)+1,":", line)
#    return(sum)
#    file.close()

# Improving the function. Using enumerate to track the index and
# Using zip to create a dictionary with the header and one row at a time
#def portfolio_cost(filename):
#    import csv
#    import sys
#    sum = 0 # Initializing a variable to 0
#    file = open(filename)
#    rows = csv.reader(file)
#    headers = next(rows)
#    for index, line in enumerate(rows, start=1):
#        record = dict(zip(headers,line))
        #print(record)
#        try:
#            sum += float(record['price'])*int(record['shares'])
#        except:
#            print("Missing integers in line:", index)
#    return(sum)
#    file.close()

import pcost_finalReport
def portfolio_cost(filename):
    #sum = 0
    portfolio_dictlist = pcost_finalReport.read_portfolio(filename, delimiter = ",")
    #for index in range(len(portfolio_dictlist)):
    #    record = portfolio_dictlist[index]
        #print(record)
    #    try:
            #sum += float(record['price'])*int(record['shares'])
    #        sum += float(record.price)*int(record.shares)
    #    except:
    #        print("Missing integers in line:", index)

    #return(sum)
    return portfolio_dictlist.total_cost


def main(args):
    if len(args) == 2:
        filename = args[1]
    else:
        filename = 'Data/portfolio.csv'

    cost = portfolio_cost(filename)
    print('Total cost:', cost)

if __name__ == '__main__':
    import sys
    main(sys.argv)
