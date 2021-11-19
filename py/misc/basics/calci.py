'''
Calculator
Demonstrate Functions
Support following operators
    +
    -
    *
    /
    %
'''

def sum(a, b):
    print('--> sum')
    return a + b

def sub(a, b):
    print('--> sub')
    return a - b

def mul(a, b):
    return a*b

def div(a, b):
    return a/b

'''
reminder(a,b)
    Devide the a with b and return the reminder

Integer Calculations
Floating Point Calculations

'''
def reminder1(n, d):
    r = 0
    #compute reminder
    #TODO : Implement this without using % operator
    q = n / d
    r = n - (q*d)
    return r

def reminder2(n, d):
    while(n >= d):
        n = n - d
    return n

def reminder(n, d):
    return reminder1(n,d)


'''
is_odd(x)
    determine whether the given is odd or not
    return true if odd
    return false if not odd
'''
def is_odd(a):
    r = reminder(a, 2)
    if (r == 1):
        return True
    else:
        return False

def is_even(a):
    return not (is_odd(a))


x = 11
if(is_odd(x)):
    print("{0} is Odd".format(x))
else:
    print("{0} is Even".format(x))




