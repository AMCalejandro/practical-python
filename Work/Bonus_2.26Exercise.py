# Perform dict comprehension to map a specific function or method to different type of data
# over a row from a full dataset


# We get the data needed
import csv
f = open('Data/dowstocks.csv')
rows = csv.reader(f)
headers = next(rows)
row = next(rows)

# We define the types for each columnd of our file
types = [str, float, "val.split('/')", str, float, float, float, float, int]

# We perform list comprehension

#print([tuple([int(x) for x in eval(func)]) if header == "date" \
#else func(val) for func,val,header in zip(types, row, headers)])

{header : (tuple([int(x) for x in eval(func)]) if header == "date" \
else func(val)) for func,val,header in zip(types, row, headers) }

