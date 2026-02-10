"""brute force"""
import math


def is_prime(n:int)->bool:
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    return count==2

print(is_prime(10))

"""optimal [ if n has factor above sqrt(n) than n would have same factor below sqrt(n)] """

def is_prime_op(n:int)->bool:

    if n<=1:
        return False

    for i in range (2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True



print(is_prime_op(10))
