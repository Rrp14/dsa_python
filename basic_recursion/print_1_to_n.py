"""forward recursion"""
def print_n_f(cur,n:int):
    if cur>n:
        return
    print(cur,end=" ")
    print_n_f(cur+1,n)

print_n_f(1,3)

"""backward recursion or backtracking"""
def print_n_b(n:int):
    if n<1:
        return
    print_n_b(n-1)
    print(n,end=" ")

print_n_b(3)






