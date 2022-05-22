import os
import time

def follow(filename):
    '''
    Generator that outputs lines of a file starting from the end
    '''
    with open(filename, 'r') as f:
        f.seek(0, os.SEEK_END)
        while True:
            line = f.readline()
            if line== '':
                time.sleep(0.1)
                continue
            yield line

# Example use
if __name__ == "__main__":
    from pcost_finalReport import read_portfolio
    myPortfolio = read_portfolio("Data/portfolio.csv")
    for line in follow("Data/stocklog.csv"):
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if name in myPortfolio:
            print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')

