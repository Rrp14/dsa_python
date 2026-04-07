def find_root(v,m):

    left,right=1,v

    while left<=right:

        mid=(left+right)//2
        val=power(mid,m,v)

        if val== v:
            return mid
        elif val>v:
            right=mid-1
        else:
            left=mid+1

    return  -1

def power(mid, m, v):
    result = 1
    for _ in range(m):
        result *= mid
        if result > v:   # early stop (important optimization)
            return result
    return result

res=find_root(69,4)
print(res)