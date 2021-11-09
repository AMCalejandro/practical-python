# Turning the pcost.py script into a function


def portfolio_cost(filename):
    import csv
    import sys
    sum = 0 # Initializing a variable to 0
    file = open(filename)
    rows = csv.reader(file)
    headers = next(rows)
    line_count=0
    for line in rows:
        try:
            #list = line.split(',')
            sum += (int(line[1])*float(line[2]))
            line_count += 1
        except:
            print("Missing integers in line:",int(line_count)+1,":", line)
    return(sum)
    file.close()



import sys
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)
