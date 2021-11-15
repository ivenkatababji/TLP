'''
Given a foreign currency, convert it to INR

currency_conversion.py --help
currency_conversion.py <amount> <currency> <target currency>

e.g.,

100 USD == 7,700 INR
'''

import sys
import json
import ast


def loadData():
    cr_data = None
    #USD is the reference
    with open('./cr-usd.json', "rb") as fh:
        cr_data = json.loads( fh.read().decode("UTF-8") )
        cr_data = ast.literal_eval(json.dumps(cr_data))
    return cr_data

CR_DATA = loadData()

def printUsage():
    print("Usage :")
    print(" currency_conversion.py --help")
    print(" currency_conversion.py <amount> <currency> <target currency>")
 
def printHelp():
    printUsage()
    print("List of Currencies :")
    print(CR_DATA.keys())


args = sys.argv[1:]

if( (len(args) == 1) and (args[0].lower() == "--help")):
    printHelp()
    exit(0)
elif(len(args) != 3):
    print("Invalid Arguments.")
    printUsage()
    exit(1)

amount = float(args[0])
source_currency = args[1].lower()
target_currency = args[2].lower()

print("         Amount : {}".format(amount))
print("Source Currency : {}".format(source_currency))
print("Target Currency : {}".format(target_currency))

source_cur_rate = None
target_cur_rate = None

if(source_currency in CR_DATA):
    source_cur_rate = CR_DATA[source_currency]["rate"]
else:
    print("Error : Unknown currency ({}). Cant convert.".format(
        source_currency))

if(target_currency in CR_DATA):
    target_cur_rate = CR_DATA[target_currency]["rate"]
else:
    print("Error : Unknown currency ({}). Cant convert.".format(
        target_currency))

if(source_cur_rate and target_cur_rate):
    target_val = (amount * target_cur_rate * 1.0) / source_cur_rate
    print("{} {} = {} {}".format(
            amount,
            source_currency,
            target_val,
            target_currency))

exit(0)
