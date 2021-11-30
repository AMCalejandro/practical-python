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
def portfolio_cost(filename):
    import csv
    import sys
    sum = 0 # Initializing a variable to 0
    file = open(filename)
    rows = csv.reader(file)
    headers = next(rows)
    for index, line in enumerate(rows, start=1):
        record = dict(zip(headers,line))
        #print(record)
        try:
            sum += float(record['price'])*int(record['shares'])
        except:
            print("Missing integers in line:", index)
    return(sum)
    file.close()




import sys
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)
