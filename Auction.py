#!/usr/bin/python
import Bid, Slot
import itertools


class Auction:
    'This class represents an auction of multiple ad slots to multiple advertisers'
    query = ""
    bids = []

    def __init__(self, term, bids1=[]):
        self.query = term

        for b in bids1:
            j = 0
            # print(len(self.bids))
            while j < len(self.bids) and float(b.value) < float(self.bids[j].value):
                j += 1
            self.bids.insert(j, b)

    '''
    This method accepts a Vector of slots and fills it with the results
    of a VCG auction. The competition for those slots is specified in the bids Vector.
    @param slots a Vector of Slots, which (on entry) specifies only the clickThruRates
    and (on exit) also specifies the name of the bidder who won that slot,
    the price said bidder must pay,
    and the expected profit for the bidder.
    '''

    def executeVCG(self, slots):
        bids = self.bids
        for index, slot in reversed(list(enumerate(slots))):
            if len(bids) > len(slots):
                if index < len(slots) - 1:
                    for ind, bid in reversed(list(enumerate(bids))):
                        if ind == index:
                            print ind, bid.name, bid.value, slots[index].clickThruRate, slots[index + 1].clickThruRate
                            slot.bidder = bid.name
                            slot.price = (float(slots[index].clickThruRate - slots[index + 1].clickThruRate)) * float(
                                bids[ind + 1].value) + float(slots[index + 1].price)
                            slot.profit = (float(slots[index].clickThruRate) * float(bids[index].value)) - slot.price
                else:
                    for ind, bid in reversed(list(enumerate(bids))):
                        if ind == index:
                            slot.bidder = bid.name
                            slot.price = (float(slots[index].clickThruRate - 0)) * float(
                                bids[ind + 1].value) + 0
                            slot.profit = (float(slots[index].clickThruRate) * float(bids[index].value)) - slot.price
            else:
                if index < len(bids) - 1:
                    for ind, bid in reversed(list(enumerate(bids))):
                        if ind == index:
                            print ind, bid.name, bid.value, slots[index].clickThruRate, slots[index + 1].clickThruRate
                            slot.bidder = bid.name
                            slot.price = (float(slots[index].clickThruRate - slots[index + 1].clickThruRate)) * float(
                                bids[ind + 1].value) + float(slots[index + 1].price)
                            slot.profit = (float(slots[index].clickThruRate) * float(bids[index].value)) - slot.price
                else:
                    for ind, bid in reversed(list(enumerate(bids))):
                        if ind == index:
                            slot.bidder = bid.name
                            slot.price = (float(slots[index].clickThruRate - 0)) * 0 + 0
                            slot.profit = (float(slots[index].clickThruRate) * float(bids[index].value)) - slot.price
