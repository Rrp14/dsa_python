"""hacked approach converting to string to make code simple"""
import math


def find_armstrong(n:int)->bool:
    s=str(n)
    l=len(s)
    total=0

    for digit in s:
        total+=int(digit)**l

    return total==n

print(find_armstrong(0))


"""real mathematical approach"""
def find_armstrong_ma(n:int)->bool:
    if n==0:
        count=1
    else:
     count=int(math.log10(n)+1)
    """or just use count=len(str(n)"""

    total=0
    temp=n

    while n>0:
        i=n%10
        total+=i**count
        n=n//10
    return total==temp

print(find_armstrong_ma(0))



