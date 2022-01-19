# fileparse.py
#
# Exercise 3.3

import csv

#def parse_csv(filename, select = None):
#    '''
#    Parse a CSV file into a list of dictionaries
#    '''
#    with open(filename) as f:
#        rows = csv.reader(f)
#        header = next(rows)
#        if select:
#           indices = [header.index(col_interest) for col_interest in select]
#           records = [{column: row[index] for column,index in zip(select, indices)}  for row in rows]
#
#        else:
#            records = []
#            for row in rows:
#                if not row:
#                    continue
#                records.append(dict(zip(header, row)))
#    return records
#print(parse_csv("Data/portfolio.csv"))


def parse_csv(filename, select = None, types = None, has_headers = True):
    '''
    Parse a CSV file into a list of dictionaries
    '''
    with open(filename) as f:
        rows = csv.reader(f)
        if has_headers:
            headers = next(rows)

        if select:
            indices = [headers.index(col_interest) for col_interest in select]
            headers = select
        else:
            indices = []

        records = []
        for row in rows:
            if not row:
                continue
            if indices:
                row = [row[index] for index in indices]
            if types:
                row = [func(val) for func,val in zip(types, row)]
            if has_headers:
                record = dict(zip(headers, row))
                records.append(record)
            if not has_headers:
                records.append(tuple(row))

    return records


