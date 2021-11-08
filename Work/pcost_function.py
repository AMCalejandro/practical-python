# Turning the pcost.py script into a function

def portfolio_cost(filename):
     sum = 0 # Initializing a variable to 0
     file = open(filename, 'rt')
     header = next(file) # Removing the header of the file
     line_count=0 
     try:
         for line in file:
             list = line.split(',')
             sum += (int(list[1])*float(list[2]))
             line_count += 1
     except:
         print("Missing integers in line:",int(line_count)+1,":", line)
     return(sum)


#print("Total cost",  portfolio_cost('Data/portfolio.csv'))
