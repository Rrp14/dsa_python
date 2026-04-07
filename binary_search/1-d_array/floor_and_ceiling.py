def find(nums,x):
    n=len(nums)
    left=0
    right=n-1
    floor=float("-inf")
    ceiling=float('inf')

    while left<=right:
        mid=(left+right)//2
        if nums[mid]<=x:
            floor=nums[mid]
            left=mid+1
        else:
            ceiling=nums[mid]
            right=mid-1


    return [floor,ceiling]

res=find([3, 4, 4, 7, 8, 10],5)
print(res)
