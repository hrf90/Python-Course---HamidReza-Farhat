
import numpy as np

class Portfolio():

    def __init__(self, cash=0, stock={}, stock_prices={}, mf={}, hist=[]):
        self.cash = cash
        self.stock = stock
        self.stock_prices = stock_prices
        self.mf = mf
        self.hist = hist

    def __repr__(self):
        return "Portfolio object. Use print function!"

    def __str__(self):
        print("Cash:")
        print(self.cash)
        print("Stock:")
        print(self.stock)
        print("MutualFund:")
        print(self.mf)
        return("")

    def addCash(self, cash):
        self.cash += cash
        self.hist.append("Added cash:{}".format(cash))


    def withdrawCash(self, cash):
        if self.cash < cash:
            print("Not enough money!")
        else:
            self.cash -= cash
            self.hist.append("Withdrawn cash:{}".format(cash))

    def buyStock(self, n, s): #n= number of shares / s = stock price

        if self.cash < n*s.price:
            print("Not enough money!")
        else:
            self.cash -= n*s.price
            if s.symbol in self.stock.keys():
                self.stock[s.symbol] += n
            else:
                self.stock[s.symbol] = n
            self.stock_prices[s.symbol] = s.price
            self.hist.append(
                "Bought stock: {} shares of ".format(n)
                + s.symbol
                + " for {} dollars per share.".format(s.price)
            )

    def sellStock(self, s, n): # s= stock's symbol / n= shares to be sold

        if s not in self.stock.keys():
            print("Stock not found!")
        elif self.stock[s] < n:
            print("Not enough shares of this stock!")
        else:
            selling_price = np.random.uniform(0.5*self.stock_prices[s], 1.5*self.stock_prices[s])
            self.stock[s] -= n
            if self.stock[s] == 0:
                self.stock.pop(s)
            self.cash += n*selling_price
            self.hist.append(
                "Sold stock: {} shares of ".format(n)
                + s
                + " for {} dollars per share.".format(selling_price)
            )

    def buyMutualFund(self, n, mf):

        if self.cash < n:
            print("Not enough money!")
        else:
            if mf.symbol in self.mf.keys():
                self.mf[mf.symbol] += n
            else:
                self.mf[mf.symbol] = n
            self.hist.append("Bought MutualFund: {} shares of ".format(n) + mf.symbol)

    def sellMutualFund(self, s, n):
        if s not in self.mf.keys():
            print("MutualFund not found!")
        elif self.mf[s] < n:
            print("Not enough shares of this mutual fund")
        else:
            selling_price = np.random.uniform(0.9, 1.2)
            self.mf[s] -= n
            if self.mf[s] == 0:
                self.mf.pop(s)
            self.cash += n*selling_price
            self.hist.append(
                "Sold MutualFund: {} shares of ".format(n)
                + s
                + " for {} dollars per share.".format(selling_price)
            )

    def history(self):
        for item in self.hist:
            print(item)


class Stock():

    def __init__(self, price=0, symbol=""):
        if symbol == "":
            print("Symbol Error!")
        else:
            self.symbol = symbol
            self.price = price


class MutualFund():

    def __init__(self, symbol=""):
        if symbol == "":
            print("Symbol Error!")
        else:
            self.symbol = symbol



if __name__ == "__main__":
    portfolio = Portfolio()
    portfolio.addCash(300.50)
    s = Stock(20, "HFH")
    portfolio.buyStock(5, s)
    mf1 = MutualFund("BRT")
    mf2 = MutualFund("GHT")
    portfolio.buyMutualFund(10.3, mf1)
    portfolio.buyMutualFund(2, mf2)
    print(portfolio)
    portfolio.sellMutualFund("BRT", 3)
    portfolio.sellStock("HFH", 1)
    portfolio.withdrawCash(50)
    portfolio.history()
    print(portfolio)
