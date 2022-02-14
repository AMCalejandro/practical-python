class Stock:
    '''
    The instance of a stock holding
    '''
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

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
