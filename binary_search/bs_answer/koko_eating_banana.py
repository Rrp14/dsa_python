import math


def total_hours(piles,speed):
    totalH=0

    for banana  in piles:
        totalH+=math.ceil(banana/speed)

    return totalH


def answer(piles,hour):
    if not piles:
        return 0

    n=len(piles)
    left,right=1,max(piles)
    ans=right

    while left<=right:
        mid=(left+right)//2

        hours=total_hours(piles,mid)

        if hours<=hour:
            ans=mid
            right=mid-1
        else:
            left=mid+1


    return ans


piles = [3, 6, 7, 11]
hour = 8
res=answer(piles,hour)

print(res)