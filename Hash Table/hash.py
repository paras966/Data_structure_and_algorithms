## from list
stock_prices=[]
with open("stock_prices.csv","r") as file:
    for line in file:
        tokens=line.split(',')
        day=tokens[0]
        price=float(tokens[1])
        stock_prices.append([day,price])

print(stock_prices)

for element in stock_prices:
    if element[0]=="7_March":
        print(element[1])

### BY DICTIONARY
from turtle import st


stock_prices={}
with open("stock_prices.csv","r") as file:
    for line in file:
        tokens=line.split(',')
        day=tokens[0]
        price=float(tokens[1])
        stock_prices[day]=price
# print(stock_prices)

print(stock_prices['8_March'])

### Using Hashtable

class HashTable:
    def __init__(self):
        self.MAX=100
        self.arr=[None ]
