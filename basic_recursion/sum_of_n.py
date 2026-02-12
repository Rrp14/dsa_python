"""brute force"""
"""t=O(n),s=O(1)"""
def sum_n_bf(n:int):
    total=0

    for i in range(n+1):
        total+=i
    print(total)

sum_n_bf(5)



"""formula"""
"""use sum=N(N+1)/2"""
"""t=O(n),s=O(n)"""
def sum_n_form(n:int):
    total= n*(n+1) / 2
    print(int(total))

sum_n_form(5)



"""recursion"""

def sum_n_recur(n:int):

    if n==1:
        return n

    return n+ sum_n_recur(n-1)

print(sum_n_recur(5))


