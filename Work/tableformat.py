class TableFormatter:
    def headings(self,headers):
        '''
        Emit the table headings.
        '''
        raise NotImplementedError()
    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()

class CSVTableFormatter(TableFormatter):
    '''
    Output portfolio data in CSV format.
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))

class HTMLTableFormatter(TableFormatter):
    '''
    Output portfolio data in HTML format.
    '''
    def headings(self, headers):
        print('<tr>', end = '')
        for h in headers:
            print(f'<th>{h}</th>', end ='')
        print('</tr>')

    def row(self, rowdata):
        print('<tr>', end = '')
        for d in rowdata:
            print(f'<td>{d}</td>', end='')
        print('</tr>')

class FormatError(Exception):
    pass

def create_formatter(name):
    '''
    Function that creates a formatter  based on the user decision
    '''
    if name == 'txt':
        return TextTableFormatter()
    elif name == 'csv':
        return CSVTableFormatter()
    elif name == 'html':
        return HTMLTableFormatter()
    else:
        raise FormatError(f'Unknown format {name}')

def print_table(portfolio, columns, formatter):
    '''
    Make a nice portfolio formatting from user-specific attributes
    '''
    formatter.headings(columns)
    for object in portfolio:
        rowdata = [str(getattr(object, name)) for name in columns]
        #print(rowdata)
        formatter.row(rowdata)






