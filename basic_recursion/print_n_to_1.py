"""forward recursion"""
def print_n_f(n:int):
    if n<1:
        return
    print(n,end=" ")
    print_n_f(n-1)

print_n_f(3)

"""backward recursion or backtracking"""
def print_n_b(cur:int,n:int):
    if n<1:
        return
    print_n_b(cur+1,n - 1)
    print(cur,end=" ")
    cur-=1


print_n_b(1,3)


