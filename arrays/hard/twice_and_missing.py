from typing import Counter



def twice_missing(nums):
    res=[0]*2
    helper=0
    twice=Counter(nums)

    for k,v in twice.items():
        if v==2:
            res[0]=k
        if int(k)-1==helper:
            helper+=1
        else:
            res[1]=helper+1
    return res

"""better one"""
from collections import Counter

def twice_missing_2(nums):
    res=[]
    helper=0
    twice=Counter(nums)

    for k in sorted(twice):   # fix here
        v=twice[k]

        if v==2:
            res.append(k)

        if k-1==helper:
            helper+=1
        else:
            res.append(helper+1)
            break

    return res

print(twice_missing([3,5,4,1,1]))










result=twice_missing([3, 5, 4, 1, 1,])
print(result)