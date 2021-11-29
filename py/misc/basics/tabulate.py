


def convert(sc, tc):
    return "{}x{}".format(sc,tc)

def tabulate_cur_conv(cur_list):
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
            row += convert(sc, tc).center(11)
        print(row)


cur_list_input = ['inr', 'sgd', 'usd']
tabulate_cur_conv(cur_list_input)
        
