# fileparse.py
#
# Exercise 3.3

import csv

def parse_csv(filename):
    '''
    Parse a CSV file into a list of dictionaries
    '''
    with open(filename) as f:
        rows = csv.reader(f)
        header = next(rows)
        #print(header)
        records = []
        for row in rows:
            if not row:
                continue
            records.append(dict(zip(header, row)))
    return records

#print(parse_csv("Data/portfolio.csv"))

