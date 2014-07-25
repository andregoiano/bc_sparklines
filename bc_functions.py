# Copyright BrokerConnector 2014. All rights reserved.
# Author: github.com/andregoiano
# Version 1.0
# http://www.brokerconnector.com/

import math, datetime, json

bcMarket = "Deema 3"
bcUnitListings = [5.1, 5.3, 5.2, 5.6, 5.7, 5.4, 5.5, 5.3, 5.4, 5.6];
bcBidListings = [5.6, 5.7, 5.9, 5.5, 5.6, 5.4];

def marketGap(listings):
	# Prints the number of listings and value gap between highest and lowest
    a = max(listings)
    b = min(listings)
    return len(listings)
    return a / b
    
# print marketGap(bcUnitListings)
# print marketGap(bcBidListings)

def marketBullBearRatio(units, bids):
	# Defines the pendulum between bids and units activities in a market
	a = len(units)
	b = len(bids)
	c = a / b
	if c < 1:
		print "It is a bull market at " + bcMarket
	elif c > 1:
		print "It is a bear market at " + bcMarket
	else:
		print "It is a balanced market at " + bcMarket

# print marketBullBearRatio(bcUnitListings, bcBidListings)

def bidAverageLastFive(bids):
	# Averages the last five bid values of the market and outputs
	a = bids[len(bids) - 6:]
	b = sum(bids) / len(a)
	print b

print bidAverageLastFive(bcBidListings)

def unitAverageLastFive(units):
	# Averages the last five unit values of the market and outputs
	a = units[len(units) - 6:]
	b = sum(units) / len(a)
	print b

print bidAverageLastFive(bcUnitListings)