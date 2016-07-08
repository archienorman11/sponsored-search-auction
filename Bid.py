#!/usr/bin/python

class Bid:
    'represents a bid in a Sponsored Search Auction'
    value = 0.0  # the value to this bidder of a click
    name = ""  # the name of this bidder

    def __init__(self, line):
        if line is not None:
            self.value = float(line.split('\t')[0])
            self.name = line.split('\t')[1]
        else:
            self.value = 0
            self.name = "empty"

            # def toString(temp):
            #	print ("bid:%6.2f %s"%(value,name))
            #	return ("bid:%6.2f %s"%(value,name))
