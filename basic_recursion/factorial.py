"""iterative solution"""

def fact_it(n:int):
    fact=1
    if n<1:
        return
    for i in range(n,1,-1):
        fact=fact*i

    print(fact)

fact_it(5)


"""recursion"""

def fact_recur(n:int):
    if n==0:
        return 1

    return n*(fact_recur(n-1))

print(fact_recur(5))