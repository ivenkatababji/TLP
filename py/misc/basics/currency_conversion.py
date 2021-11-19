'''
Given a foreign currency, convert it to INR

currency_conversion.py --help [1/2]
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
    print(" currency_conversion.py --help [1/2]")
    print(" currency_conversion.py <amount> <currency> <target currency>")
 
def printHelp(level):
    printUsage()
    if(level == 1):
        print("List of Currencies :")
        print(CR_DATA.keys())
    elif(level == 2):
        print("List of Currencies (ex) :")
        for currency in CR_DATA.keys():
            print("{} : {}".format(currency, CR_DATA[currency]["name"]))

def convert_cur(amount, source_currency, target_currency):
    source_cur_rate = CR_DATA[source_currency]["rate"]
    target_cur_rate = CR_DATA[target_currency]["rate"]
    return (amount * target_cur_rate * 1.0) / source_cur_rate


'''''''''''''''''''''''''''''''''
        Main Processing
'''''''''''''''''''''''''''''''''
args = sys.argv[1:]

#
#Argument Validation and Processing
#
if(len(args) == 0):
    printHelp(0)
    exit(0)
else:
    if(args[0].lower() == "--help"):
        level = 1
        if(len(args) == 2):
            level = int(args[1])
        printHelp(level)
        exit(0)
    elif(len(args) != 3):
        print("Invalid Arguments.")
        printUsage()
        exit(1)

#
#Input Initialisation
#
amount = float(args[0])
source_currency = args[1].lower()
target_currency = args[2].lower()

#
#Input Validation
#
if(source_currency not in CR_DATA):
    print("Error : Unknown currency ({}). Cant convert.".format(
        source_currency))
elif(target_currency not in CR_DATA):
    print("Error : Unknown currency ({}). Cant convert.".format(
        target_currency))
else:
    #
    # Currency Conversion
    #
    target_val = convert_cur(amount, source_currency, target_currency)

    #
    # Generate Results (output)
    #
    
    print("         Amount : {}".format(amount))

    print("Source Currency : {} ({})".format(
        source_currency, 
        CR_DATA[source_currency]["name"]))

    print("Target Currency : {} ({})".format(
        target_currency,
        CR_DATA[target_currency]["name"]))

    print("{} {} = {} {}".format(
                amount,
                source_currency,
                target_val,
                target_currency))

exit(0)
