from follow import follow
import csv
from pcost_finalReport import read_portfolio
import tableformat

def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row) ]

def make_dict(rows, header):
    for row in rows:
        yield {name:value for name,value in zip(header, row) } #dict(zip(header, row))

def filter_symbols(rows, names):
    for row in rows:
        if row['name'] in names:
            yield row

portfolio = read_portfolio("Data/portfolio.csv")


def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0,1,4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dict(rows, ['name', 'price', 'change'])
    return rows


def ticker(portfile, logfile, fmt):
    stock_live = follow("Data/stocklog.csv")
    rows = parse_stock_data(stock_live) # For each live row, we get it on dict format

    portfolio = read_portfolio("Data/portfolio.csv")
    rows = filter_symbols(rows, portfolio) # Check if the live rows are in portfolio.

    formatter = tableformat.create_formatter(fmt)    #We create the formatter
    formatter.headings(['Name','Price','Change']) # We pass the heading tou our formatter
    for row in rows:
         formatter.row([row['name'], f"{row['price']:0.2f}" , f"{row['change']:0.2f}" ])


def main(args):
    if len(args) != 4:
        raise SystemExit("Usage: %s portfoliofile logfile fmt" % args[0])
    ticker(args[1],args[2],args[3])

if __name__ == "__main__":
    import sys
    main(sys.argv)
