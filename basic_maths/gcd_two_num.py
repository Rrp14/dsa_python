
"""brute force"""
def find_gcd_bf(n1:int,n2:int)->int:
    gcd = 1
    minimum=min(n1,n2)

    for i in range(1,minimum):
        if n1%i==0 and n2%i==0:
            gcd=i
    return gcd



print(find_gcd_bf(20,15))


"""better approach"""

def find_gcd_ba(n1:int,n2:int)->int:

    minimum=min(n1,n2)

    for i in range(minimum,1,-1):
        if n1%i==0 and n2%i==0:
            return i
    return 1


print(find_gcd_ba(20,15))

"""optimal approach:euclidean algorithm"""

def e_gcd(n1:int,n2:int)->int:
    while n2:
        n1,n2=n2,n1%n2
        """take20,15 .. n1 will be n2 ie 15 and n2 will be 20%15=5 , 
        again n1 will be n2 ie 5 and n2 will be 15%5=0 loop breaks n1=5 """

    return n1


print(e_gcd(15,20))



