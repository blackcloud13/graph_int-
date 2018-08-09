import xlsxwriter
import json
import requests
import random
import datetime
import time
#  import sqlite




#########################
### Define Functions ####
#########################


# This function creates Random Price within +/-10% of a given price
# Question - why do you think this is useful?
def nextPrice(currentPrice):
    return (currentPrice * (1 + random.randint(-200, 200)/2000))


#  This function gets the current price of a given currency
#  See Lesson 16 for an answer to your question on picking on specific currency


def getCryptoPrice(currencyID):
    ticker_url = 'https://api.coinmarketcap.com/v2/ticker/' + str(currencyID) + '/?structure=array'

    request = requests.get(ticker_url)
    results = request.json()
    data = results['data'][0]


    price = quotes['price']

    return(price)

## this function gets the id of a given crypto ccy

def getCryptoID(ccy):
    
    listings_url = 'https://api.coinmarketcap.com/v2/listings/'

    request = requests.get(listings_url)
    results = request.json()
    
    data = results['data'][0]


def getAllListings():


    listings_url = 'https://api.coinmarketcap.com/v2/listings/'

    request = requests.get(listings_url)
    results = request.json()


    
    #  data = results['data'][0]

    return results['data']

def getTickerList():

    allRefData = getAllListings()
    tickerDict = {}

    for item in allRefData:
        symbol = item['symbol']
        ccyID = item['id']
        tickerDict[symbol] = ccyID

    return tickerDict


def getTickerForSymbol(aSymbol):
    d1 = getTickerList()
    return d1[aSymbol.upper()]

    

####################################
####  Run Scripts and test code ####
####################################

start = 1
f = 1
convert = 'USD'
delayInSeconds = 1
maxLoops = 1

crypto_workbook = xlsxwriter.Workbook('price_graph3.xlsx')
crypto_sheet = crypto_workbook.add_worksheet()

crypto_sheet.write('A1', 'Name')
crypto_sheet.write('B1', 'Symbol')
crypto_sheet.write('C1', 'Price')

currencyID = 1


ticker_url = 'https://api.coinmarketcap.com/v2/ticker/' + str(currencyID) + '/?structure=array'

request = requests.get(ticker_url)
results = request.json()
data = results['data']
currency = data[0]

name = currency['name']
symbol = currency['symbol']
quotes = currency['quotes'][convert]
price = quotes['price']


print(price)

loopCounter = 0
while loopCounter < maxLoops:

    price = nextPrice(price)
#    price = getCryptoPrice(currencyID)

    print (f)
    print (loopCounter)
    print(price)

    #write to sheet
    crypto_sheet.write(f,0,name)
    crypto_sheet.write(f,1,symbol)
    crypto_sheet.write(f,2,price)

    loopCounter += 1
    f += 1

    time.sleep(delayInSeconds)


print (f)
print (loopCounter)
print ('Closing Book')
crypto_workbook.close()




    
currentPrice = 12.0
newPrice = nextPrice(currentPrice)

print (currentPrice)


## mini tests of ticker code
l1= getAllListings()
d1 = getTickerList()
cccy = 'btc'
t1 = getTickerForSymbol(cccy)
print (cccy)
print(t1)



##  See example of Currency and Ticker from a list
aList = ['btc','eth','ltc','bcc','xrp', 'bch']
d2  = {}

for cccy in aList:
    d2[cccy] = getTickerForSymbol(cccy)


print (d2)


## TEST Print Bitcoin Ticker
ticker = d2['btc']
print ('Bitcoin ticker is : ' + str(ticker))

ticker = d2['eth']
print ('Ethereum ticker is : ' + str(ticker))

