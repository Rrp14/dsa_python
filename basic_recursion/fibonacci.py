from typing import List

"""brute force"""
def find_fibonacci(n:int):
    if n==0:
        return 0
    if n==1:
        return 1

    fib=[0]*(n+1)

    fib[0],fib[1]=0,1

    for i in range(2,n+1):
        fib[i]=fib[i-1]+fib[i-2]

    return fib

print(find_fibonacci(5))

"""better approach"""

def find_fib_ba(n:int):
    if n==0:
        print(0)
    if n==1:
        print(0,1)

    last_term=1
    second_last_term=0

    print(0,1,end=" ")

    for i in range(2,n+1):
        i_term=last_term+second_last_term
        print(i_term,end=" ")
        second_last_term=last_term
        last_term=i_term
    return None

find_fib_ba(5)


"""recursion"""
def find_fib_rec(n:int):
    if n<=1:
        return n

    return find_fib_rec(n-1)+find_fib_rec(n-2)

ans=find_fib_rec(5)
print("\n",ans)





