"""brute force approach"""
import math


def get_all_divisors_bf(n:int)->list[int]:
    l=[]
    for i in range(1,n+1):
        if n%i==0:
            l.append(i)
    return l

print(get_all_divisors_bf(36))

"""optimal solution"""
def get_all_divisor_op(n:int)->list[int]:
    l=[]
    """ex:- n=36.  i=1,36%1==0 append 1 [1] , 1 is not equal to 36//1 so append 36 """
    for i in range(1,int(math.sqrt(n))+1):
        if n%i==0:
            l.append(i)
            """i X j(something) = n , after square root things repeat"""
            if i!=n//i:
                l.append(n//i)
    l.sort()
    return l

print(get_all_divisor_op(36))

