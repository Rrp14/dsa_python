"""brute force"""
import math


def dig_counter(n:int)->int:
    if n==0:
        return 1
    counter = 0

    while n> 0:
        counter += 1
        n= n//10

    return counter
"""T=O(log10(N+1))
   S=O(1)"""


"""optimal"""

def opt_digi_counter(n:int)->int:
    if n==0:
        return 1

    return int(math.log10(n)+1)



print(opt_digi_counter(1000))

"""T&S=O(1)"""

"""log10 gives power to which the number needs to be raised 
for eg: log10(1234) is 3 i.e 10^3 is 1000 we add +1 to get number of digits 3+1 is 4 
because power is always 1 less then digit count """


