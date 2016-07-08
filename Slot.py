#!/usr/bin/python

class Slot:
    'represents a slot where an ad can be posted'
    clickThruRate = 0  # the number of clicks expected
    price = 0  # price to be paid for those clicks
    profit = 0  # profit expected from those clicks
    bidder = 0  # the Bid that wins this slot

    def __init__(self, ctr):
        if ctr is not None:
            self.clickThruRate = float(ctr)
        else:
            self.clickThruRate = 0

        # def toString(temp):
        # print ("slot: %6.2f %8.2f %8.2f   %s" %(self.clickThruRate,self.price,self.profit,self.bidder))
        # return ("slot: %6.2f %8.2f %8.2f   %s" %(self.clickThruRate,self.price,self.profit,self.bidder))
