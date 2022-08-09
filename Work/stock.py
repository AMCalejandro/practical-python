from typedproperty import typedproperty, String, Integer, Float

class Stock:
    '''
    The instance of a stock holding
    '''

    # Restricting the attributes names with __slots__
    __slots__ = ('_name', '_shares','_price')

    name = String('name')
    shares = Integer('shares')
    price = Float('price')


    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return f'Stock({self.name!r}, {self.shares!r}, {self.price!r})'

    @property
    def cost(self):
        '''
        Method that returns the cost of current shares according to market price
        '''
        return self.shares * self.price

    def sell(self, sells):
        '''
        A method to update the total shares after selling some
        '''
        self.shares -= sells

#    @property
#    def shares(self):
#        return self._shares

#    @shares.setter
#    def shares(self, value):
#        if not isinstance(value, int):
#            raise TypeError("Expected int")
#        self._shares = value




#class NewStock(Stock):
#    def yow(self):
#        print("Yow!")
