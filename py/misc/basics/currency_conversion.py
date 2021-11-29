'''
Given a foreign currency, convert it to INR

currency_conversion.py --help [1/2] [reference currency]
currency_conversion.py <amount> <currency> <target currency>
currency_conversion.py --matrix usd inr sgd pkr

              usd       inr       sgd       pkr
    usd      1.000     77.04      1.35     172.29
    inr      0.013     1.00       0.02      2.31
    sgd      0.73      55.01      1.00     127.29
    pkr      0.006     0.432      0.008     1.00 

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

def convert_cur(amount, source_currency, target_currency):
    source_cur_rate = CR_DATA[source_currency]["rate"]
    target_cur_rate = CR_DATA[target_currency]["rate"]
    return (amount * target_cur_rate * 1.0) / source_cur_rate

def printUsage():
    print("Usage :")
    print(" currency_conversion.py --help [1/2] [reference currency]")
    print("    reference currency is applicable for help level 2")
    print("")
    print(" currency_conversion.py --convert <amount> <currency> <target currency>")
    print("")
    print(" currency_conversion.py --matrix <currency> <currency> ...")
 
def tabulateCurConv(cur_list):
    #prepare column heade
    # each currency code padded with some space
    col_header = "     "
    for c in cur_list:
        col_header += c.center(11)
    print(col_header)

    #print each row : <SOURCE>  <VALUE> <VALUE> ..... 
    # The <value> for each of the target currency
    # The <alue> to be printer below the target currency 
    for sc in cur_list:
        row = sc.ljust(5)
        for tc in cur_list:
            row += "{:.4f}".format(convert_cur(1, sc, tc)).center(11)
        print(row)


def printHelp(level, ref_currency = None):
    printUsage()
    if(level == 1):
        print("List of Currencies :")
        print(CR_DATA.keys())
    elif(level == 2):
        if(not ref_currency):
            print("List of Currencies (ex) :")
            for currency in CR_DATA.keys():
                print("{} : {}".format(
                    currency, 
                    CR_DATA[currency]["name"]))
        else:
            print("List of Currencies (ex) :")
            for currency in CR_DATA.keys():
                print("{} : {} ({} / {})".format(
                    currency, 
                    CR_DATA[currency]["name"],
                    convert_cur(1, ref_currency, currency),
                    ref_currency))

def validateCurrencyList(cur_list):
    retVal = True
    for c in cur_list:
        if(c not in CR_DATA):
            print("Error : Unknown currency ({})".format(c))
            retVal = False
    return retVal

def curConvert(amount, source_currency, target_currency):
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
    #---------------------------------------------------------
    mode = args[0].lower()
    if(mode == "--help"):
        level = 1
        if(len(args) >= 2):
            level = int(args[1])
        ref_currency = None
        if(len(args) == 3):
            ref_currency = args[2]
            if(not validateCurrencyList([ref_currency])):
                exit(0)
        printHelp(level, ref_currency)
        exit(0)
    #---------------------------------------------------------
    elif(mode == "--matrix"):
        if(len(args) < 3):
            print("Invalid Arguments")
            printUsage()
            exit(1)
        else:
            cur_list_input = args[1:]
            if(validateCurrencyList(cur_list_input)):
                tabulateCurConv(cur_list_input)
            exit(0)
    #---------------------------------------------------------
    elif(mode == "--convert"):
        amount = float(args[1])
        source_currency = args[2].lower()
        target_currency = args[3].lower()
        if(validateCurrencyList([source_currency, target_currency])):
            curConvert(amount, source_currency, target_currency)
    #---------------------------------------------------------
    else:
        print("Invalid Arguments.")
        printUsage()
        exit(1)

exit(0)
