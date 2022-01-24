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


def parse_csv(filename, select = None, types = None, has_headers = True, delimiter = " ", silence_errors = False):
    '''
    Parse a CSV file into a list of dictionaries
    '''
    with open(filename) as f:
        rows = csv.reader(f, delimiter = delimiter)

        if select and not has_headers:
             raise RuntimeError('select requires column headers')

        if has_headers:
            headers = next(rows)

        if select:
            indices = [headers.index(col_interest) for col_interest in select]
            headers = select
        else:
            indices = []

        records = []
#        for row in rows:
        for row_index,row in enumerate(rows):
            if not row:
                continue
            if indices:
                row = [row[index] for index in indices]


            if types:
#                row = [func(val) for func,val in zip(types, row)]
                 try:
                     row = [func(val) for func,val in zip(types, row)]
                 except ValueError as e:
                     if not silence_errors:
                         print(f'Row {row_index + 1}: Couldn\'t convert {row}')
                         print(f'Row {row_index + 1}: Reason invalid literal for int() with base 10: \'\'')
                     continue

            if has_headers:
                record = dict(zip(headers, row))
                records.append(record)
            else:
                records.append(tuple(row))

    return records


